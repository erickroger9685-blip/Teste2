# Plano de implementação incremental (brief §29): integração com Claude Code

> Pré-condição: esta pesquisa aprovada. **Nenhuma fase importa código sem**: licença confirmada no CSV, auditoria em `security-audits/`, versão e escopo fixados e registro em `THIRD_PARTY.md`.
> Ferramenta de IA: **Claude Code** no repositório (Rojo/Git) + **MCP embutido do Roblox Studio** (Assistant → MCP Servers → *Enable Studio as MCP server*; Claude Code aparece na lista de quick-connect oficial). O MCP permite ler e editar scripts, rodar código e automatizar playtests. Toda edição feita via MCP precisa ser **revisada antes de publicar**, como a própria Roblox recomenda.

## Fluxo de trabalho com Claude Code (vale para todas as fases)

1. O código-fonte vive **no repositório** (Rojo). O Studio só recebe sync. O MCP serve para **inspecionar, rodar playtests e testes**, não para ser a fonte do código.
2. Cada fase = branch + PR, com CI: `selene`, `stylua --check`, `luau-lsp analyze` (strict), testes Jest-Lua via Lune e `lune run validate-content`.
3. Um `CLAUDE.md` na raiz documenta a arquitetura (este diretório), as regras de fronteira de confiança e o "um dono por estado".
4. Toda dependência nova passa pelo [checklist de segurança](00-methodology/security-checklist.md) antes do merge.

---

## Fase 1: Core architecture

- **Repositórios e ferramentas:** Rojo, Rokit, Wally, Selene, StyLua, luau-lsp, Lune, Jest-Lua, wally-package-types, Blink, Asphalt.
- **Dependências (Wally, versões exatas):** `sleitnick/signal`, `sleitnick/trove`, `sleitnick/table-util`, `sleitnick/timer`, `osyrisrblx/t`.
- **Arquivos a criar:** `rokit.toml`, `wally.toml`, `default.project.json`, `.luaurc` (strict), `selene.toml`, `stylua.toml`, `src/{client,server,shared}/Core/{Bootstrap,Registry,Scheduler,DomainEventBus,RateLimiter,Logger}.luau`, `src/shared/Content/` (loader), `net/core.blink`, `lune/validate-content.luau`, `THIRD_PARTY.md`, `ASSETS_LEDGER.md`, `CLAUDE.md`.
- **Interfaces:** `Service`, `Controller`, `DomainEvent<T>`, `ContentRegistry`.
- **Spike obrigatório:** ativar `Workspace.AuthorityMode = Server` num place de teste e medir o efeito em StreamingEnabled, SignalBehavior Deferred, IAS nos PlayerScripts e CCL. **Decisão go/no-go do Server Authority.**
- **Testes:** ordem de `Init`/`Start` do Registry; o rate limiter bloqueia rajadas; o validador de conteúdo rejeita dados inválidos.
- **Riscos:** o Server Authority ainda muda rápido. Mitigação: o spike, e a lógica de combate isolada atrás de `Simulation` (substituível).

## Fase 2: Combat foundation

- **Repositórios:** TeamSwordphin/ShapecastHitbox (Wally `teamswordphin/shapecasthitbox`), Brawldude2/RagdollService (fixar commit com LICENSE MIT). Consultar o WCS só como design.
- **Arquivos:** `src/server/Combat/{CharacterStateService,CombatService,DamageService,TargetingService}.luau`, `src/shared/Combat/{States,ComboGraph,DamageTypes}.luau`, `src/shared/Adapters/{HitboxAdapter,RagdollAdapter}.luau`, `src/client/Combat/{CombatInput(IAS),HitFeedback}.luau`, `net/combat.blink`, `content/combos/*.luau`.
- **Adaptações:** mover o update do ShapecastHitbox para o Scheduler e o `BindToSimulation`; filtro de alvos (times, i-frames, um hit por golpe); ragdoll testado com ControllerManager.
- **Interfaces:** `IHitboxProvider`, `IDamageable`, `DamageRequest`/`DamageResult`, `CombatState` (enum em atributo).
- **Ordem do pipeline de dano:** i-frame → parry → block/guard (guard break) → armadura → dano → hitstun/stagger/knockback → eventos.
- **Testes:** FSM (transições válidas e inválidas), pipeline de dano (casos parry/block/guard-break), hitbox em playtest via MCP com 2 clientes e latência simulada.
- **Riscos:** conflito de loop e predição; performance com muitas hitboxes. Mitigação: loop central e profiling.

