# Log de buscas e origem dos candidatos

Período: 2026-09-29 → 2026-09-30.

## Buscas web (§20 do brief + complementares)

| # | Consulta | Principais pistas úteis |
| --- | --- | --- |
| 1 | `Roblox combat framework Luau github hitbox` | ShapecastHitbox, ClientCast, JoshuaIO fighting framework, gist-semente |
| 2 | `Roblox melee combat framework github luau open source M1 combo block parry` | AMS, WCS, galenamc/Roblox-CombatSystem, aziz8235 (vazio) |
| 3 | `Roblox anime battlegrounds combat system open source github` | dwmk/RobloxGames, Anime Movement System (DevForum), posts de combate simples |
| 4 | `Roblox lock on system github luau target camera` | repositórios de "camlock" (scripts de exploit, descartados), CameraService |
| 5 | `Roblox movement framework github dash wallrun slide luau` | Slubbie, carlos123344222, lewuat DashPlace, Roblox/dash (homônimo) |
| 6 | `Roblox ability framework skill system luau github cooldown` | Vainalykas skill system, repositórios de "skills" para IA (fora de escopo) |
| 7 | `Roblox NPC AI framework behavior tree github luau` | behaviortree.rbxlua (howmanysmall/seyaidev), KURVOX (vazio) |
| 8 | `WCS combat system roblox github luau skills status effects framework` | WCS (docs + DevForum) |
| 9 | `Chickynoid server authoritative character controller roblox github license` | easy-games/chickynoid |
| 10 | `Roblox quest system open source github luau RoQuest` | RoQuest |
| 11 | `Roblox inventory system open source github luau equipment hotbar Satchel` | Stoway, Satchel, inventory-logic-NoGoodUi (proprietário) |
| 12 | `Roblox character creator customization system open source github HumanoidDescription` | docs oficiais, Character-Realism, Sugar |
| 13 | `Roblox procedural terrain generation github luau open world chunk` | Gzeu/roblox-procedural-worlds, RTerrainGenerator |
| 14 | `"gameplay ability system" roblox luau github` | nada maduro |
| 15 | `devforum roblox "Character Controller Library" full release` | CCL (oficial) + beta de Custom Abilities |
| 16 | `Roblox "Server Authority" beta client prediction rollback 2026` | docs e newsroom oficiais |
| 17 | `Roblox Input Action System ... release devforum` | IAS full release |
| 18 | `create.roblox.com docs server authority lag compensation combat` | Rewind (arquivado), RollbackHitbox |
| 19 | `FastCast github EtiTheSpirit ...` | FastCast2 (+ forks), FastCastAPIDocs |
| 20 | `PartCache github Xan roblox module repository` | PartCache (DevForum), ObjectCache |
| 21 | `Prvd 'M Wrong roblox framework github providers` | prvdmwrong, Sleitnick/Axis, listas awesome-roblox |
| 22 | `EzLockOn ...` | EzLockOn (DevForum/Creator Store) |
| 23 | `Suphi DataStore Module devforum session locking license` | Suphi's DataStore Module |
| 24 | `MuchachoHitbox github roblox` | CatSushi/MuchachoHitbox, MaxHitbox |
| 25 | `devforum roblox status effect system open source Effectify license github` | Effectify, StatusEffectManager, statusify |
| 26 | `VFX Forge emit module roblox github license` | zilibobi/forge-vfx |
| 27 | `Refx roblox VFX replication library github` | wad4444/refx |
| 28 | `Roblox official templates open source github ... license` | templates oficiais (Laser Tag, Platformer) |
| 29 | `Suphi Packet networking module devforum buffer` | Packet + mirror de terceiro |
| 30 | `NoobPath pathfinding roblox github license` | NoobPath, PathForge, RoPath |
| 31 | `Roblox Terms of Use Creator Store assets license ...` | Creator Store Terms, IP licensing |
| 32 | `Roblox "Distributed Content" license ...` | Limited Use License, Audio Upload License |
| 33 | `Mixamo license FAQ ...` | FAQ Adobe |
| 34 | `Quaternius Universal Animation Library CC0 license` | Quaternius |
| 35 | `Roblox audio library licensed music APM ...` | Licensed Music (APM) |
| 36 | `Kenney assets license CC0` / `Poly Haven ... ambientCG CC0` / `Sonniss GDC ... license` / uncopylocked | fontes de assets |
| 37 | `Roblox Studio built-in MCP server Claude Code` | MCP embutido no Studio (mar/2026) |

