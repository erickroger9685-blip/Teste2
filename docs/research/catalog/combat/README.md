# Seção C — Combate

> Escopo: framework de combate, hitbox, lock-on, state machine, combo, block/parry/dodge, knockback/ragdoll, projéteis e lag compensation.
> Todos os candidatos estão em [`../../data/catalog.csv`](../../data/catalog.csv) (`category=combat`). As auditorias estão em [`../../security-audits/`](../../security-audits/README.md).

## Veredito da categoria

**Não existe um framework de combate "estilo Naruto Storm" pronto, licenciado e maduro.** O que o ecossistema oferece:

- **Blocos maduros e reutilizáveis:** detecção de hit (ShapecastHitbox), projéteis (FastCast2), ragdoll (RagdollService) e compensação de latência para ataques à distância (RollbackHitbox).
- **Um bom modelo conceitual:** WCS (skills, status effects, movesets, damage modifiers). Porém é TypeScript/Flamework e traz uma pilha de rede própria.
- **A fundação oficial mudou em 2026.** O [Server Authority](https://create.roblox.com/docs/projects/server-authority) nativo (predição e rollback) e o [Input Action System](https://create.roblox.com/docs/input/input-action-system) resolvem, dentro da engine, o que Chickynoid, Rewind e similares tentavam resolver. Segundo a própria documentação, o combate deve rodar em `RunService:BindToSimulation()` com estado em atributos sincronizados.

**Decisão:** **construir** o núcleo de combate (máquina de estados, combos, block/parry/dodge, hitstun, knockback, pipeline de dano), **reutilizar** hitbox, ragdoll e projéteis através de *adapters*, e **usar o WCS como referência de design**.

---

## Candidatos principais (fichas)

### Projeto: TeamSwordphin/ShapecastHitbox
- **URL:** https://github.com/TeamSwordphin/ShapecastHitbox
- **Licença:** MIT (LICENSE.md no clone; `wally.toml` também declara MIT)
- **Arquitetura:** biblioteca `shared` sem dependências. `init.luau` (registro) + `Hitbox.luau` (objeto hitbox) + `Solvers/` (Raycast, Blockcast, Spherecast, Attachment, Bone) + `Visualizers/` (debug). Cada hitbox conecta seu próprio `RunService.PostSimulation`.
- **Recursos:** `hitbox:HitStart()`, `HitStop()`, `OnHit()`, `OnUpdate()`, `OnStopped()`, `SetResolution()`, `SetCastData()`, segmentos (`AddSegment`/`RemoveSegment`), `Reconcile()`, pontos marcados por tag/atributo (`DmgPoint`), cast por Attachments/Bones (ideal para armas e membros animados).
- **Pontos fortes:** sucessor oficial do RaycastHitboxV4 (mesmo autor); 10/14 arquivos `--!strict`; zero dependências; shapecasts (bloco e esfera) cobrem golpes largos, não só raios.
- **Problemas:** 24 commits, 1 autor e último commit em 2025-08-12, portanto baixa atividade. README sem documentação ("Installation: To do"); a documentação está no DevForum. Uma conexão `PostSimulation` por hitbox ativa pesa com muitos NPCs atacando ao mesmo tempo.
- **Dependências:** nenhuma.
- **Compatibilidade:** 🛠️ **REQUIRES ADAPTATION**. Os solvers são reutilizáveis, mas o loop de atualização precisa ser centralizado e rodar dentro de `BindToSimulation` (Server Authority).
- **O que reutilizar:** `Solvers/*`, tipos e lógica de segmentos e resolução.
- **O que reescrever:** o agendamento (um único loop para todas as hitboxes ativas), a integração com o pipeline de dano e a filtragem de alvos (times, i-frames, "já atingido neste golpe").
- **Integração (§25):** (1) recebe comandos do `CombatService` e emite `OnHit` para o adapter, que converte em `HitEvent`; (2) nenhuma dependência; (3) API de objeto hitbox; (4) assume Parts/Attachments no rig ou arma; (5) conflito de loop com o scheduler da simulação; (6) ~2–3 arquivos de adaptação; (7) sim, usar só os solvers.

### Projeto: wad4444/WCS
- **URL:** https://github.com/wad4444/WCS · docs: https://wad4444.github.io/WCS/
- **Licença:** MIT (`LICENSE.txt`). O pacote Wally é publicado no escopo `cheetiedotpy/wcs`, que precisa ser confirmado como do mesmo autor.
- **Arquitetura:** fonte em **TypeScript** (`src/source/*.ts`, ~3,3k linhas) compilada para Luau. Classes `Character` (`ApplyMoveset`, `GetSkills`, `TakeDamage`, `PredictDamage`, `GetAllActiveStatusEffects`…), `Skill`, `HoldableSkill`, `StatusEffect` e `Moveset`. Rede via `@flamework/networking` (eventos `requestSkill`, `messageToServer`, `sync`). Estado replicado com `@rbxts/charm-sync`.
- **Recursos:** skills com cooldown no servidor (`ApplyCooldown`), `MutualExclusives`/`Requirements` por status, `ShouldStart`, skills "seguráveis", status effects com ciclo de vida, movesets, modificadores de dano, mensagens cliente↔servidor tipadas com validators.
- **Pontos fortes:** modelagem madura (512 commits, 22 tags, 9 autores); validação de dono do personagem no servidor; separação clara entre skill e status.
- **Problemas:** apenas 1 commit nos últimos 12 meses (último 2025-11-12). O pacote embute um runtime Flamework mais charm/charm-sync/janitor/t, o que cria uma **segunda pilha de rede e estado** paralela ao Blink/Charm do projeto (a "colcha de retalhos" do §25). Não é desenhado para o `BindToSimulation` do Server Authority. Os parâmetros do cliente chegam direto em `Skill.Start(...)` e não há rate limit.
- **Dependências:** @flamework/core, @flamework/networking, @rbxts/charm, @rbxts/charm-sync, @rbxts/flamework-binary-serializer, @rbxts/immut, @rbxts/janitor, @rbxts/services, @rbxts/sleitnick-signal, @rbxts/t, @rbxts/timer.
- **Compatibilidade:** 📖 **USE AS REFERENCE ONLY**. Adotá-lo significaria aceitar TS/Flamework e uma rede concorrente.
- **O que reutilizar (como design):** o vocabulário e o contrato Skill/HoldableSkill/StatusEffect/Moveset/DamageContainer; `MutualExclusives`/`Requirements`; o cooldown autoritativo com timestamp replicado.
- **O que reescrever:** tudo em Luau como `AbilityRuntime` e `StatusRuntime` próprios, integrados ao Server Authority e à rede Blink.

### Projeto: weenachuangkud/FastCast2
- **URL:** https://github.com/weenachuangkud/FastCast2 · docs: https://weenachuangkud.github.io/FastCast2/
- **Licença:** MIT para o **código** (`LICENSE-MIT`). **CC BY-NC-ND 4.0 para a arte e os logos** (`LICENSE-ART`), que não podem ser usados.
- **Arquitetura:** `FastCastParallel` / `FastCastSerial` (`RaycastFire`, `BlockcastFire`, `SpherecastFire`), VMs de cliente e servidor em Actors (Parallel Luau), `ObjectCache` para projéteis visuais, `newBehavior()` para configurar.
- **Pontos fortes:** projéteis por cast (sem física replicada); raycast, blockcast e spherecast; Parallel Luau; muito ativo (1.205 commits em 12 meses, 9 autores, 8 tags).
- **Problemas:** o volume de commits indica API ainda em movimento. É novo (primeiro commit em 2025-11-22) e tem só 4/17 arquivos `--!strict`.
- **Compatibilidade:** 🛠️ **REQUIRES ADAPTATION**. Encapsular num `ProjectileService` que decide o dano no servidor. O cliente só renderiza.
- **O que reutilizar:** simulação de cast e parallel VMs. **O que reescrever:** o hook de dano, a replicação de spawn via Blink e a validação de origem e direção.

### Projeto: Brawldude2/RagdollService
- **URL:** https://github.com/Brawldude2/RagdollService
- **Licença:** MIT (LICENSE atual, alterada em março de 2026; o ecosyste.ms ainda mostra LGPL-3.0). **Fixar o commit adotado.**
- **Arquitetura:** `Ragdoll(character, rigType?)`, `Unragdoll`, `IsRagdolled`, `SetupRagdoll`; configs por rig (R6, R15, R15Legacy); remote para ativar localmente no jogador.
- **Pontos fortes:** 9/9 arquivos `--!strict`; suporte a R6/R15; pequeno (~1k linhas).
- **Problemas:** 1 autor, 27 commits (todos em 2026). A interação com Server Authority e CCL (ControllerManager) não foi testada pelo autor.
- **Compatibilidade:** 🛠️ **REQUIRES ADAPTATION**. Validar com o CCL e o Server Authority em protótipo.

### Projeto: michaelvqq/RollbackHitbox
- **URL:** https://github.com/michaelvqq/RollbackHitbox
- **Licença:** MIT (adicionada em 2026-07-09; antes disso não tinha licença).
- **Arquitetura:** `RegisterCharacter`, `RecordAll`/`RecordSnapshot` (buffer circular ~60 Hz), `GetInterpolatedSnapshot`, `ValidateHit` (interseção OBB).
- **Pontos fortes:** 5/5 arquivos `--!strict`; algoritmo claro (busca binária com interpolação).
- **Problemas:** 10 commits, projeto novo. Foco em hitscan: o próprio autor diz que a direção do tiro é confiada ao cliente e recomenda raycast de linha de visão no servidor.
- **Compatibilidade:** 🛠️ **REQUIRES ADAPTATION**, só para habilidades à distância e hitscan. Para melee sob Server Authority, a simulação predita já cobre a maior parte.

---

## Hitbox: comparação

| Projeto | Licença | Método | Onde roda | Estado | Decisão |
| --- | --- | --- | --- | --- | --- |
| ShapecastHitbox | MIT | Raycast/Blockcast/Spherecast por segmento | cliente ou servidor | 2025-08, 1 autor | 🛠️ adaptar (escolhido) |
| RaycastHitboxV4 | MIT | Raycast por attachments | idem | 2021-09 | 📖 superado |
| MuchachoHitbox | MIT | Spatial queries (GetPartBoundsInBox/Radius) + predição | idem | só `.rbxm` (auditado por extração) | 📖 referência de API |
| ClientCast | MIT | Raycast no cliente + envio ao servidor | cliente→servidor | 2023-09 | 📖 **confia no cliente** |
| HitboxClass v2 | sem licença | spatial queries | servidor | Creator Store | ⛔ NÃO CONFIRMADO |
| HitMesh-Pro, Attachment-Based-Raycast | sem licença | — | — | — | ⛔ |

**Recomendação de arquitetura de hit:** para melee, fazer shapecast **no servidor** (autoritativo) dentro da simulação. Com Server Authority, o cliente prediz a mesma simulação e o feedback fica imediato. Para ataques à distância, usar FastCast2 no servidor, e só quando a latência pesar, adicionar rewind (RollbackHitbox) e raycast de linha de visão.

## Lock-on / targeting

| Projeto | Licença | Observação | Decisão |
| --- | --- | --- | --- |
| EzLockOn (DevForum/Creator Store) | sem licença | só cliente; mira a `Head` | ⛔ NÃO CONFIRMADO |
| "Lock-On Combat in 3D" (DevForum) | não verificado | pista do gist | — |
| Repositórios "camlock" no GitHub | — | scripts de exploit/aimbot | ⛔ descartados |

**Construir:** `TargetingService` (servidor valida o alvo: alcance, linha de visão, time, estado vivo) + `LockOnController` (câmera e indicador no cliente). São poucas centenas de linhas, e ter o código próprio é necessário para integrar com a câmera de combate. Ver [câmera](../camera/README.md).

## State machine, combo, block, parry, dodge, knockback

| Necessidade | Solução pronta encontrada? | Decisão |
| --- | --- | --- |
| Estados de combate (idle, attacking, hitstun, stagger, blocking, guard-broken, dodging, airborne, knocked, ragdolled) | FSMs genéricas (RobloxStateMachine MIT, parado desde 2024-05; várias no Wally) | **Construir** FSM de combate orientada a dados, com estado em atributos escritos só dentro de `BindToSimulation` (recomendação oficial para rollback) |
| Combos e branching | Nenhum sistema dedicado com licença | **Construir** grafo de combo em dados (nós = golpes; arestas = input + janela de tempo) |
| Block, guard break, parry, i-frames | Só em exemplos sem licença | **Construir** dentro do pipeline de dano (ordem: i-frame → parry → block → dano) |
| Hitstop, camera shake, FOV | RbxCameraShaker (MIT), spr (MIT) | **Reutilizar** no cliente (ver [câmera](../camera/README.md)) |
| Knockback, launchers | Módulos do DevForum sem licença | **Construir** (impulso/LinearVelocity no personagem autoritativo) |
| Ragdoll | RagdollService (MIT) | 🛠️ adaptar |
| Cooldowns e energia | WCS (referência); módulos do DevForum | **Construir** no `AbilityRuntime` (cooldown autoritativo com timestamp replicado) |

## Descartados por licença ou qualidade (resumo)

`text21/Rewind` (sem licença), `JoshuaIO/Fighting-Game-Framework-RobloxAPI`, `rinme/UntitledGame`, `galenamc/Roblox-CombatSystem`, `elomala/Fighting-game`, `idiomic/Roblox_Sword_Fighting_AI` (sem licença), `aziz8235/roblox-luau-game-framework` (repositório sem código), `1Axen/Secure-Cast` (arquivado, só referência), `hatmatty/AMS` (2022, TS, só referência). Detalhes no CSV.