## Fase 3: Movement

- **Base:** CCL (oficial). **Opcional:** EgoMoose/rbx-wallstick (refazer a replicação).
- **Arquivos:** `src/shared/Movement/Abilities/{Dash,AirDash,Dodge,DoubleJump,WallRun,Flight,Knockback}.luau`, `src/server/Movement/MovementService.luau`, `IMovementAbility`.
- **Adaptações:** implementar as abilities de mobilidade com a mesma interface que a Custom Abilities API usa (`StartsWhen/RunsWhile/Blocks/Stops`), para migrar quando a API sair do beta.
- **Testes:** dash com i-frames × hitbox; bloqueios (sem dash em hitstun); voo com streaming; mobile/console via IAS.
- **Riscos:** beta da CCL e incompatibilidades listadas pela Roblox (Tools/Inventory/Health). Mitigação: não usar Tools nativos.

## Fase 4: Abilities, status e transformações

- **Repositórios:** nenhum importado (design do WCS como referência). FastCast2 para projéteis (`weenachuangkud/fastcast2`, só o código MIT).
- **Arquivos:** `src/shared/Abilities/{AbilityRuntime,Timeline,Targeting}.luau`, `src/shared/Status/StatusRuntime.luau`, `src/shared/Forms/FormRuntime.luau`, `src/shared/Adapters/ProjectileAdapter.luau`, `content/{abilities,status,forms}/*.luau`, `net/abilities.blink`.
- **Interfaces:** `AbilityDefinition`, `StatusDefinition`, `FormDefinition` (ver [habilidades](catalog/abilities-status-effects/README.md) e [transformações](catalog/transformations/README.md)).
- **Testes:** custos, cooldown autoritativo, stacking de status, forma com drenagem de energia e estágios, e 100+ definições carregadas sem erro (validador).
- **Riscos:** explosão de casos especiais. Mitigação: timeline declarativa com hooks pequenos e opcionais.

## Fase 5: NPC / IA

- **Repositórios:** grayzcale/simplepath (release fixada, auditada). **Avaliar** Ukendio/jecs com benchmark (100/300/600 NPCs).
- **Arquivos:** `src/server/Npc/{NpcRuntime,Perception,Brain,Lod,BossPhases}.luau`, `src/shared/Adapters/PathAdapter.luau`, `content/npcs/*.luau`.
- **Adaptações:** os NPCs usam o **mesmo** AbilityRuntime e DamageService; tick escalonado; percepção via octree ou spatial hash; Actors para percepção em lote.
- **Testes:** patrulha, aggro e chase; decisão de ataque; boss com fases; benchmark de CPU e memória no servidor.
- **Riscos:** o suporte da CCL a NPCs ainda é "coming soon". Mitigação: PathAdapter e controle via Humanoid até lá.

## Fase 6: Quest

- **Repositório:** prooheckcp/RoQuest, **só depois** de esclarecer a licença (LICENSE Apache-2.0 × README MIT). Senão, QuestEngine próprio com o mesmo modelo.
- **Arquivos:** `src/server/Quests/{QuestService,QuestAdapter}.luau`, `content/quests/*.luau`, `net/quests.blink`, UI de quest (Vide).
- **Adaptações:** trocar o Red vendorizado pela rede Blink; objetivos ligados ao `DomainEventBus`; recompensas só via `RewardService`; quests ocultas e requisitos de nível e diálogo via disponibilidade condicionada.
- **Testes:** cadeia de quests, daily/weekly (reset UTC), cliente sem poder de alterar progresso, persistência do progresso.
- **Riscos:** beta sem commits há mais de 12 meses. Mitigação: adapter fino; plano B pronto.

## Fase 7: Inventory

