# Mapa de integração (brief §25 e §26): como evitar a "colcha de retalhos"

## Princípios

1. **Um dono por estado.** Estado de personagem: `CharacterStateService`. Dados persistidos: `DataService`. Recompensas: `RewardService`. Rolls: `RngService`. Ninguém mais escreve nesses estados.
2. **Uma fronteira de rede.** Só o módulo gerado pelo Blink (`Net`) toca remotes. A simulação autoritativa usa o Server Authority nativo, não remotes.
3. **Toda lib externa atrás de um adapter** com interface do projeto. Trocar a lib muda um arquivo, não o jogo.
4. **Eventos de domínio** (`DomainEventBus`) conectam sistemas sem acoplamento direto. Exemplos: `EnemyKilled`, `DamageDealt`, `ItemAcquired`, `RegionEntered`, `NpcTalkedTo`, `FormActivated`.
5. **Conteúdo como dados** (`content/`), validado por Lune + `t` no CI: raças, bloodlines, genes, mutações, habilidades, status, formas, itens, loot, quests, NPCs, regiões.

## Diagrama

```text
                                   GENESIS REALMS
                                         │
┌────────────────────────────────── PLATAFORMA ROBLOX ─────────────────────────────────────┐
│ Server Authority (BindToSimulation, rollback) · IAS · CCL (ControllerManager/Abilities)   │
│ StreamingEnabled · PathfindingService · DataStore · TeleportService · Parallel Luau      │
└────────────────────────────────────────┬─────────────────────────────────────────────────┘
                                         │
┌──────────────────────────────────── CORE (próprio) ──────────────────────────────────────┐
│ Bootstrap/Registry · Scheduler (budget) · DomainEventBus · Net[Blink] · RateLimiter      │
│ Content DB (dados validados) · RngService · Logger/Telemetria · RbxUtil(Signal/Trove) · t │
└───────┬───────────────────────────────┬──────────────────────────────────┬───────────────┘
        │                               │                                  │
  ┌─────┴──────── COMBATE ────────┐ ┌───┴──────── MOVIMENTO ─────────┐ ┌───┴──── HABILIDADES ──────┐
  │ CharacterStateService (FSM)   │ │ MovementService                │ │ AbilityRuntime (timeline) │
  │ CombatService (combos, block, │ │  base: CCL                     │ │ StatusRuntime (buff/debuff│
  │  parry, dodge, hitstun)       │ │  abilities próprias: dash,     │ │ FormRuntime (transforma-  │
  │ DamageService (pipeline único)│ │  air dash, double jump,        │ │  ções = status "Form")    │
  │ TargetingService (lock-on)    │ │  wall run, voo, knockback      │ │ custos/cooldowns no       │
  │ ─ adapters ─                  │ │ ─ adapter opcional ─           │ │  servidor                 │
  │ HitboxAdapter → ShapecastHitbox│ │ WallstickAdapter → wallstick  │ │                           │
  │ ProjectileAdapter → FastCast2 │ └────────────────────────────────┘ └───────────────────────────┘
  │ RagdollAdapter → RagdollService│
  │ RewindAdapter → RollbackHitbox│            (todos rodam em BindToSimulation;
  └───────────────────────────────┘             estado predito em atributos)
                                         │
┌──────────────────────────────── SISTEMAS COMPARTILHADOS ─────────────────────────────────┐
│ QuestService ─ adapter → RoQuest (ou QuestEngine próprio)                                 │
│ InventoryService · ItemDatabase · LootService · Shop/Trade (escrow ou Lyra tx)           │
│ NpcRuntime (Perception · Brain FSM+utility · PathAdapter → SimplePath · usa AbilityRuntime)│
│ GeneticsService · AppearanceService (HumanoidDescription) · RewardService · RegionService │
└────────────────────────────────────────┬─────────────────────────────────────────────────┘
                                         │
┌──────────────────────────────────── PERSISTÊNCIA ────────────────────────────────────────┐
│ DataService (único importador) ─ adapter → DocumentService · migrações versionadas · t   │
└──────────────────────────────────────────────────────────────────────────────────────────┘

CLIENTE: InputController (IAS) · CameraDirector (spr + CameraShaker) · AnimationController
         (Animator + wrello/Animations adaptado) · VfxPlayer (ObjectCache) · UI (Vide + Charm/charm-sync)
```

## Análise §25 por componente externo adotado

