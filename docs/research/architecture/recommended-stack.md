# Seção G — Arquitetura final recomendada (stack concreta)

> Cada escolha tem justificativa técnica e evidência. Nada foi escolhido só por popularidade. Regra: **um componente por responsabilidade** e **toda biblioteca externa atrás de um adapter próprio**.

## Stack

```text
PLATAFORMA (oficial Roblox)
  Server Authority (Workspace.AuthorityMode = Server) · Input Action System · Character Controller Library
  StreamingEnabled · PathfindingService · DataStoreService · TeleportService (reinos = places) · Parallel Luau

TOOLING
  Rokit · Rojo · Wally (+ wally-package-types) · Selene · StyLua · luau-lsp · Lune · Jest-Lua · Blink (codegen)
  Asphalt (assets) · [opcional] Mantle (deploy) · Moonwave (docs) · MCP embutido do Studio (Claude Code)

CORE (próprio + utilitários)
  Bootstrap/ServiceRegistry próprio · Scheduler central próprio · DomainEventBus próprio · Content DB (dados) próprio
  RbxUtil: Signal, Trove, TableUtil, Timer · t (validação) · RateLimiter próprio · RngService próprio

REDE             → Blink (IDL → Luau tipado, buffers) para eventos discretos; Server Authority para simulação
ESTADO / UI      → Charm + charm-sync (replicação) · Vide (+ vide-charm) · Iris (debug, só dev) · flipbook (storybook)
DADOS            → DocumentService atrás de DataService próprio  [alternativa: ProfileStore]  [avaliação p/ trading: Lyra txAsync]
COMBATE          → CharacterStateService + CombatService + DamageService (próprios)
                   Hitbox → ShapecastHitbox (solvers, adaptado ao loop central / BindToSimulation)
                   Projéteis → FastCast2 (adaptado; dano no servidor)
                   Ragdoll → RagdollService (adaptado)
                   Lag comp. à distância → RollbackHitbox (opcional, adaptado)
                   Lock-on/targeting → TargetingService + LockOnMode (próprios)
HABILIDADES      → AbilityRuntime + StatusRuntime + FormRuntime (próprios; design inspirado no WCS)
MOVIMENTO        → CCL (base) + MovementAbilities próprias (dash, air dash, dodge, double jump, wall run, voo)
                   [opcional] rbx-wallstick para andar em paredes
CÂMERA           → CameraDirector próprio + spr + RbxCameraShaker
ANIMAÇÃO         → Animator oficial + wrello/Animations (adaptado) + AnimationCatalog próprio
VFX              → VfxService/VfxPlayer próprios + ObjectCache  [forge-vfx só após revisão jurídica]
NPC / IA         → NpcRuntime próprio (FSM + utility) + SimplePath + PathfindingService  [jecs após benchmark]
QUESTS           → RoQuest adaptado (licença a confirmar) OU QuestEngine próprio (mesmo modelo de dados)
INVENTÁRIO       → ItemDatabase + InventoryService + LootService próprios (padrões do Stoway, sem o código dele)
PERSONAGEM       → GeneticsService + AppearanceService próprios sobre HumanoidDescription
MUNDO            → RegionService próprio + places por reino + terreno/kits próprios (assets CC0/Roblox)
ADMIN            → Cmdr (permissões no servidor)
```

## Justificativas

| Escolha | Por quê (evidência) | Alternativas e motivo da rejeição |
| --- | --- | --- |
| **Server Authority + IAS + CCL** | Resolvem na engine a predição e o rollback de movimento e combate, e o input cross-platform (PC, mobile, console). A documentação indica `BindToSimulation` para a lógica e atributos para estado predito. Server Authority anunciado em 2026-07-09; IAS full release em 2026-06; CCL full release em 2026-04-08. | Chickynoid (último commit 2024-01, substitui o Humanoid), Rewind (sem licença): reimplementam o que agora é nativo. |
| **Rojo/Wally/Selene/StyLua/luau-lsp/Lune/Rokit** | Pedidos no brief §19. Todos ativos em 2026, com licença MIT ou MPL. São ferramentas e não entram no runtime. | Argon, Lync, pesde, Foreman: evitar misturar ferramentas. |
| **Bootstrap próprio** | Knit arquivado; Prvd 'M Wrong desaconselhado pelo autor; Flamework exige TS; Nevermore traz lock-in. Um bootstrap tem ~150–300 linhas. | — |
| **Blink** | IDL com validação gerada, buffers; o mais ativo da categoria (42 commits em 12 meses, 16 autores, 91 tags); strict no projeto. | Zap (equivalente, menos ativo), ByteNet (0 commits em 12m), Packet (só Creator Store; vulnerabilidades relatadas). |
| **Charm + charm-sync + Vide** | O mesmo autor mantém o binding `vide-charm`. Vide é o framework de UI mais ativo (commit 2026-09-28, 25 autores) e strict no projeto. O Charm tem 30 arquivos de teste. | Fusion (maduro, mas 5 commits em 12m), react-lua (pesado, push 2025-05), Roact (arquivado). |
| **DocumentService** | Único que junta migrações, validação, Result types, retries, session lock opcional e testes, sem dependências e ativo (2026-09). Atende o §11. | ProfileStore (sem migrações/validação; fica como alternativa); Lyra (autor desaconselha para dados críticos); Lapis (sem commits em 12m). |
| **ShapecastHitbox** | Sucessor do RaycastHitboxV4, sem dependências, 10/14 arquivos `--!strict`, solvers por raycast, blockcast, spherecast, attachment e bone. | ClientCast (confia no cliente), MuchachoHitbox (só `.rbxm`), HitboxClass (sem licença). |
| **FastCast2** | Código MIT, Parallel Luau, raycast/blockcast/spherecast, muito ativo. | Secure-Cast (arquivado), FastCast original (sem manutenção). |
| **Runtime próprio de habilidades, status e formas** | Nenhum runtime Luau licenciado é compatível com Server Authority. O WCS é TS/Flamework, com rede paralela e 1 commit em 12m. Habilidades, formas e genética são o **núcleo da identidade** do jogo. | Adotar WCS = duas pilhas de rede e estado (a "colcha de retalhos" do §25). |
| **SimplePath** | MIT, 176 commits, 10 autores, pequeno (~450 linhas), ativo (2026-06). | BehaviorTree3 (GPL), NoobPath/PathForge (sem licença). |
| **RoQuest (condicional)** | O único sistema de quests sério: fronteira de confiança correta (cliente só lê), persistência plugável, `Daily`/`Weekly`/`Custom`, `RequiredQuests`. | Construir o próprio caso a licença (Apache vs MIT) não se resolva. |
| **ObjectCache, spr, RbxCameraShaker** | Pequenos, MIT, auditados, sem dependências. | PartCache (sem licença). |
| **Cmdr** | Console extensível com hooks de permissão; ativo (push 2026-08). | Adonis (grande superfície; fora de escopo). |

## O que **não** entra no jogo (decisão explícita)

WCS, Chickynoid, Knit, Nevermore (como framework), BehaviorTree3 (GPL), Stoway (código), qualquer item sem licença, Free Models não auditados, arte do FastCast2 (NC-ND), Cube3D (research-only).