## Registro Wally (`api.wally.run/v1/package-search`)

36 consultas: combat, hitbox, ability, skill, status effect, cooldown, lockon, lock on, dash, movement, ragdoll, knockback, parry, quest, inventory, item, loot, npc, pathfinding, behavior tree, behaviortree, state machine, statemachine, fsm, camera, camera shake, spring, vfx, particle, animation, animator, pool, cache, octree, zone, streaming.

- **653 pacotes únicos** retornados.
- Observação principal: grande parte são **re-uploads e forks de terceiros** de pacotes populares (24 escopos distintos com um pacote chamado `profilestore`; vários de RaycastHitbox, PartCache, RbxCameraShaker, Spring). Isso reforça a regra de fixar o escopo do autor original.
- Pacotes com escopo oficial usados no catálogo: `teamswordphin/shapecasthitbox`, `cheetiedotpy/wcs` (escopo do WCS), `prooheckcp/roquest`, `prooheckcp/robloxstatemachine`, `wrello/animations`, `sleitnick/*`, `paradoxum-games/lyra`, `anthony0br/documentservice`.
- Pistas vistas **só no Wally** e não verificadas a fundo (fora do catálogo principal, candidatas a uma segunda rodada): `axp3cter/arbor` (behavior trees tipadas), `thunn/behavior-tree`, `metricrb/skilltree`, `ppeter2/npc-engine`, `nsawill1405/hitbox-plus`, `vbaumel1337/central` (hitbox server-authoritative com compensação de latência), `nontkph/arclightinput`, `skatingii/perfect-sequencer`, `pepeeltoro41/dataforge`, `xoifaii/ledger`, `kashtheking/stagger`.

## Listas curadas

- [awesome-roblox/awesome-roblox](https://github.com/awesome-roblox/awesome-roblox): tooling, DataStore, ECS, networking, UI e admin.
- [loominatrx/useful-roblox-resources](https://github.com/loominatrx/useful-roblox-resources) (Unlicense).
- [Coyenn/awesome-roblox-ts](https://github.com/Coyenn/awesome-roblox-ts) (TypeScript).

## Gist-semente

[Roblox Combat & Movement Systems — Complete Catalog (150+ entries)](https://gist.github.com/pivatol1995-star/fce8245f1828fca3ffe03a1c301a5d19): usado **só como fonte de pistas**. Várias licenças ali estavam desatualizadas ou incorretas. Exemplos: RollbackHitbox era "sem licença" e passou a MIT; RagdollService aparecia como LGPL, mas hoje o arquivo é MIT. Seções do gist descartadas por escopo ou licença: sistemas pagos (BuiltByBit, Payhip), matchmaking, PvP rating, holstering, damage indicators, "uncopylocked games" (sem licença de código).

## Verificação de metadados

- 197 lookups (150 repositórios únicos) na API do [ecosyste.ms](https://repos.ecosyste.ms) (`/api/v1/hosts/GitHub/repositories/<owner>%2F<repo>`).
- 49 clones completos sem blobs (`git clone --filter=blob:none`) + 37 clones rasos (`--depth 1`; 1 deles só de árvore, sem checkout: Nevermore) para confirmar LICENSE e o último commit.
- Posts do DevForum lidos: WCS, EzLockOn, Suphi's DataStore, BehaviorTrees3, Rewind, RollbackHitbox, HitboxClass v2, Effectify, StatusEffectManager, Anime Movement System, Packet, PartCache, NoobPath, CCL (full release e beta de Custom Abilities), MCP embutido.