- **Repositórios:** nenhum importado (Stoway só como referência de padrões).
- **Arquivos:** `src/server/Inventory/{InventoryService,ItemDatabase,LootService,TradeService}.luau`, `content/items/*.luau`, `content/loot/*.luau`, `net/inventory.blink`, UI (Vide).
- **Interfaces:** `ItemDefinition`, `ItemInstance`, operações idempotentes com `opId`.
- **Testes:** stack/split/swap/equip, tentativa de duplicação (retry, desconexão no meio), trade atômico, loot com seed auditável.
- **Riscos:** dupe. Mitigação: operações idempotentes; trade via escrow ou Lyra `txAsync` (após testes de carga).

## Fase 8: World

- **Repositórios:** nenhum importado (Gzeu procedural só como referência). Assets CC0 (Poly Haven, ambientCG, Kenney, Quaternius) registrados no `ASSETS_LEDGER.md`.
- **Arquivos:** `src/server/World/{RegionService,RealmTeleportService}.luau`, `content/regions/*.luau`; places por reino no universo (Mantle opcional para IaC).
- **Testes:** transição entre reinos (estado salvo antes e revalidado no destino), aviso de perigo, streaming em mobile.
- **Riscos:** memória e streaming. Mitigação: `ModelStreamingMode` por modelo e orçamento de instâncias por região.

## Fase 9: Persistence (endurecimento)

> O `DataService` **mínimo** nasce na Fase 1 ou 2 (os jogadores precisam de perfil desde cedo). Esta fase endurece a persistência para produção.

- **Repositório:** anthony0br/DocumentService (Wally `anthony0br/documentservice`, versão fixa). Alternativa: `lm-loleris/profilestore` (**este** é o escopo oficial; existem 24 escopos homônimos).
- **Arquivos:** `src/server/Data/{DataService,Schema,Migrations/*}.luau`, testes com DataStore mock.
- **Testes:** migração vN→vN+1 com dados reais anonimizados; session lock com dois servidores; BindToClose; rollback via Cmdr (permissão restrita).
- **Riscos:** perda de dados. Mitigação: backups e versões do DataStore, alertas em `ProfileStore.OnError` ou nos Result de erro, feature flags.

## Fase 10: Optimization

- **Ferramentas:** MicroProfiler, Script Profiler, visualizador do Server Authority (`Ctrl+Shift+F6`), playtests automatizados via MCP com N bots.
- **Candidatos a adotar se o profiling pedir:** jecs (+ planck), Parallel Luau em percepção e projéteis, ObjectCache em todo VFX e projétil.
- **Testes:** orçamento por frame (servidor e cliente), memória por região, largura de banda por jogador (Blink batching), qualidade de VFX por dispositivo.
- **Riscos:** otimização prematura. Mitigação: só otimizar o que o profiler aponta.

---

## Resumo de dependências por fase

| Fase | Wally / ferramentas adicionadas |
| --- | --- |
| 1 | rojo, rokit, wally, selene, stylua, luau-lsp, lune, jest-lua, wally-package-types, blink, asphalt; `sleitnick/{signal,trove,table-util,timer}`, `osyrisrblx/t` |
| 2 | `teamswordphin/shapecasthitbox`, RagdollService (commit fixo) |
| 3 | — (CCL oficial); opcional wallstick |
| 4 | FastCast2 (código MIT, versão fixa) |
| 5 | SimplePath (release fixa); opcional `ukendio/jecs` |
| 6 | RoQuest (se a licença for confirmada) |
| 7 | — |
| 8 | — (assets CC0 no ledger) |
| 9 | `anthony0br/documentservice` (ou `lm-loleris/profilestore`) |
| 10 | opcional jecs/planck |
| Transversal | `littensy/charm` + `littensy/charm-sync`, `centau/vide` (+ `littensy/vide-charm`), `pyseph/objectcache`, `wrello/animations` (adaptado), `sirmallard/iris` (dev), flipbook (plugin de dev); **spr** e **RbxCameraShaker** não têm `wally.toml` nos repos oficiais: vendorizar o fonte com o LICENSE (evitar re-uploads de terceiros); **Cmdr**: escopo Wally não verificado nesta pesquisa |

> Os nomes de escopo Wally acima foram vistos nos manifestos dos repositórios ou na busca do registro em 2026-09-29. **Confirmar cada escopo** no momento da instalação (checklist §C).