| Componente | 1. Comunica com | 2. Dependências | 3. APIs que expõe | 4. Assume que existe | 5. Conflitos possíveis | 6. Adaptação estimada | 7. Usar só partes? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ShapecastHitbox** | HitboxAdapter → CombatService | nenhuma | objeto hitbox (`HitStart/HitStop/OnHit/SetResolution/...`) | Attachments/tags `DmgPoint` no rig ou arma | loop `PostSimulation` próprio vs. `BindToSimulation` | 2–3 arquivos (scheduler + adapter) | Sim: `Solvers/` + `Types` |
| **FastCast2** | ProjectileAdapter → DamageService; cliente renderiza | nenhuma declarada no Wally | `RaycastFire/BlockcastFire/SpherecastFire`, behaviors | Actors para VMs paralelas | eventos de hit próprios vs. pipeline de dano | adapter + config de VMs | Sim: simulação; ignorar arte (NC-ND) |
| **RagdollService** | RagdollAdapter ← CharacterStateService | nenhuma | `Ragdoll/Unragdoll/IsRagdolled/SetupRagdoll` | Humanoid, R6/R15 | interação com CCL/ControllerManager e rollback | 1 adapter + testes | Sim |
| **RollbackHitbox** | RewindAdapter ← AbilityRuntime (ranged) | nenhuma | `RegisterCharacter/RecordAll/ValidateHit` | loop de gravação ~60 Hz | redundante em parte com o Server Authority | 1 adapter | Sim (só ranged) |
| **CCL** | MovementService | plataforma | ControllerManager, AvatarAbilities, Custom Abilities (beta) | IAS, Server Authority | beta: Tools/Inventory/Health; NPCs "coming soon" | interface `IMovementAbility` | Sim: base de locomoção |
| **Blink** | todos os serviços via `Net` | compilador na toolchain | funções geradas por evento | contratos `.blink` | nenhum (única rede) | 0 (codegen) | — |
| **Charm + charm-sync + Vide** | UI ← estado replicado | nenhuma externa | atoms, `effect`, componentes | servidor publica patches | nenhum se for a única pilha de estado | wiring inicial | — |
| **DocumentService** | DataService (único) | nenhuma | `DocumentStore`, `Document` com Result | schema e migrações definidos | nenhum | DataService (~1 módulo) | — |
| **SimplePath** | PathAdapter ← NpcRuntime | PathfindingService | `Path.new`, `:Run(target)`, `:Stop()`, `:Destroy()`, eventos `Reached/WaypointReached/Blocked/Error` | Humanoid ou modelo | movimentação CCL de NPC (futuro) | 1 adapter | — |
| **RoQuest** | QuestAdapter ↔ DomainEventBus/DataService/RewardService | Red, Promise, Signal, Trove vendorizados | API de servidor (`GiveQuest`, `AddObjective`…) | persistência externa via Get/SetPlayerData | **Red** (segunda rede) | trocar a rede do Client/Server (~3–5 arquivos) | Sim: `Shared/` + `Server/` |
| **wrello/Animations** | AnimationController | nenhuma declarada | preload/play por rig | cache de tracks | **cache de AnimationTrack** vs. rollback | ajuste do cache | Sim |
| **ObjectCache** | VfxPlayer, ProjectileAdapter | nenhuma | cache de Parts/Models | — | nenhum | 0 | — |
| **spr / RbxCameraShaker** | CameraDirector, UI | nenhuma | springs / shake | — | nenhum | 0 | — |
| **Cmdr** | Admin | — | comandos, hooks `BeforeRun` | grupos/permissões | nenhum | permissões | — |

## Reutilizar × adaptar × construir

| Construir do zero | Adaptar | Reutilizar como está |
| --- | --- | --- |
| Bootstrap, Scheduler, DomainEventBus, RateLimiter, RngService | ShapecastHitbox (loop) | Rojo, Wally, Selene, StyLua, luau-lsp, Lune, Jest-Lua, Rokit, Asphalt |
| CharacterStateService (FSM de combate), CombatService (combos, block, parry, dodge, hitstun, knockback), DamageService | FastCast2 (adapter de dano) | Blink, t |
| AbilityRuntime, StatusRuntime, FormRuntime (transformações) | RagdollService, RollbackHitbox | RbxUtil (Signal/Trove/TableUtil/Timer) |
| MovementAbilities (dash, air dash, double jump, wall run, voo) | CCL (beta de custom abilities) | Charm + charm-sync, Vide, Iris, flipbook |
| TargetingService + LockOn, CameraDirector | wrello/Animations (cache) | DocumentService (via DataService) |
| NpcRuntime (percepção, brain, LOD, boss) | RoQuest (rede + licença) | SimplePath, ObjectCache, spr, RbxCameraShaker, Cmdr |
| InventoryService, ItemDatabase, LootService, Trade | forge-vfx (se aprovado juridicamente) | APIs oficiais (Pathfinding, HumanoidDescription, Teleport, Streaming) |
| GeneticsService, AppearanceService, criação de personagem | wallstick (opcional) | |
| RegionService, reinos, mundo e assets próprios | | |
| VfxService/VfxPlayer, AnimationCatalog, UI do jogo | | |
