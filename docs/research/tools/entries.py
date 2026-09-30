# Curated catalog entries for Genesis Realms research (verified 2026-09-29).
# Fields: cat, sub, name, src, lic, lic_ev, rec, sec, notes  (+ optional url)
# src: github | devforum | roblox-official | creator-store
R = "READY TO INTEGRATE"; A = "REQUIRES ADAPTATION"; F = "USE AS REFERENCE ONLY"; X = "DO NOT USE"
AUD_OK = "AUDITADO (grep + leitura): sem achados críticos"
NA = "NÃO AUDITADO (fora da shortlist)"
TOOL = "NÃO AUDITADO (ferramenta de build, não entra no jogo)"
OFF = "N/A (recurso oficial da plataforma)"
NOLIC = "NÃO CONFIRMADO — NÃO USAR ATÉ VERIFICAR"

E = [
# ---------------- TOOLING
dict(cat="tooling", sub="sync", name="rojo-rbx/rojo", lic="MPL-2.0", lic_ev="ecosyste.ms + awesome-roblox", rec=R, sec=TOOL, notes="Sincronização filesystem↔Studio; padrão de fato. Base de toda a arquitetura src/client|server|shared."),
dict(cat="tooling", sub="toolchain", name="rojo-rbx/rokit", lic="MIT", lic_ev="ecosyste.ms", rec=R, sec=TOOL, notes="Gerenciador de toolchain ('Next-generation toolchain manager', org rojo-rbx; alternativa a Aftman/Foreman). Fixa versões de rojo/wally/selene/stylua/lune/luau-lsp/blink."),
dict(cat="tooling", sub="packages", name="UpliftGames/wally", lic="MPL-2.0", lic_ev="ecosyste.ms", rec=R, sec=TOOL, notes="Gerenciador de pacotes. ATENÇÃO: registro tem muitos re-uploads/forks de terceiros; fixar escopo oficial do autor."),
dict(cat="tooling", sub="packages", name="pesde-pkg/pesde", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=TOOL, notes="Alternativa ao Wally (multi-runtime). Não usar dois gerenciadores; manter Wally."),
dict(cat="tooling", sub="lint", name="Kampfkarren/selene", lic="MPL-2.0", lic_ev="ecosyste.ms", rec=R, sec=TOOL, notes="Linter Luau."),
dict(cat="tooling", sub="format", name="JohnnyMorganz/StyLua", lic="MPL-2.0", lic_ev="ecosyste.ms", rec=R, sec=TOOL, notes="Formatter."),
dict(cat="tooling", sub="lsp", name="JohnnyMorganz/luau-lsp", lic="MIT", lic_ev="ecosyste.ms", rec=R, sec=TOOL, notes="Language server (VS Code); typecheck --!strict em CI."),
dict(cat="tooling", sub="runtime", name="lune-org/lune", lic="MPL-2.0", lic_ev="ecosyste.ms", rec=R, sec=TOOL, notes="Runtime Luau standalone: scripts de build, validação de dados de conteúdo, testes fora do Studio."),
dict(cat="tooling", sub="transform", name="seaofvoices/darklua", lic="MIT", lic_ev="ecosyste.ms", rec=R, sec=TOOL, notes="Opcional: transforma requires por string/paths; usado por DocumentService no build."),
dict(cat="tooling", sub="test", name="jsdotlua/jest-lua", lic="MIT", lic_ev="ecosyste.ms", rec=R, sec=TOOL, notes="Framework de testes (porte do Jest) mantido pela org jsdotlua; TestEZ está arquivado. Último push 2024-12: pouco movimento."),
dict(cat="tooling", sub="test", name="Roblox/testez", lic="Apache-2.0", lic_ev="ecosyste.ms", rec=X, sec=TOOL, notes="Arquivado (ecosyste.ms: archived=true). Usar Jest-Lua."),
dict(cat="tooling", sub="docs", name="evaera/moonwave", lic="MPL-2.0", lic_ev="ecosyste.ms", rec=R, sec=TOOL, notes="Opcional: docs de API a partir de comentários."),
dict(cat="tooling", sub="types", name="JohnnyMorganz/wally-package-types", lic="MIT", lic_ev="ecosyste.ms", rec=R, sec=TOOL, notes="Reexporta tipos de pacotes Wally (necessário p/ --!strict com Packages)."),
dict(cat="tooling", sub="assets", name="jackTabsCode/asphalt", lic="MIT", lic_ev="ecosyste.ms", rec=R, sec=TOOL, notes="Assets-as-files: upload de imagens/sons/meshes por CLI e geração de tabela de IDs versionada."),
dict(cat="tooling", sub="assets", name="rojo-rbx/tarmac", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=TOOL, notes="Ferramenta de assets mais antiga (org rojo-rbx); último push 2024-03. Asphalt cobre o mesmo caso e está ativo."),
dict(cat="tooling", sub="deploy", name="blake-mealey/mantle", lic="MIT", lic_ev="ecosyste.ms", rec=A, sec=TOOL, notes="Opcional: infraestrutura-como-código (places, produtos, badges) p/ ambientes dev/staging/prod."),
dict(cat="tooling", sub="sync", name="argon-rbx/argon", lic="Apache-2.0", lic_ev="ecosyste.ms", rec=F, sec=TOOL, notes="Alternativa ao Rojo. Não misturar ferramentas de sync."),
dict(cat="tooling", sub="sync", name="Iron-Stag-Games/Lync", lic="LGPL-2.1", lic_ev="ecosyste.ms", rec=F, sec=TOOL, notes="Alternativa ao Rojo (LGPL; ferramenta, não entra no jogo)."),
dict(cat="tooling", sub="toolchain", name="Roblox/foreman", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=TOOL, notes="Toolchain manager anterior da Roblox; Rokit (org rojo-rbx) é a alternativa ativa escolhida."),
dict(cat="tooling", sub="ts", name="roblox-ts/roblox-ts", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=TOOL, notes="Stack TypeScript. Genesis usa Luau; relevante só p/ entender libs compiladas de TS (WCS, refx)."),
dict(cat="tooling", sub="docs", name="Roblox/creator-docs", lic="CC-BY-4.0", lic_ev="ecosyste.ms", rec=F, sec=OFF, notes="Documentação oficial (fonte das páginas de Server Authority, IAS, CCL)."),
dict(cat="tooling", sub="ai", name="Roblox/studio-rust-mcp-server", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=TOOL, notes="Arquivado; substituído pelo MCP embutido no Studio (mar/2026)."),
dict(cat="tooling", sub="ai", name="Roblox Studio built-in MCP server", src="roblox-official", url="https://devforum.roblox.com/t/assistant-updates-studio-built-in-mcp-server-and-playtest-automation/4474643", lic="Roblox Terms", lic_ev="anúncio oficial DevForum 2026-03-05", rec=R, sec=OFF, notes="Integração oficial com Claude Code: ler/editar scripts, rodar código, playtest automatizado. Revisar edições antes de publicar."),
dict(cat="tooling", sub="language", name="luau-lang/luau", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=TOOL, notes="Linguagem/typechecker (referência)."),
dict(cat="tooling", sub="opencloud", name="Sleitnick/rbxcloud", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=TOOL, notes="CLI Open Cloud (DataStore/Messaging) p/ ferramentas de suporte/admin fora do jogo."),
dict(cat="tooling", sub="dom", name="rojo-rbx/rbx-dom", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=TOOL, notes="(De)serialização de arquivos Roblox em Rust; base de Rojo/Lune."),

# ---------------- CORE FRAMEWORKS
dict(cat="core-frameworks", sub="framework", name="Sleitnick/Knit", lic="MIT", lic_ev="ecosyste.ms + página GitHub", rec=X, sec=NA, notes="Arquivado em 2024-07-31 ('will no longer receive updates')."),
dict(cat="core-frameworks", sub="framework", name="Sleitnick/AeroGameFramework", lic="MIT", lic_ev="ecosyste.ms", rec=X, sec=NA, notes="Arquivado/deprecado (predecessor do Knit)."),
dict(cat="core-frameworks", sub="utils", name="Sleitnick/RbxUtil", lic="MIT", lic_ev="LICENSE (clone)", rec=R, sec=AUD_OK, notes="Coleção modular (Signal, Trove, TableUtil, Timer, Component...). Usar SOMENTE módulos selecionados via Wally (sleitnick/*). HttpService usado apenas p/ JSON."),
dict(cat="core-frameworks", sub="framework", name="Quenty/NevermoreEngine", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Monorepo enorme e ativo (285 pacotes em src/), com loader/ecossistema próprio (lock-in). Consultar pacotes individuais (src/octree, src/spring, CameraStackService em src/camera) como referência."),
dict(cat="core-frameworks", sub="framework", name="welcomestohell/prvdmwrong", lic="MPL-2.0", lic_ev="LICENSE.md (clone)", rec=X, sec=NA, notes="README do próprio autor: 'unfinished. Do not use ... for production'."),
dict(cat="core-frameworks", sub="framework", name="Sleitnick/Axis", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Provider framework experimental; último push 2023-12."),
dict(cat="core-frameworks", sub="framework", name="rbxts-flamework/core", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Exige TypeScript/roblox-ts. Incompatível com stack Luau (é dependência runtime do WCS)."),
dict(cat="core-frameworks", sub="async", name="evaera/roblox-lua-promise", lic="MIT", lic_ev="LICENSE (clone)", rec=R, sec=AUD_OK, notes="Somente se uma dependência exigir (ex.: Lapis). Preferir task.* nativo no código próprio. Último commit 2023-10 (estável)."),
dict(cat="core-frameworks", sub="cleanup", name="howmanysmall/Janitor", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=AUD_OK, notes="Equivalente ao Trove; escolher UM (recomendado: Trove do RbxUtil). 31/38 arquivos --!strict."),
dict(cat="core-frameworks", sub="ecs", name="Ukendio/jecs", lic="MIT", lic_ev="LICENSE (clone)", rec=A, sec=AUD_OK, notes="ECS mais ativo (860 commits, 54 contributors). Candidato p/ simulação de NPCs/projéteis/status em massa — adotar após profiling (Fase 5/10)."),
dict(cat="core-frameworks", sub="ecs", name="matter-ecs/matter", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Fork mantido do Matter; último push 2024-12."),
dict(cat="core-frameworks", sub="ecs", name="evaera/matter", lic="MIT", lic_ev="ecosyste.ms", rec=X, sec=NA, notes="Arquivado (continuação em matter-ecs/matter)."),
dict(cat="core-frameworks", sub="ecs", name="centau/ecr", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="ECS sparse-set; alternativa ao jecs."),
dict(cat="core-frameworks", sub="ecs", name="YetAnotherClown/planck", lic="MIT", lic_ev="LICENSE (clone)", rec=A, sec=AUD_OK, notes="Scheduler agnóstico p/ ECS (110 commits, 10 autores, strict no projeto); avaliar junto com jecs."),
dict(cat="core-frameworks", sub="ecs", name="PepeElToro41/replecs", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Replicação p/ jecs; avaliar contra Server Authority nativo antes de adotar."),
dict(cat="core-frameworks", sub="utils", name="csqrl/sift", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=NA, notes="Dados imutáveis; autor declara 'no longer actively maintained'."),
dict(cat="core-frameworks", sub="signal", name="stravant/goodsignal", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Coberto pelo Signal do RbxUtil (baseado no mesmo design)."),
dict(cat="core-frameworks", sub="signal", name="AlexanderLindholt/SignalPlus", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Alternativa de Signal."),
dict(cat="core-frameworks", sub="state", name="littensy/charm", lic="MIT", lic_ev="LICENSE (clone)", rec=R, sec=AUD_OK, notes="Estado atômico + pacote charm-sync (mesmo repo) p/ replicar estado servidor→cliente (UI). 30 arquivos de teste."),
dict(cat="core-frameworks", sub="state", name="littensy/reflex", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Mesmo autor do Charm; container de estado estilo Redux."),
dict(cat="core-frameworks", sub="state", name="Roblox/rodux", lic="Apache-2.0", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Redux-like; mais verboso que Charm."),
dict(cat="core-frameworks", sub="admin", name="evaera/Cmdr", lic="MIT", lic_ev="LICENSE (clone)", rec=R, sec="AUDITADO: seguro por padrão (comandos bloqueados in-game sem hook BeforeRun); built-ins incluem fetch (HttpService.GetAsync), kick e teleport", notes="Console dev/admin: 666 commits, 63 autores, ativo (2026-09). Registrar só os comandos necessários e restringir via BeforeRun no servidor."),
dict(cat="core-frameworks", sub="admin", name="alicesaidhi/conch", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Alternativa ao Cmdr."),
dict(cat="core-frameworks", sub="admin", name="Epix-Incorporated/Adonis", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Sistema de moderação completo; grande superfície. Não auditado; fora do escopo do core."),
dict(cat="core-frameworks", sub="utils", name="Roblox/dash", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Mirror read-only de utilitários da Roblox."),
dict(cat="core-frameworks", sub="template", name="MonzterDev/Roblox-Game-Template", lic="None", lic_ev="sem arquivo LICENSE (clone)", rec=X, sec=NA, notes=NOLIC + ". Template com ProfileService (legado)."),

# ---------------- NETWORKING / SECURITY
dict(cat="networking-security", sub="authority", name="Roblox Server Authority", src="roblox-official", url="https://create.roblox.com/docs/projects/server-authority", lic="Roblox Terms", lic_ev="docs oficiais + newsroom 2026-07-09", rec=R, sec=OFF, notes="Workspace.AuthorityMode=Server; RunService:BindToSimulation; predição+rollback no cliente; exige StreamingEnabled, IAS, SignalBehavior Deferred. Fundação de combate/movimento."),
dict(cat="networking-security", sub="input", name="Roblox Input Action System (IAS)", src="roblox-official", url="https://create.roblox.com/docs/input/input-action-system", lic="Roblox Terms", lic_ev="DevForum full release 2026-06", rec=R, sec=OFF, notes="InputContext/InputAction cross-platform (PC/mobile/console). Obrigatório p/ inputs que afetam simulação sob Server Authority."),
dict(cat="networking-security", sub="networking", name="1Axen/blink", lic="MIT", lic_ev="LICENSE (clone)", rec=R, sec=AUD_OK, notes="Compilador IDL → código Luau tipado com buffers; validação de tipos no servidor gerada. Mais ativo da categoria (489 commits, 16 contributors, 42 commits em 12m)."),
dict(cat="networking-security", sub="networking", name="red-blox/zap", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=AUD_OK, notes="Alternativa equivalente ao Blink (IDL). Escolher UM."),
dict(cat="networking-security", sub="networking", name="ffrostfall/ByteNet", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=AUD_OK, notes="Sem commits nos últimos 12 meses (último 2025-08)."),
dict(cat="networking-security", sub="networking", name="roblox-aurora/rbx-net", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Orientado a roblox-ts; último push 2025-01."),
dict(cat="networking-security", sub="networking", name="ffrostfall/BridgeNet2", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Mesmo autor do ByteNet; último push 2025-05."),
dict(cat="networking-security", sub="networking", name="red-blox/Red", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Último push 2024-02; vendorizado dentro do RoQuest."),
dict(cat="networking-security", sub="networking", name="imezx/Warp", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Alternativa de networking."),
dict(cat="networking-security", sub="networking", name="AstaWasTaken/NetRay", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Pouca adoção aparente."),
dict(cat="networking-security", sub="networking", name="Packet (Suphi)", src="devforum", url="https://devforum.roblox.com/t/packet-networking-library/3573907", lic="ISC-like (declarado no post)", lic_ev="texto no post DevForum", rec=F, sec="NÃO AUDITADO; comunidade relatou vulnerabilidades (retomada de coroutine / bypass de limite de buffer)", notes="Distribuído via Creator Store (asset 104116977416770), sem repositório oficial."),
dict(cat="networking-security", sub="networking", name="mrchigurh/Suphi-Packet", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec=NA, notes="Mirror de TERCEIRO do Packet, sem licença. " + NOLIC),
dict(cat="networking-security", sub="validation", name="osyrisrblx/t", lic="MIT", lic_ev="LICENSE (clone)", rec=R, sec=AUD_OK, notes="Validação runtime de payloads/configs (também usado por Lyra/WCS). Estável; último commit 2025-03."),
dict(cat="networking-security", sub="anticheat", name="chrisc06/TAC-Roblox-Anticheat", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Pouca adoção; anti-cheat deve nascer da autoridade do servidor, não de módulo externo."),

# ---------------- COMBAT
dict(cat="combat", sub="framework", name="wad4444/WCS", lic="MIT", lic_ev="LICENSE.txt (clone) + wally.toml", rec=F, sec=AUD_OK + "; servidor valida dono do personagem/cooldown/requisitos; sem rate limit; params do cliente passam direto p/ Start()", notes="Melhor modelo conceitual (Skill, HoldableSkill, StatusEffect, Moveset, damage modifiers). Porém: fonte em TypeScript, pacote Wally 'cheetiedotpy/wcs' embute runtime Flamework+networking próprio+charm-sync (pilha de rede paralela), 1 commit em 12m. Usar como referência de design."),
dict(cat="combat", sub="framework", name="hatmatty/AMS", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=AUD_OK + " (rbxl extraído)", notes="Melee direcional (medieval), roblox-ts, último commit 2022-06."),
dict(cat="combat", sub="hitbox", name="TeamSwordphin/ShapecastHitbox", lic="MIT", lic_ev="LICENSE.md (clone) + wally.toml", rec=A, sec=AUD_OK, notes="Sucessor do RaycastHitbox: solvers Raycast/Blockcast/Spherecast/Attachment/Bone, 10/14 arquivos --!strict, sem dependências. Adaptar: loop central (1 conexão PostSimulation por hitbox hoje) e execução dentro de BindToSimulation. README sem docs."),
dict(cat="combat", sub="hitbox", name="Swordphin/raycastHitboxRbxl", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=AUD_OK, notes="RaycastHitboxV4; último commit 2021-09. Substituído pelo ShapecastHitbox."),
dict(cat="combat", sub="hitbox", name="Pyseph/ClientCast", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec="AUDITADO: atenção — servidor aceita RaycastResult reportado pelo cliente checando só dono/ID (sem validação geométrica); 1 conexão OnServerEvent por caster", notes="Último commit 2023-09."),
dict(cat="combat", sub="hitbox", name="CatSushi/MuchachoHitbox", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec="AUDITADO via extração do .rbxm (4 ModuleScripts): sem achados", notes="Código só em .rbxm (sem fonte texto no repo). Spatial queries + GoodSignal. Útil como referência de API."),
dict(cat="combat", sub="hitbox", name="HitboxClass v2 (DevForum)", src="devforum", url="https://devforum.roblox.com/t/hitboxclass-v20-a-powerful-oop-based-hitbox-module/3929512", lic="None", lic_ev="post: 'open source and free to use' sem licença", rec=X, sec=NA, notes=NOLIC + ". Distribuído só via Creator Store."),
dict(cat="combat", sub="lagcomp", name="michaelvqq/RollbackHitbox", lic="MIT", lic_ev="LICENSE (clone; adicionada 2026-07-09)", rec=A, sec=AUD_OK, notes="Buffer circular de hitboxes ~60Hz + OBB; foco hitscan. Autor admite: direção do tiro é confiada. Útil p/ habilidades à distância."),
dict(cat="combat", sub="lagcomp", name="text21/Rewind", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec="AUDITADO (fonte + 4 .rbxm): sem backdoor; inclui AbuseTracker com Kick/ban automático", notes=NOLIC + ". Post no DevForum marcado [Archived]."),
dict(cat="combat", sub="projectile", name="weenachuangkud/FastCast2", lic="MIT (código) + CC BY-NC-ND 4.0 (arte)", lic_ev="LICENSE-MIT + LICENSE-ART (clone)", rec=A, sec=AUD_OK, notes="Projéteis com Parallel Luau, muito ativo (1205 commits em 12m, 9 contributors). Arte/logos NÃO podem ser usados (NC-ND)."),
dict(cat="combat", sub="projectile", name="EtiTheSpirit/FastCastAPIDocs", lic="MPL-2.0", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="FastCast original, sem manutenção (push 2020)."),
dict(cat="combat", sub="projectile", name="1Axen/Secure-Cast", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=AUD_OK, notes="Projéteis server-authoritative; ARQUIVADO (último commit 2024-10)."),
dict(cat="combat", sub="projectile", name="synpixel/flashcast", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Biblioteca simples de projéteis; push 2024-04."),
dict(cat="combat", sub="projectile", name="noahrepublic/trojectile", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Experimento de replicação com timestamps."),
dict(cat="combat", sub="ragdoll", name="Brawldude2/RagdollService", lic="MIT", lic_ev="LICENSE (clone; alterada em 2026-03 — ecosyste.ms ainda mostra LGPL-3.0)", rec=A, sec=AUD_OK, notes="R6/R15/R15Legacy, 9/9 arquivos --!strict, 1 mantenedor. Verificar licença da versão exata adotada."),
dict(cat="combat", sub="statemachine", name="prooheckcp/RobloxStateMachine", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=AUD_OK, notes="FSM genérica (States/Transitions); último commit 2024-05. Estados de combate devem ser próprios e sincronizados via atributos em BindToSimulation."),
dict(cat="combat", sub="lockon", name="EzLockOn (DevForum)", src="devforum", url="https://devforum.roblox.com/t/ezlockon-fully-typed-optimized-lock-on-for-fighting-games/3150695", lic="None", lic_ev="post sem licença", rec=X, sec=NA, notes=NOLIC + ". Só cliente; via Creator Store."),
dict(cat="combat", sub="example", name="JoshuaIO/Fighting-Game-Framework-RobloxAPI", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec=NA, notes=NOLIC),
dict(cat="combat", sub="example", name="rinme/UntitledGame", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec=NA, notes=NOLIC),
dict(cat="combat", sub="example", name="galenamc/Roblox-CombatSystem", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec=NA, notes=NOLIC + " Último commit 2020."),
dict(cat="combat", sub="example", name="elomala/Fighting-game", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec=NA, notes=NOLIC),
dict(cat="combat", sub="example", name="aziz8235/roblox-luau-game-framework", lic="MIT", lic_ev="LICENSE (clone)", rec=X, sec="N/A — repositório sem código", notes="Aparece em buscas, mas o HEAD só tem README+LICENSE (0 arquivos Luau)."),
dict(cat="combat", sub="hitbox", name="RealHyperion/HitMesh-Pro", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec=NA, notes=NOLIC),
dict(cat="combat", sub="hitbox", name="CaidenSteele05/Attachment-Based-Raycast-Hit-Detection", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec=NA, notes=NOLIC),
dict(cat="combat", sub="example", name="dwmk/RobloxGames", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec="AUDITADO via extração (.rbxl): sem achados", notes="Backups de jogos (.rbxl) incl. battlegrounds inacabado; só referência."),
dict(cat="combat", sub="ai", name="idiomic/Roblox_Sword_Fighting_AI", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec=NA, notes=NOLIC + " (Q-learning, 2019)."),

# ---------------- MOVEMENT
dict(cat="movement", sub="controller", name="Roblox Character Controller Library (CCL)", src="roblox-official", url="https://create.roblox.com/docs/characters/character-controller-library", lic="Roblox Terms", lic_ev="DevForum full release 2026-04-08; beta 2026-09-10", rec=A, sec=OFF, notes="ControllerManager + AvatarAbilities em Luau (Walk/Run/Jump/Swim/Climb/Sit; Sprint/Crouch + Custom Abilities API em Studio Beta). Compatível c/ Server Authority. Carregado dinamicamente de asset (não vendorizável). NPCs 'coming soon'."),
dict(cat="movement", sub="controller", name="easy-games/chickynoid", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=AUD_OK + " (14 binários extraídos)", notes="Controller server-authoritative que substitui Humanoid; último commit 2024-01. Superado pelo Server Authority nativo; conflita com CCL/Animator."),
dict(cat="movement", sub="gravity", name="EgoMoose/rbx-wallstick", lic="MIT", lic_ev="LICENSE (clone)", rec=A, sec="AUDITADO: atenção — remote de replicação retransmite part/offset do cliente p/ todos sem validação/rate limit", notes="Andar em paredes/superfícies (14/14 --!strict). Opcional p/ habilidades de mobilidade especiais."),
dict(cat="movement", sub="gravity", name="EgoMoose/Rbx-Gravity-Controller", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Predecessor do wallstick; push 2022."),
dict(cat="movement", sub="gravity", name="EgoMoose/gravity-camera", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Câmera com 'up' customizado (acompanha wallstick)."),
dict(cat="movement", sub="gravity", name="KendallCole/RobloxGravityKit", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec=NA, notes=NOLIC),
dict(cat="movement", sub="melee", name="shmove/roblox-melee-movement-system", lic="Unlicense", lic_ev="LICENSE (clone)", rec=F, sec=NA, notes="Arquivado, WIP de 2023."),
dict(cat="movement", sub="parkour", name="MaxDevLol/Roblox-Parkour-System-by-max", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec="AUDITADO via extração (.rbxl, 134 scripts): sem achados de backdoor", notes="Só .rbxl; contém ~186 KeyframeSequences de proveniência não documentada — não reutilizar animações."),
dict(cat="movement", sub="parkour", name="Slubbie/slubbie", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec=NA, notes=NOLIC + " (momentum/wallrun/slide)."),
dict(cat="movement", sub="parkour", name="carlos123344222/robloxgame", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec=NA, notes=NOLIC + " (Dash/Slide/WallRun/Mantle)."),
dict(cat="movement", sub="dash", name="lewuat/Roblox-DashPlace", lic="Unlicense", lic_ev="LICENSE (clone)", rec=F, sec="AUDITADO via extração (.rbxl): sem achados", notes="Só .rbxl, 2 scripts."),
dict(cat="movement", sub="grapple", name="Ecliptorhizes/Hooksystem", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=NA, notes="Grapple duplo com física; pouca adoção."),
dict(cat="movement", sub="character", name="MaximumADHD/Character-Realism", lic="MPL-2.0", lic_ev="LICENSE (clone)", rec=A, sec="AUDITADO: remote valida tipo/NaN e faz clamp; sem rate limit (FireAllClients por evento)", notes="Look-angles/first person. MPL-2.0: modificações nos arquivos MPL devem ser publicadas; o README pede crédito ao criador."),
dict(cat="movement", sub="anime", name="Anime Movement System (DevForum)", src="devforum", url="https://devforum.roblox.com/t/anime-movement-system-open-source/1553138", lic="None", lic_ev="post sem licença", rec=X, sec=NA, notes=NOLIC + " Baseado em Knit; autor declarou abandonado."),

# ---------------- ABILITIES / STATUS
dict(cat="abilities-status-effects", sub="status", name="Opxourc/statusify", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=NA, notes="Status effects p/ Humanoid; criado em 2026; pouca adoção."),
dict(cat="abilities-status-effects", sub="status", name="WBlair1/StatusEffectManager", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=NA, notes="OOP server/client; lifetime máx. 30 s embutido; pouca adoção."),
dict(cat="abilities-status-effects", sub="status", name="Effectify (DevForum)", src="devforum", url="https://devforum.roblox.com/t/effectify-v131-a-customizable-status-effect-implementation/3635681", lic="None", lic_ev="post sem licença", rec=X, sec=NA, notes=NOLIC + " Bom modelo de stacking (Overwrite/Yield/Overlap) como ideia."),

# ---------------- NPC / AI
dict(cat="npc-ai", sub="pathfinding", name="Roblox PathfindingService", src="roblox-official", url="https://create.roblox.com/docs/characters/pathfinding", lic="Roblox Terms", lic_ev="API oficial", rec=R, sec=OFF, notes="Base de navegação (PathfindingModifiers/Links)."),
dict(cat="npc-ai", sub="pathfinding", name="grayzcale/simplepath", lic="MIT", lic_ev="LICENSE (clone)", rec=R, sec=AUD_OK, notes="Wrapper pequeno (453 LOC), 176 commits, 10 contributors, último commit 2026-06. Humanoid e não-humanoid."),
dict(cat="npc-ai", sub="bt", name="Defaultio/BehaviorTree3", lic="GPL-3.0", lic_ev="LICENSE (clone)", rec=X, sec=NA, notes="GPL-3.0 (copyleft forte) incompatível com código fechado comercial. Ideias (editor visual/blackboard) só como conceito."),
dict(cat="npc-ai", sub="bt", name="howmanysmall/behaviortree.rbxlua", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec=NA, notes=NOLIC + " (2018)."),
dict(cat="npc-ai", sub="bt", name="seyaidev/behaviortree.rbxlua", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec=NA, notes=NOLIC + " (2019)."),
dict(cat="npc-ai", sub="pathfinding", name="imezx/JPSPlus", lic="LGPL-3.0", lic_ev="ecosyste.ms", rec=X, sec=NA, notes="LGPL exige permitir relink/substituição da lib — impraticável num jogo Roblox."),
dict(cat="npc-ai", sub="pathfinding", name="kozuidev/PathForge", lic="None", lic_ev="sem LICENSE (clone)", rec=X, sec=NA, notes=NOLIC),
dict(cat="npc-ai", sub="ai", name="KURVOX/roblox-ai-npc", lic="MIT", lic_ev="LICENSE (clone)", rec=X, sec="N/A — repositório sem código", notes="HEAD só tem README+LICENSE (0 arquivos Luau)."),
dict(cat="npc-ai", sub="pathfinding", name="NoobPath (DevForum)", src="devforum", url="https://devforum.roblox.com/t/noobpath-easy-pathfinding/3254514", lic="None", lic_ev="post sem licença", rec=X, sec=NA, notes=NOLIC + " Creator Store."),

# ---------------- QUESTS
dict(cat="quests", sub="quest", name="prooheckcp/RoQuest", lic="Apache-2.0 (LICENSE) ≠ MIT (README)", lic_ev="LICENSE (clone) vs README", rec=A, sec=AUD_OK + "; cliente só lê dados (GetPlayerData/GetQuests); mutações só via API de servidor", notes="Quests, objetivos, cadeias (lifecycles), repetíveis, replicação p/ cliente; persistência agnóstica (Get/SetPlayerData). Beta, último commit 2025-05. Vendoriza Red/Promise/Signal/Trove. Confirmar licença com autor."),

# ---------------- INVENTORY / ITEMS / ECONOMY
dict(cat="inventory-items-economy", sub="inventory", name="Zyn-ic/Stoway", lic="MIT", lic_ev="LICENSE (clone)", rec=A, sec="AUDITADO: ACHADO CRÍTICO — Debug/ChatCommands registrado p/ TODO jogador sem checagem de permissão (/add item qtd, /clear, /set_limit...) no commit ed64b7e (2026-03-07); depende de 'acecateer/fusion' (escopo Wally não oficial)", notes="Boa base server-authoritative (operações validadas, lock por jogador, UUID por item, replicação delta, console). Remover debug e trocar Fusion antes de qualquer uso."),
dict(cat="inventory-items-economy", sub="inventory", name="Asiandayboy/InventoryMaker", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=AUD_OK, notes="Framework de UI de inventário (containers, drag, stack/split, filtros); 1 contributor."),
dict(cat="inventory-items-economy", sub="backpack", name="ryanlua/satchel", lic="MPL-2.0", lic_ev="LICENSE.md (clone)", rec=F, sec=AUD_OK, notes="Substituto do Backpack nativo (Tools). Só se o jogo usar Tools; Genesis terá inventário próprio."),
dict(cat="inventory-items-economy", sub="backpack", name="ryanlua/purse", lic="Apache-2.0", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Backpack padrão desacoplado do CoreGui."),
dict(cat="inventory-items-economy", sub="hotbar", name="ImAvafe/NeoHotbar", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=NA, notes="Hotbar customizável."),
dict(cat="inventory-items-economy", sub="inventory", name="lab2SecurityProjectsR/inventory-logic-NoGoodUi", lic="Proprietary", lic_ev="LICENSE: 'PROPRIETARY SOURCE CODE LICENSE - PORTFOLIO EVALUATION ONLY'", rec=X, sec=NA, notes="Licença proprietária; proibido reutilizar."),

# ---------------- PERSISTENCE
dict(cat="persistence", sub="data", name="anthony0br/DocumentService", lic="MIT", lic_ev="LICENSE (clone)", rec=R, sec=AUD_OK, notes="Session lock opcional, migrações, validação de schema, Result types, retries, cache imutável, sem dependências; 16/28 --!strict, 10 testes, 389 commits, 13 contributors, ativo (2026-09). README cita produção com 156K CCU (não verificado de forma independente)."),
dict(cat="persistence", sub="data", name="MadStudioRoblox/ProfileStore", lic="Apache-2.0", lic_ev="LICENSE (clone)", rec=R, sec=AUD_OK, notes="Sucessor do ProfileService (loleris); session locking, mock store. Sem migrações/validação de schema embutidas. Último commit 2025-07."),
dict(cat="persistence", sub="data", name="MadStudioRoblox/ProfileService", lic="Apache-2.0", lic_ev="ecosyste.ms", rec=X, sec=NA, notes="README do autor: 'FOR NEW PROJECTS - USE ProfileStore … This project is no longer supported'."),
dict(cat="persistence", sub="data", name="paradoxum-games/lyra", lic="MIT", lic_ev="LICENSE (clone)", rec=A, sec=AUD_OK, notes="Transações multi-jogador (trading anti-dupe), sharding, migrações, validação. README: 'early development ... avoid where data loss would be catastrophic'."),
dict(cat="persistence", sub="data", name="nezuo/lapis", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=AUD_OK, notes="Sem commits em 12m; README: 'not been battle-tested in a large production game'."),
dict(cat="persistence", sub="data", name="noahrepublic/DataKeep", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Alternativa Promise-based."),
dict(cat="persistence", sub="data", name="Kampfkarren/Roblox", lic="Custom", lic_ev="LICENSE (clone): licença própria", rec=F, sec=NA, notes="Contém DataStore2 (legado); licença customizada, último commit 2023-06."),
dict(cat="persistence", sub="data", name="Suphi's DataStore Module (DevForum)", src="devforum", url="https://devforum.roblox.com/t/suphis-datastore-module/2425597", lic="ISC-like (declarado no post)", lic_ev="texto no post DevForum", rec=F, sec=NA, notes="Session lock via MemoryStore; distribuído só via Creator Store (asset 11671168253)."),
dict(cat="persistence", sub="replication", name="MadStudioRoblox/Replica", lic="Apache-2.0", lic_ev="LICENSE (clone)", rec=F, sec=AUD_OK, notes="Replicação de estado servidor→cliente; alternativa ao charm-sync."),
dict(cat="persistence", sub="replication", name="MadStudioRoblox/ReplicaService", lic="Apache-2.0", lic_ev="ecosyste.ms", rec=X, sec=NA, notes="README do autor: 'FOR NEW PROJECTS - USE Replica … (This project is no longer supported)'."),

# ---------------- CHARACTER CUSTOMIZATION
dict(cat="character-customization", sub="avatar", name="Roblox HumanoidDescription / AvatarEditorService", src="roblox-official", url="https://create.roblox.com/docs/characters/appearance", lic="Roblox Terms", lic_ev="API oficial", rec=R, sec=OFF, notes="Aplicar corpo/escala/cores/acessórios/roupas; base do criador de personagem próprio."),
dict(cat="character-customization", sub="avatar", name="vocksel/Sugar", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=NA, notes="Utilitários (merge de HumanoidDescription); 2019."),

# ---------------- CAMERA
dict(cat="camera", sub="shake", name="Sleitnick/RbxCameraShaker", lic="MIT", lic_ev="LICENSE (clone)", rec=R, sec=AUD_OK, notes="Port do EZ Camera Shake; 478 LOC, estável (último commit 2019). Usar pelo escopo oficial ou vendorizar."),
dict(cat="camera", sub="spring", name="Fraktality/spr", lic="MIT", lic_ev="LICENSE (clone)", rec=R, sec=AUD_OK, notes="Springs para câmera/UI/VFX; arquivo único, 84 commits, último 2024-07."),
dict(cat="camera", sub="camera", name="LugicalDev/CameraService", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=NA, notes="Alternativa ao sistema de câmera padrão (visões customizadas)."),
dict(cat="camera", sub="camera", name="Yiannis123Git/ShiftUnlocked", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Câmera 3ª pessoa; push 2024-05. CCL está melhorando Shift-Lock nativo."),

# ---------------- ANIMATION
dict(cat="animation", sub="anim", name="wrello/Animations", lic="MIT", lic_ev="LICENSE (clone)", rec=A, sec=AUD_OK, notes="Preload/playback por rig, 171 commits. Adaptar ao Server Authority (não cachear AnimationTrack; usar Animator:GetTrackByAnimationId). Instalar via Wally, não via InsertService:LoadAsset."),
dict(cat="animation", sub="anim", name="evaera/roblox-animation-transfer", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=TOOL, notes="Arquivado; ferramenta de transferência de animações entre donos."),
dict(cat="animation", sub="anim", name="michaeldougal/AnimNation", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Utilitário de springs/tweens."),
dict(cat="animation", sub="anim", name="Khaomi/Animator", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Arquivado."),
dict(cat="animation", sub="anim", name="wes-BAN/crux-animation", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Push 2016; abandonado."),

# ---------------- VFX
dict(cat="vfx", sub="pool", name="Pyseph/ObjectCache", lic="MIT", lic_ev="LICENSE (clone)", rec=R, sec=AUD_OK, notes="Cache de Parts/Models (173 LOC, --!strict); sucessor prático do PartCache."),
dict(cat="vfx", sub="pool", name="PartCache (DevForum)", src="devforum", url="https://devforum.roblox.com/t/partcache-for-all-your-quick-part-creation-needs/246641", lic="None", lic_ev="post sem licença", rec=X, sec=NA, notes=NOLIC + " Usar ObjectCache."),
dict(cat="vfx", sub="emit", name="zilibobi/forge-vfx", lic="Custom (VFX-DL-1.1)", lic_ev="LICENSE (clone): só em jogos Roblox; derivados com mesma licença; uso comercial permitido", rec=A, sec=AUD_OK, notes="Módulo de emissão do plugin VFX Forge; licença custom exige revisão jurídica antes de adotar."),
dict(cat="vfx", sub="replication", name="wad4444/refx", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=AUD_OK, notes="Padrão 'nunca instanciar VFX no servidor' (proxy → clientes). roblox-ts; último commit 2024-12."),

# ---------------- UI
dict(cat="ui", sub="ui", name="centau/vide", lic="MIT", lic_ev="LICENSE (clone)", rec=R, sec=AUD_OK, notes="UI reativa leve; ativo (commit 2026-09-28), 25 contributors, testes."),
dict(cat="ui", sub="ui", name="dphfox/Fusion", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=AUD_OK + " (getfenv só em testes)", notes="Mais maduro (933 commits, 53 contributors, 98 arquivos --!strict, 49 testes); ritmo caiu (5 commits em 12m). Alternativa válida ao Vide."),
dict(cat="ui", sub="ui", name="jsdotlua/react-lua", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Tradução do React 17; pesado; último push 2025-05."),
dict(cat="ui", sub="ui", name="Roblox/roact", lic="Apache-2.0", lic_ev="ecosyste.ms", rec=X, sec=NA, notes="Arquivado."),
dict(cat="ui", sub="debug", name="SirMallard/Iris", lic="MIT", lic_ev="LICENSE (clone)", rec=R, sec=AUD_OK, notes="UI imediata p/ ferramentas de debug (somente builds de dev)."),
dict(cat="ui", sub="topbar", name="1ForeverHD/TopbarPlus", lic="MPL-2.0 + cláusula de crédito", lic_ev="LICENSE (clone): manter atributo ou creditar na descrição", rec=A, sec=AUD_OK, notes="Ícones de topbar; exige crédito."),
dict(cat="ui", sub="storybook", name="flipbook-labs/flipbook", lic="MIT", lic_ev="ecosyste.ms", rec=R, sec=TOOL, notes="Storybook de UI (plugin de dev)."),
dict(cat="ui", sub="storybook", name="PepeElToro41/ui-labs", lic="GPL-3.0", lic_ev="ecosyste.ms", rec=F, sec=TOOL, notes="Plugin GPL; ok como ferramenta, nunca incorporar código ao jogo."),
dict(cat="ui", sub="storybook", name="Kampfkarren/hoarcekat", lic="MPL-2.0", lic_ev="LICENSE.md (clone)", rec=F, sec=TOOL, notes="Storybook mais antigo."),
dict(cat="ui", sub="motion", name="littensy/ripple", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Motion p/ UI; spr cobre o caso."),
dict(cat="ui", sub="components", name="loneka/onyx-ui", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Componentes p/ Fusion."),
dict(cat="ui", sub="components", name="7kayoh/Lydie", lic="MIT (texto)", lic_ev="LICENSE (clone)", rec=F, sec=NA, notes="Componentes p/ Fusion."),
dict(cat="ui", sub="ui", name="ffrostfall/fluid", lic="MIT", lic_ev="ecosyste.ms", rec=F, sec=NA, notes="Framework declarativo recente."),

# ---------------- WORLD / MAP
dict(cat="world-map", sub="streaming", name="Roblox StreamingEnabled / Places / TeleportService", src="roblox-official", url="https://create.roblox.com/docs/workspace/streaming", lic="Roblox Terms", lic_ev="API oficial", rec=R, sec=OFF, notes="Streaming obrigatório sob Server Authority; reinos (Spiritual/Celestial/Abyss/Void) como places do mesmo universo via TeleportService."),
dict(cat="world-map", sub="zone", name="1ForeverHD/ZonePlus", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=AUD_OK, notes="Detecção de zonas; último commit 2024-02, sem --!strict. Preferir serviço de regiões próprio com spatial queries."),
dict(cat="world-map", sub="procedural", name="Gzeu/roblox-procedural-worlds", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec="AUDITADO: sem backdoor; escopo 'kitchen-sink' (produtos, teleports, anti-exploit com Kick, party, NPC dialogue)", notes="Gerador offline em Python + módulos Luau; 1 autor, criado em 2026. Referência p/ biomas/chunks/cavernas."),
dict(cat="world-map", sub="procedural", name="TheArturZh/RTerrainGenerator", lic="MIT", lic_ev="LICENSE (clone)", rec=F, sec=NA, notes="Heightmap com domain warping; 2020."),

# ---------------- PERFORMANCE (official)
dict(cat="performance", sub="parallel", name="Roblox Parallel Luau (Actors)", src="roblox-official", url="https://create.roblox.com/docs/scripting/multithreading", lic="Roblox Terms", lic_ev="API oficial", rec=R, sec=OFF, notes="Paralelizar IA/queries de NPCs em massa."),
]
