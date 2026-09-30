# Seção B — Master Table

> Gerada automaticamente a partir de [`data/catalog.csv`](data/catalog.csv) (fonte única de verdade). Dados coletados em **2026-09-29**. Nenhum valor foi estimado: o que não foi verificado aparece como **NÃO VERIFICADO**.

**Como ler as colunas**

- **Stars**: valor ao vivo via ungh.cc (proxy da API do GitHub) em 2026-09-30. É só um indicador de popularidade, **não de qualidade**.
- **Atividade**: data do último commit na branch padrão (via `git clone`). Quando não houve clone, é o último push segundo o ecosyste.ms.
- **Qualidade**: fatos objetivos do clone (nº de commits e de autores, arquivos `--!strict` sobre o total de arquivos Luau, arquivos de teste). A leitura qualitativa de cada projeto está nas fichas de `catalog/`.
- **Integração**: se o projeto tem manifesto Wally e/ou projeto Rojo.
- **Recomendação**: segue os critérios de [`00-methodology/evaluation-criteria.md`](00-methodology/evaluation-criteria.md).

**Totais (168 candidatos):** DO NOT USE: 35 · READY TO INTEGRATE: 34 · REQUIRES ADAPTATION: 16 · USE AS REFERENCE ONLY: 83


## Tooling

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| ai | Roblox Studio built-in MCP server | [link](https://devforum.roblox.com/t/assistant-updates-studio-built-in-mcp-server-and-playtest-automation/4474643) | Roblox Terms | n/a | oficial/DevForum | — | API da plataforma | ✅ READY TO INTEGRATE |
| ai | Roblox/studio-rust-mcp-server | [link](https://github.com/Roblox/studio-rust-mcp-server) | MIT | 493 | 2026-04-03 · ARQUIVADO | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| assets | jackTabsCode/asphalt | [link](https://github.com/jackTabsCode/asphalt) | MIT | 161 | 2026-07-28 | NÃO VERIFICADO | NÃO VERIFICADO | ✅ READY TO INTEGRATE |
| assets | rojo-rbx/tarmac | [link](https://github.com/rojo-rbx/tarmac) | MIT | 35 | 2024-03-05 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| deploy | blake-mealey/mantle | [link](https://github.com/blake-mealey/mantle) | MIT | 116 | 2026-05-28 | NÃO VERIFICADO | NÃO VERIFICADO | 🛠️ REQUIRES ADAPTATION |
| docs | evaera/moonwave | [link](https://github.com/evaera/moonwave) | MPL-2.0 | 246 | 2026-06-02 | NÃO VERIFICADO | NÃO VERIFICADO | ✅ READY TO INTEGRATE |
| docs | Roblox/creator-docs | [link](https://github.com/Roblox/creator-docs) | CC-BY-4.0 | 844 | 2026-09-25 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| dom | rojo-rbx/rbx-dom | [link](https://github.com/rojo-rbx/rbx-dom) | MIT | 198 | 2026-07-29 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| format | JohnnyMorganz/StyLua | [link](https://github.com/JohnnyMorganz/StyLua) | MPL-2.0 | 2300 | 2026-09-13 | NÃO VERIFICADO | NÃO VERIFICADO | ✅ READY TO INTEGRATE |
| language | luau-lang/luau | [link](https://github.com/luau-lang/luau) | MIT | 5918 | 2026-09-25 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| lint | Kampfkarren/selene | [link](https://github.com/Kampfkarren/selene) | MPL-2.0 | 824 | 2026-05-21 | NÃO VERIFICADO | NÃO VERIFICADO | ✅ READY TO INTEGRATE |
| lsp | JohnnyMorganz/luau-lsp | [link](https://github.com/JohnnyMorganz/luau-lsp) | MIT | 542 | 2026-09-27 | NÃO VERIFICADO | NÃO VERIFICADO | ✅ READY TO INTEGRATE |
| opencloud | Sleitnick/rbxcloud | [link](https://github.com/Sleitnick/rbxcloud) | MIT | 140 | 2025-03-23 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| packages | pesde-pkg/pesde | [link](https://github.com/pesde-pkg/pesde) | MIT | 129 | 2026-09-23 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| packages | UpliftGames/wally | [link](https://github.com/UpliftGames/wally) | MPL-2.0 | 498 | 2026-09-26 | NÃO VERIFICADO | NÃO VERIFICADO | ✅ READY TO INTEGRATE |
| runtime | lune-org/lune | [link](https://github.com/lune-org/lune) | MPL-2.0 | 955 | 2026-07-03 | NÃO VERIFICADO | NÃO VERIFICADO | ✅ READY TO INTEGRATE |
| sync | argon-rbx/argon | [link](https://github.com/argon-rbx/argon) | Apache-2.0 | 148 | 2026-07-01 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| sync | Iron-Stag-Games/Lync | [link](https://github.com/Iron-Stag-Games/Lync) | LGPL-2.1 | 38 | 2026-09-24 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| sync | rojo-rbx/rojo | [link](https://github.com/rojo-rbx/rojo) | MPL-2.0 | 1758 | 2026-07-06 | NÃO VERIFICADO | NÃO VERIFICADO | ✅ READY TO INTEGRATE |
| test | jsdotlua/jest-lua | [link](https://github.com/jsdotlua/jest-lua) | MIT | 59 | 2024-12-23 | NÃO VERIFICADO | NÃO VERIFICADO | ✅ READY TO INTEGRATE |
| test | Roblox/testez | [link](https://github.com/Roblox/testez) | Apache-2.0 | 209 | 2024-03-05 · ARQUIVADO | NÃO VERIFICADO | NÃO VERIFICADO | ⛔ DO NOT USE |
| toolchain | Roblox/foreman | [link](https://github.com/Roblox/foreman) | MIT | 262 | 2026-05-01 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| toolchain | rojo-rbx/rokit | [link](https://github.com/rojo-rbx/rokit) | MIT | 465 | 2026-05-09 | NÃO VERIFICADO | NÃO VERIFICADO | ✅ READY TO INTEGRATE |
| transform | seaofvoices/darklua | [link](https://github.com/seaofvoices/darklua) | MIT | 242 | 2026-07-13 | NÃO VERIFICADO | NÃO VERIFICADO | ✅ READY TO INTEGRATE |
| ts | roblox-ts/roblox-ts | [link](https://github.com/roblox-ts/roblox-ts) | MIT | 1308 | 2026-09-22 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| types | JohnnyMorganz/wally-package-types | [link](https://github.com/JohnnyMorganz/wally-package-types) | MIT | 122 | 2026-07-05 | NÃO VERIFICADO | NÃO VERIFICADO | ✅ READY TO INTEGRATE |

## Core / frameworks

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| admin | alicesaidhi/conch | [link](https://github.com/alicesaidhi/conch) | MIT | 122 | 2026-08-15 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| admin | Epix-Incorporated/Adonis | [link](https://github.com/Epix-Incorporated/Adonis) | MIT | 504 | 2026-09-27 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| admin | evaera/Cmdr | [link](https://github.com/evaera/Cmdr) | MIT | 528 | 2026-09-29 | 666 commits/63 autores; strict 0/86; testes 0 | Wally+Rojo | ✅ READY TO INTEGRATE |
| async | evaera/roblox-lua-promise | [link](https://github.com/evaera/roblox-lua-promise) | MIT | 352 | 2023-10-15 | 211 commits/15 autores; strict 0/3; testes 1 | Wally+Rojo | ✅ READY TO INTEGRATE |
| cleanup | howmanysmall/Janitor | [link](https://github.com/howmanysmall/Janitor) | MIT | 149 | 2025-10-18 | 191 commits/10 autores; strict (projeto, .luaurc); testes 1 | Wally+Rojo | 📖 USE AS REFERENCE ONLY |
| ecs | centau/ecr | [link](https://github.com/centau/ecr) | MIT | 59 | 2026-06-03 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| ecs | evaera/matter | [link](https://github.com/evaera/matter) | MIT | 142 | 2024-07-16 · ARQUIVADO | NÃO VERIFICADO | NÃO VERIFICADO | ⛔ DO NOT USE |
| ecs | matter-ecs/matter | [link](https://github.com/matter-ecs/matter) | MIT | 116 | 2024-12-31 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| ecs | PepeElToro41/replecs | [link](https://github.com/PepeElToro41/replecs) | MIT | 62 | 2026-09-26 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| ecs | Ukendio/jecs | [link](https://github.com/Ukendio/jecs) | MIT | 471 | 2026-09-17 | 860 commits/54 autores; strict (projeto, .luaurc); testes 13 | Wally+Rojo | 🛠️ REQUIRES ADAPTATION |
| ecs | YetAnotherClown/planck | [link](https://github.com/YetAnotherClown/planck) | MIT | 57 | 2026-09-24 | 110 commits/10 autores; strict (projeto, .luaurc); testes 6 | Wally+Rojo | 🛠️ REQUIRES ADAPTATION |
| framework | Quenty/NevermoreEngine | [link](https://github.com/Quenty/NevermoreEngine) | MIT | 616 | 2026-09-24 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| framework | rbxts-flamework/core | [link](https://github.com/rbxts-flamework/core) | MIT | 159 | 2025-09-04 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| framework | Sleitnick/AeroGameFramework | [link](https://github.com/Sleitnick/AeroGameFramework) | MIT | 224 | 2022-12-29 · ARQUIVADO | NÃO VERIFICADO | NÃO VERIFICADO | ⛔ DO NOT USE |
| framework | Sleitnick/Axis | [link](https://github.com/Sleitnick/Axis) | MIT | 13 | 2023-12-29 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| framework | Sleitnick/Knit | [link](https://github.com/Sleitnick/Knit) | MIT | 630 | 2024-07-31 · ARQUIVADO | NÃO VERIFICADO | NÃO VERIFICADO | ⛔ DO NOT USE |
| framework | welcomestohell/prvdmwrong | [link](https://github.com/welcomestohell/prvdmwrong) | MPL-2.0 | 36 | 2025-12-29 | NÃO VERIFICADO | — | ⛔ DO NOT USE |
| signal | AlexanderLindholt/SignalPlus | [link](https://github.com/AlexanderLindholt/SignalPlus) | MIT | 38 | 2026-09-05 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| signal | stravant/goodsignal | [link](https://github.com/stravant/goodsignal) | MIT | 71 | 2025-08-28 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| state | littensy/charm | [link](https://github.com/littensy/charm) | MIT | 265 | 2026-06-21 | 129 commits/9 autores; strict (projeto, .luaurc); testes 30 | Wally+Rojo | ✅ READY TO INTEGRATE |
| state | littensy/reflex | [link](https://github.com/littensy/reflex) | MIT | 108 | 2025-12-21 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| state | Roblox/rodux | [link](https://github.com/Roblox/rodux) | Apache-2.0 | 335 | 2026-06-30 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| template | MonzterDev/Roblox-Game-Template | [link](https://github.com/MonzterDev/Roblox-Game-Template) | None | 16 | 2024-03-26 | NÃO VERIFICADO | Wally+Rojo | ⛔ DO NOT USE |
| utils | csqrl/sift | [link](https://github.com/cxmeel/sift) | MIT | 92 | 2025-03-12 | NÃO VERIFICADO | Wally+Rojo | 📖 USE AS REFERENCE ONLY |
| utils | Roblox/dash | [link](https://github.com/Roblox/dash) | MIT | 38 | 2026-09-05 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| utils | Sleitnick/RbxUtil | [link](https://github.com/Sleitnick/RbxUtil) | MIT | 467 | 2026-07-27 | 534 commits/33 autores; strict 16/69; testes 14 | Wally+Rojo | ✅ READY TO INTEGRATE |

## Rede & segurança

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| anticheat | chrisc06/TAC-Roblox-Anticheat | [link](https://github.com/chrisc06/TAC-Roblox-Anticheat) | MIT | 3 | 2026-01-10 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| authority | Roblox Server Authority | [link](https://create.roblox.com/docs/projects/server-authority) | Roblox Terms | n/a | oficial/DevForum | — | API da plataforma | ✅ READY TO INTEGRATE |
| input | Roblox Input Action System (IAS) | [link](https://create.roblox.com/docs/input/input-action-system) | Roblox Terms | n/a | oficial/DevForum | — | API da plataforma | ✅ READY TO INTEGRATE |
| networking | 1Axen/blink | [link](https://github.com/1Axen/blink) | MIT | 186 | 2026-09-19 | 489 commits/16 autores; strict (projeto, .luaurc); testes 4 | Rojo | ✅ READY TO INTEGRATE |
| networking | AstaWasTaken/NetRay | [link](https://github.com/AstaWasTaken/NetRay) | MIT | 10 | 2026-06-12 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| networking | ffrostfall/BridgeNet2 | [link](https://github.com/ffrostfall/BridgeNet2) | MIT | 72 | 2025-05-30 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| networking | ffrostfall/ByteNet | [link](https://github.com/ffrostfall/ByteNet) | MIT | 181 | 2025-08-01 | 78 commits/9 autores; strict (projeto, .luaurc); testes 0 | Wally+Rojo | 📖 USE AS REFERENCE ONLY |
| networking | imezx/Warp | [link](https://github.com/imezx/Warp) | MIT | 32 | 2026-05-05 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| networking | mrchigurh/Suphi-Packet | [link](https://github.com/mrchigurh/Suphi-Packet) | None | 4 | 2025-06-15 | NÃO VERIFICADO | — | ⛔ DO NOT USE |
| networking | Packet (Suphi) | [link](https://devforum.roblox.com/t/packet-networking-library/3573907) | ISC-like (declarado no post) | n/a | oficial/DevForum | — | Creator Store/rbxm | 📖 USE AS REFERENCE ONLY |
| networking | red-blox/Red | [link](https://github.com/red-blox/Red) | MIT | 57 | 2024-02-18 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| networking | red-blox/zap | [link](https://github.com/red-blox/zap) | MIT | 189 | 2026-06-23 | 334 commits/22 autores; strict 1/3; testes 2 | — | 📖 USE AS REFERENCE ONLY |
| networking | roblox-aurora/rbx-net | [link](https://github.com/roblox-aurora/rbx-net) | MIT | 108 | 2025-01-30 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| validation | osyrisrblx/t | [link](https://github.com/osyrisrblx/t) | MIT | 333 | 2025-03-11 | 302 commits/19 autores; strict 0/4; testes 1 | Wally+Rojo | ✅ READY TO INTEGRATE |

## Combate

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| ai | idiomic/Roblox_Sword_Fighting_AI | [link](https://github.com/idiomic/Roblox_Sword_Fighting_AI) | None | 11 | 2019-12-13 | NÃO VERIFICADO | — | ⛔ DO NOT USE |
| example | aziz8235/roblox-luau-game-framework | [link](https://github.com/aziz8235/roblox-luau-game-framework) | MIT | 0 | 2026-09-18 | NÃO VERIFICADO | — | ⛔ DO NOT USE |
| example | dwmk/RobloxGames | [link](https://github.com/dwmk/RobloxGames) | MIT | 3 | 2024-08-06 | NÃO VERIFICADO | — | 📖 USE AS REFERENCE ONLY |
| example | elomala/Fighting-game | [link](https://github.com/elomala/Fighting-game) | None | 8 | 2024-01-03 | NÃO VERIFICADO | — | ⛔ DO NOT USE |
| example | galenamc/Roblox-CombatSystem | [link](https://github.com/galenamc/Roblox-CombatSystem) | None | 2 | 2020-06-06 | NÃO VERIFICADO | — | ⛔ DO NOT USE |
| example | JoshuaIO/Fighting-Game-Framework-RobloxAPI | [link](https://github.com/JoshuaIO/Fighting-Game-Framework-RobloxAPI) | None | 1 | 2025-05-11 | NÃO VERIFICADO | Rojo | ⛔ DO NOT USE |
| example | rinme/UntitledGame | [link](https://github.com/rinme/UntitledGame) | None | 0 | 2026-09-15 | NÃO VERIFICADO | Rojo | ⛔ DO NOT USE |
| framework | hatmatty/AMS | [link](https://github.com/hatmatty/AMS) | MIT | 16 | 2022-06-02 | 178 commits/4 autores; strict 0/2; testes 0 | Rojo | 📖 USE AS REFERENCE ONLY |
| framework | wad4444/WCS | [link](https://github.com/wad4444/WCS) | MIT | 59 | 2025-11-12 | 512 commits/9 autores; strict 0/8; testes 0 | Wally+Rojo | 📖 USE AS REFERENCE ONLY |
| hitbox | CaidenSteele05/Attachment-Based-Raycast-Hit-Detection | [link](https://github.com/CaidenSteele05/Attachment-Based-Raycast-Hit-Detection) | None | 1 | 2026-04-06 | NÃO VERIFICADO | — | ⛔ DO NOT USE |
| hitbox | CatSushi/MuchachoHitbox | [link](https://github.com/CatSushi/MuchachoHitbox) | MIT | 3 | 2026-04-11 | 8 commits/1 autores; strict 0/0; testes 0 | — | 📖 USE AS REFERENCE ONLY |
| hitbox | HitboxClass v2 (DevForum) | [link](https://devforum.roblox.com/t/hitboxclass-v20-a-powerful-oop-based-hitbox-module/3929512) | None | n/a | oficial/DevForum | — | Creator Store/rbxm | ⛔ DO NOT USE |
| hitbox | Pyseph/ClientCast | [link](https://github.com/Pyseph/ClientCast) | MIT | 20 | 2023-09-25 | 93 commits/3 autores; strict 0/6; testes 0 | Rojo | 📖 USE AS REFERENCE ONLY |
| hitbox | RealHyperion/HitMesh-Pro | [link](https://github.com/RealHyperion/HitMesh-Pro) | None | 0 | 2024-11-27 | NÃO VERIFICADO | — | ⛔ DO NOT USE |
| hitbox | Swordphin/raycastHitboxRbxl | [link](https://github.com/Swordphin/raycastHitboxRbxl) | MIT | 70 | 2021-09-21 | 26 commits/6 autores; strict 6/8; testes 0 | Rojo | 📖 USE AS REFERENCE ONLY |
| hitbox | TeamSwordphin/ShapecastHitbox | [link](https://github.com/TeamSwordphin/ShapecastHitbox) | MIT | 22 | 2025-08-12 | 24 commits/1 autores; strict 10/14; testes 0 | Wally+Rojo | 🛠️ REQUIRES ADAPTATION |
| lagcomp | michaelvqq/RollbackHitbox | [link](https://github.com/michaelvqq/RollbackHitbox) | MIT | 8 | 2026-07-09 | 10 commits/2 autores; strict 5/5; testes 0 | Wally+Rojo | 🛠️ REQUIRES ADAPTATION |
| lagcomp | text21/Rewind | [link](https://github.com/text21/Rewind) | None | 0 | 2026-01-09 | 31 commits/2 autores; strict 35/623; testes 73 | Wally+Rojo | ⛔ DO NOT USE |
| lockon | EzLockOn (DevForum) | [link](https://devforum.roblox.com/t/ezlockon-fully-typed-optimized-lock-on-for-fighting-games/3150695) | None | n/a | oficial/DevForum | — | Creator Store/rbxm | ⛔ DO NOT USE |
| projectile | 1Axen/Secure-Cast | [link](https://github.com/1Axen/Secure-Cast) | MIT | 30 | 2024-10-21 · ARQUIVADO | 57 commits/5 autores; strict 13/16; testes 0 | Wally+Rojo | 📖 USE AS REFERENCE ONLY |
| projectile | EtiTheSpirit/FastCastAPIDocs | [link](https://github.com/EtiTheSpirit/FastCastAPIDocs) | MPL-2.0 | 12 | 2020-09-04 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| projectile | noahrepublic/trojectile | [link](https://github.com/noahrepublic/trojectile) | MIT | 0 | 2024-06-03 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| projectile | synpixel/flashcast | [link](https://github.com/synpixel/flashcast) | MIT | 8 | 2024-04-27 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| projectile | weenachuangkud/FastCast2 | [link](https://github.com/weenachuangkud/FastCast2) | MIT (código) + CC BY-NC-ND 4.0 (arte) | 28 | 2026-09-20 | 1205 commits/9 autores; strict 4/17; testes 0 | Wally+Rojo | 🛠️ REQUIRES ADAPTATION |
| ragdoll | Brawldude2/RagdollService | [link](https://github.com/Brawldude2/RagdollService) | MIT | 7 | 2026-07-31 | 27 commits/1 autores; strict 9/9; testes 0 | Rojo | 🛠️ REQUIRES ADAPTATION |
| statemachine | prooheckcp/RobloxStateMachine | [link](https://github.com/prooheckcp/RobloxStateMachine) | MIT | 41 | 2024-05-12 | 149 commits/5 autores; strict 0/13; testes 0 | Wally+Rojo | 📖 USE AS REFERENCE ONLY |

## Movimento

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| anime | Anime Movement System (DevForum) | [link](https://devforum.roblox.com/t/anime-movement-system-open-source/1553138) | None | n/a | oficial/DevForum | — | Creator Store/rbxm | ⛔ DO NOT USE |
| character | MaximumADHD/Character-Realism | [link](https://github.com/MaximumADHD/Character-Realism) | MPL-2.0 | 132 | 2026-06-23 | 26 commits/5 autores; strict 3/4; testes 0 | Rojo | 🛠️ REQUIRES ADAPTATION |
| controller | easy-games/chickynoid | [link](https://github.com/easy-games/chickynoid) | MIT | 264 | 2024-01-03 | 399 commits/17 autores; strict 0/51; testes 0 | Wally+Rojo | 📖 USE AS REFERENCE ONLY |
| controller | Roblox Character Controller Library (CCL) | [link](https://create.roblox.com/docs/characters/character-controller-library) | Roblox Terms | n/a | oficial/DevForum | — | API da plataforma | 🛠️ REQUIRES ADAPTATION |
| dash | lewuat/Roblox-DashPlace | [link](https://github.com/lewuat/Roblox-DashPlace) | Unlicense | 0 | 2026-04-15 | NÃO VERIFICADO | — | 📖 USE AS REFERENCE ONLY |
| grapple | Ecliptorhizes/Hooksystem | [link](https://github.com/Ecliptorhizes/Hooksystem) | MIT | 2 | 2026-03-09 | NÃO VERIFICADO | Wally+Rojo | 📖 USE AS REFERENCE ONLY |
| gravity | EgoMoose/gravity-camera | [link](https://github.com/EgoMoose/gravity-camera) | MIT | 8 | 2025-01-09 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| gravity | EgoMoose/Rbx-Gravity-Controller | [link](https://github.com/EgoMoose/Rbx-Gravity-Controller) | MIT | 51 | 2022-09-03 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| gravity | EgoMoose/rbx-wallstick | [link](https://github.com/EgoMoose/rbx-wallstick) | MIT | 49 | 2026-06-04 | 21 commits/1 autores; strict 14/14; testes 0 | Wally+Rojo | 🛠️ REQUIRES ADAPTATION |
| gravity | KendallCole/RobloxGravityKit | [link](https://github.com/KendallCole/RobloxGravityKit) | None | 3 | 2025-04-07 | NÃO VERIFICADO | Rojo | ⛔ DO NOT USE |
| melee | shmove/roblox-melee-movement-system | [link](https://github.com/shmove/roblox-melee-movement-system) | Unlicense | 4 | 2023-08-31 · ARQUIVADO | NÃO VERIFICADO | — | 📖 USE AS REFERENCE ONLY |
| parkour | carlos123344222/robloxgame | [link](https://github.com/carlos123344222/robloxgame) | None | 0 | 2026-09-29 | NÃO VERIFICADO | Rojo | ⛔ DO NOT USE |
| parkour | MaxDevLol/Roblox-Parkour-System-by-max | [link](https://github.com/MaxDevLol/Roblox-Parkour-System-by-max) | MIT | 1 | 2026-02-11 | NÃO VERIFICADO | — | 📖 USE AS REFERENCE ONLY |
| parkour | Slubbie/slubbie | [link](https://github.com/Slubbie/slubbie) | None | 0 | 2026-09-27 | NÃO VERIFICADO | Rojo | ⛔ DO NOT USE |

## Habilidades & status

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| status | Effectify (DevForum) | [link](https://devforum.roblox.com/t/effectify-v131-a-customizable-status-effect-implementation/3635681) | None | n/a | oficial/DevForum | — | Creator Store/rbxm | ⛔ DO NOT USE |
| status | Opxourc/statusify | [link](https://github.com/Opxourc/statusify) | MIT | 1 | 2026-09-26 | NÃO VERIFICADO | Wally+Rojo | 📖 USE AS REFERENCE ONLY |
| status | WBlair1/StatusEffectManager | [link](https://github.com/WBlair1/StatusEffectManager) | MIT | 2 | 2026-01-31 | NÃO VERIFICADO | — | 📖 USE AS REFERENCE ONLY |

## NPC / IA

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| ai | KURVOX/roblox-ai-npc | [link](https://github.com/KURVOX/roblox-ai-npc) | MIT | 0 | 2026-09-23 | NÃO VERIFICADO | — | ⛔ DO NOT USE |
| bt | Defaultio/BehaviorTree3 | [link](https://github.com/Defaultio/BehaviorTree3) | GPL-3.0 | 45 | 2023-06-24 | 45 commits/5 autores; strict 0/2; testes 0 | — | ⛔ DO NOT USE |
| bt | howmanysmall/behaviortree.rbxlua | [link](https://github.com/hms-junk/behaviortree.rbxlua) | None | 0 | 2018-07-10 | NÃO VERIFICADO | — | ⛔ DO NOT USE |
| bt | seyaidev/behaviortree.rbxlua | [link](https://github.com/spelled-ayayron/behaviortree.rbxlua) | None | 9 | 2019-08-05 | NÃO VERIFICADO | — | ⛔ DO NOT USE |
| pathfinding | grayzcale/simplepath | [link](https://github.com/ahmicy/simplepath) | MIT | 70 | 2026-06-11 | 176 commits/10 autores; strict 0/3; testes 2 | — | ✅ READY TO INTEGRATE |
| pathfinding | imezx/JPSPlus | [link](https://github.com/imezx/JPSPlus) | LGPL-3.0 | 4 | 2026-01-30 | NÃO VERIFICADO | NÃO VERIFICADO | ⛔ DO NOT USE |
| pathfinding | kozuidev/PathForge | [link](https://github.com/kozuidev/PathForge) | None | 0 | 2025-08-24 | NÃO VERIFICADO | — | ⛔ DO NOT USE |
| pathfinding | NoobPath (DevForum) | [link](https://devforum.roblox.com/t/noobpath-easy-pathfinding/3254514) | None | n/a | oficial/DevForum | — | Creator Store/rbxm | ⛔ DO NOT USE |
| pathfinding | Roblox PathfindingService | [link](https://create.roblox.com/docs/characters/pathfinding) | Roblox Terms | n/a | oficial/DevForum | — | API da plataforma | ✅ READY TO INTEGRATE |

## Quests

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| quest | prooheckcp/RoQuest | [link](https://github.com/prooheckcp/RoQuest) | Apache-2.0 (LICENSE) ≠ MIT (README) | 20 | 2025-05-22 | 124 commits/3 autores; strict 13/63; testes 0 | Wally+Rojo | 🛠️ REQUIRES ADAPTATION |

## Inventário / itens / economia

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| backpack | ryanlua/purse | [link](https://github.com/ryanlua/purse) | Apache-2.0 | 17 | 2026-09-22 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| backpack | ryanlua/satchel | [link](https://github.com/ryanlua/satchel) | MPL-2.0 | 133 | 2026-09-22 | 1020 commits/10 autores; strict 1/4; testes 0 | Wally+Rojo | 📖 USE AS REFERENCE ONLY |
| hotbar | ImAvafe/NeoHotbar | [link](https://github.com/loneka/neohotbar) | MIT | 28 | 2026-02-04 | NÃO VERIFICADO | Wally+Rojo | 📖 USE AS REFERENCE ONLY |
| inventory | Asiandayboy/InventoryMaker | [link](https://github.com/Asiandayboy/InventoryMaker) | MIT | 17 | 2025-12-21 | 61 commits/1 autores; strict 9/11; testes 0 | Rojo | 📖 USE AS REFERENCE ONLY |
| inventory | lab2SecurityProjectsR/inventory-logic-NoGoodUi | [link](https://github.com/lab2SecurityProjectsR/inventory-logic-NoGoodUi) | Proprietary | 0 | 2026-09-29 | NÃO VERIFICADO | Rojo | ⛔ DO NOT USE |
| inventory | Zyn-ic/Stoway | [link](https://github.com/Zyn-ic/Stoway) | MIT | 13 | 2026-03-07 | 73 commits/2 autores; strict 0/35; testes 0 | Wally+Rojo | 🛠️ REQUIRES ADAPTATION |

## Persistência

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| data | anthony0br/DocumentService | [link](https://github.com/anthony0br/DocumentService) | MIT | 53 | 2026-09-07 | 389 commits/13 autores; strict 16/28; testes 10 | Wally+Rojo | ✅ READY TO INTEGRATE |
| data | Kampfkarren/Roblox | [link](https://github.com/Kampfkarren/Roblox) | Custom | 393 | 2023-03-17 | NÃO VERIFICADO | Wally+Rojo | 📖 USE AS REFERENCE ONLY |
| data | MadStudioRoblox/ProfileService | [link](https://github.com/MadStudioRoblox/ProfileService) | Apache-2.0 | 329 | 2023-06-29 | NÃO VERIFICADO | NÃO VERIFICADO | ⛔ DO NOT USE |
| data | MadStudioRoblox/ProfileStore | [link](https://github.com/MadStudioRoblox/ProfileStore) | Apache-2.0 | 338 | 2025-07-31 | 32 commits/5 autores; strict 0/2; testes 0 | Wally+Rojo | ✅ READY TO INTEGRATE |
| data | nezuo/lapis | [link](https://github.com/nezuo/lapis) | MIT | 81 | 2025-02-11 | 198 commits/5 autores; strict 1/23; testes 7 | Wally+Rojo | 📖 USE AS REFERENCE ONLY |
| data | noahrepublic/DataKeep | [link](https://github.com/noahrepublic/DataKeep) | MIT | 20 | 2025-09-14 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| data | paradoxum-games/lyra | [link](https://github.com/paradoxum-games/lyra) | MIT | 152 | 2026-03-25 | 552 commits/8 autores; strict (projeto, .luaurc); testes 23 | Wally+Rojo | 🛠️ REQUIRES ADAPTATION |
| data | Suphi's DataStore Module (DevForum) | [link](https://devforum.roblox.com/t/suphis-datastore-module/2425597) | ISC-like (declarado no post) | n/a | oficial/DevForum | — | Creator Store/rbxm | 📖 USE AS REFERENCE ONLY |
| replication | MadStudioRoblox/Replica | [link](https://github.com/MadStudioRoblox/Replica) | Apache-2.0 | 75 | 2025-08-07 | 12 commits/3 autores; strict 2/6; testes 0 | Rojo | 📖 USE AS REFERENCE ONLY |
| replication | MadStudioRoblox/ReplicaService | [link](https://github.com/MadStudioRoblox/ReplicaService) | Apache-2.0 | 68 | 2024-10-16 | NÃO VERIFICADO | NÃO VERIFICADO | ⛔ DO NOT USE |

## Customização de personagem

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| avatar | Roblox HumanoidDescription / AvatarEditorService | [link](https://create.roblox.com/docs/characters/appearance) | Roblox Terms | n/a | oficial/DevForum | — | API da plataforma | ✅ READY TO INTEGRATE |
| avatar | vocksel/Sugar | [link](https://github.com/vocksel/Sugar) | MIT | 6 | 2019-09-08 | NÃO VERIFICADO | Rojo | 📖 USE AS REFERENCE ONLY |

## Câmera

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| camera | LugicalDev/CameraService | [link](https://github.com/rduoDevs/CameraService) | MIT | 36 | 2026-06-10 | NÃO VERIFICADO | — | 📖 USE AS REFERENCE ONLY |
| camera | Yiannis123Git/ShiftUnlocked | [link](https://github.com/Yiannis123Git/ShiftUnlocked) | MIT | 5 | 2024-05-29 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| shake | Sleitnick/RbxCameraShaker | [link](https://github.com/Sleitnick/RbxCameraShaker) | MIT | 125 | 2019-12-15 | 9 commits/1 autores; strict 0/3; testes 0 | Rojo | ✅ READY TO INTEGRATE |
| spring | Fraktality/spr | [link](https://github.com/Fraktality/spr) | MIT | 144 | 2024-07-30 | 84 commits/4 autores; strict 1/1; testes 0 | Rojo | ✅ READY TO INTEGRATE |

## Animação

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| anim | evaera/roblox-animation-transfer | [link](https://github.com/evaera/roblox-animation-transfer) | MIT | 53 | 2023-07-14 · ARQUIVADO | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| anim | Khaomi/Animator | [link](https://github.com/Khaomi/Animator) | MIT | 11 | 2025-07-02 · ARQUIVADO | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| anim | michaeldougal/AnimNation | [link](https://github.com/michaeldougal/AnimNation) | MIT | 15 | 2026-06-26 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| anim | wes-BAN/crux-animation | [link](https://github.com/wes-BAN/crux-animation) | MIT | 4 | 2016-06-13 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| anim | wrello/Animations | [link](https://github.com/wrello/Animations) | MIT | 20 | 2026-02-22 | 171 commits/3 autores; strict 3/14; testes 0 | — | 🛠️ REQUIRES ADAPTATION |

## VFX

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| emit | zilibobi/forge-vfx | [link](https://github.com/zilibobi/forge-vfx) | Custom (VFX-DL-1.1) | 18 | 2026-07-26 | 151 commits/1 autores; strict 2/56; testes 11 | Wally+Rojo | 🛠️ REQUIRES ADAPTATION |
| pool | PartCache (DevForum) | [link](https://devforum.roblox.com/t/partcache-for-all-your-quick-part-creation-needs/246641) | None | n/a | oficial/DevForum | — | Creator Store/rbxm | ⛔ DO NOT USE |
| pool | Pyseph/ObjectCache | [link](https://github.com/Pyseph/ObjectCache) | MIT | 19 | 2025-03-19 | 29 commits/4 autores; strict 1/1; testes 0 | Wally+Rojo | ✅ READY TO INTEGRATE |
| replication | wad4444/refx | [link](https://github.com/wad4444/refx) | MIT | 16 | 2024-12-23 | 139 commits/5 autores; strict 1/25; testes 3 | Wally+Rojo | 📖 USE AS REFERENCE ONLY |

## UI

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| components | 7kayoh/Lydie | [link](https://github.com/7kayoh/Lydie) | MIT (texto) | 29 | 2026-08-13 | NÃO VERIFICADO | Wally+Rojo | 📖 USE AS REFERENCE ONLY |
| components | loneka/onyx-ui | [link](https://github.com/loneka/onyx-ui) | MIT | 59 | 2026-02-09 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| debug | SirMallard/Iris | [link](https://github.com/SirMallard/Iris) | MIT | 354 | 2026-08-10 | 522 commits/27 autores; strict 0/31; testes 2 | Wally+Rojo | ✅ READY TO INTEGRATE |
| motion | littensy/ripple | [link](https://github.com/littensy/ripple) | MIT | 130 | 2026-07-18 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| storybook | flipbook-labs/flipbook | [link](https://github.com/flipbook-labs/flipbook) | MIT | 125 | 2026-09-24 | NÃO VERIFICADO | NÃO VERIFICADO | ✅ READY TO INTEGRATE |
| storybook | Kampfkarren/hoarcekat | [link](https://github.com/Kampfkarren/hoarcekat) | MPL-2.0 | 148 | 2025-11-21 | NÃO VERIFICADO | Wally | 📖 USE AS REFERENCE ONLY |
| storybook | PepeElToro41/ui-labs | [link](https://github.com/PepeElToro41/ui-labs) | GPL-3.0 | 194 | 2026-09-19 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| topbar | 1ForeverHD/TopbarPlus | [link](https://github.com/1ForeverHD/TopbarPlus) | MPL-2.0 + cláusula de crédito | 236 | 2025-09-17 | 397 commits/30 autores; strict 2/21; testes 0 | Wally+Rojo | 🛠️ REQUIRES ADAPTATION |
| ui | centau/vide | [link](https://github.com/centau/vide) | MIT | 337 | 2026-09-28 | 207 commits/25 autores; strict (projeto, .luaurc); testes 7 | Wally+Rojo | ✅ READY TO INTEGRATE |
| ui | dphfox/Fusion | [link](https://github.com/dphfox/Fusion) | MIT | 798 | 2026-02-01 | 933 commits/53 autores; strict (projeto, .luaurc); testes 49 | Wally+Rojo | 📖 USE AS REFERENCE ONLY |
| ui | ffrostfall/fluid | [link](https://github.com/ffrostfall/fluid) | MIT | 40 | 2026-07-26 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| ui | jsdotlua/react-lua | [link](https://github.com/jsdotlua/react-lua) | MIT | 570 | 2025-05-23 | NÃO VERIFICADO | NÃO VERIFICADO | 📖 USE AS REFERENCE ONLY |
| ui | Roblox/roact | [link](https://github.com/Roblox/roact) | Apache-2.0 | 626 | 2023-12-13 · ARQUIVADO | NÃO VERIFICADO | NÃO VERIFICADO | ⛔ DO NOT USE |

## Mundo / mapa

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| procedural | Gzeu/roblox-procedural-worlds | [link](https://github.com/Gzeu/roblox-procedural-worlds) | MIT | 0 | 2026-04-14 | 53 commits/1 autores; strict 19/73; testes 0 | Rojo | 📖 USE AS REFERENCE ONLY |
| procedural | TheArturZh/RTerrainGenerator | [link](https://github.com/TheArturZh/RTerrainGenerator) | MIT | 8 | 2020-05-14 | NÃO VERIFICADO | Rojo | 📖 USE AS REFERENCE ONLY |
| streaming | Roblox StreamingEnabled / Places / TeleportService | [link](https://create.roblox.com/docs/workspace/streaming) | Roblox Terms | n/a | oficial/DevForum | — | API da plataforma | ✅ READY TO INTEGRATE |
| zone | 1ForeverHD/ZonePlus | [link](https://github.com/1ForeverHD/ZonePlus) | MIT | 101 | 2024-02-02 | 196 commits/9 autores; strict 0/12; testes 0 | Wally+Rojo | 📖 USE AS REFERENCE ONLY |

## Performance

| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |
| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |
| parallel | Roblox Parallel Luau (Actors) | [link](https://create.roblox.com/docs/scripting/multithreading) | Roblox Terms | n/a | oficial/DevForum | — | API da plataforma | ✅ READY TO INTEGRATE |

## Transformações

Nenhum candidato reutilizável foi encontrado (buscas no GitHub, no Wally e no DevForum). **Construir do zero** sobre o runtime de habilidades e status. Ver [`catalog/transformations/`](catalog/transformations/README.md).

