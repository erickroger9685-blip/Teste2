# Seção D — Movimento

> Escopo: movimento base, sprint, dash, air dash, dodge, slide, wall run/jump, double jump, ledge/mantle/climb, knockback movement, ragdoll, voo/hover e habilidades de mobilidade.

## Veredito da categoria

A base de movimento **mudou de dono em 2026**: a Roblox lançou o **Character Controller Library (CCL)**, que tira a lógica do Humanoid da "caixa-preta" da engine e a implementa em Luau. O CCL é compatível com o Server Authority e está recebendo uma **Custom Abilities API**. Os projetos comunitários de parkour e dash encontrados são, em sua maioria, **sem licença**, **só binário** ou **abandonados**.

**Decisão:** usar **CCL + Server Authority** como base de locomoção e implementar as habilidades de mobilidade do Genesis (dash, air dash, double jump, wall run, voo) como **abilities próprias**. No começo elas rodam no `MovementService` próprio. Quando a Custom Abilities API sair do beta, migram para ela.

---

### Projeto: Roblox Character Controller Library (oficial)
- **URL:** https://create.roblox.com/docs/characters/character-controller-library · anúncios: [full release](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) (2026-04-08), [Custom Abilities API — Studio Beta](https://devforum.roblox.com/t/studio-beta-expanding-the-character-controller-library-new-default-abilities-custom-abilities-api/4863739) (2026-09-10)
- **Licença:** Termos da Roblox (recurso da plataforma). O código Luau fica visível em `game.PlatformLibraries.rbx.AvatarAbilities`, mas é **carregado dinamicamente de um asset** e atualizado pela Roblox.
- **Arquitetura:** `ControllerManager` + biblioteca `AvatarAbilities`. Abilities padrão: Walk, Run, Jump, Swim, Climb, Sit; Sprint e Crouch em beta. Na API custom: ciclo de vida `OnSetup/OnStart/OnStop/OnUpdate/OnTeardown`, regras `StartsWhen/RunsWhile/Blocks/Stops`, `SyncedState` (predito no cliente e reconciliado no servidor), slots de ação ligados ao IAS (Press/Hold/Toggle/Repeat).
- **Pontos fortes:** oficial; alinhado com Server Authority (rollback) e IAS (PC, mobile e console); R6 e R15.
- **Problemas (declarados pela Roblox):** suporte a NPC "coming soon"; `Humanoid:MoveTo` não suportado; problemas de física listados (rampas, grudar em parede, jitter em escadas). Na beta de Custom Abilities: "não recomendado com Tools, Inventory/Backpack ou Health systems"; problemas de input no Mac; bindings que falham após respawn com Authority Automatic.
- **Compatibilidade:** 🛠️ **REQUIRES ADAPTATION**. Adotar a base agora e manter as abilities de mobilidade do Genesis atrás de uma interface própria (`IMovementAbility`), para trocar a implementação quando a API estabilizar.
- **O que reutilizar:** locomoção base, swim/climb, sprint/crouch, integração com IAS.
- **O que construir:** dash, air dash, dodge com i-frames, double jump, wall run/jump, ledge/mantle, voo/hover, knockback e launch, sempre como abilities com estado sincronizado.

### Projeto: easy-games/chickynoid
- **URL:** https://github.com/easy-games/chickynoid
- **Licença:** MIT
- **Arquitetura:** substitui o Humanoid por um controlador próprio, server-authoritative, com predição e rollback feitos à mão. Pacotes em `src/ServerScriptService/Packages/Chickynoid` e vários módulos em `Vendor/`.
- **Maturidade:** 399 commits, 17 autores; **último commit 2024-01-03**.
- **Problemas:** foi superado pelo Server Authority nativo; conflita com CCL, Animator e Humanoid; está inativo.
- **Compatibilidade:** 📖 **USE AS REFERENCE ONLY**. Serve para estudar predição, reconciliação e anti-speedhack.

### Projeto: EgoMoose/rbx-wallstick
- **URL:** https://github.com/EgoMoose/rbx-wallstick
- **Licença:** MIT · 14/14 arquivos `--!strict` · último commit 2026-06-04 · 1 autor
- **Recursos:** grudar o personagem em qualquer superfície (andar em paredes e tetos), com câmera acompanhando (`gravity-camera`).
- **Segurança:** o remote de replicação retransmite `part`/`offset` do cliente para todos sem validação nem rate limit (ver [auditoria](../../security-audits/EgoMoose__rbx-wallstick.md)).
- **Compatibilidade:** 🛠️ **REQUIRES ADAPTATION**. Opcional, só para habilidades especiais de mobilidade (andar em paredes). A replicação precisa ser refeita.

### Projeto: MaximumADHD/Character-Realism
- **URL:** https://github.com/MaximumADHD/Character-Realism · **Licença:** MPL-2.0
- **Recursos:** olhar da cabeça e do tronco para a câmera, corpo visível em primeira pessoa.
- **Segurança:** o remote valida tipo e NaN e faz clamp; não tem rate limit.
- **Compatibilidade:** 🛠️ **REQUIRES ADAPTATION** (opcional, polish). MPL-2.0 exige publicar modificações nos arquivos MPL.

---

## Movimento especializado: o que existe

| Necessidade | Candidatos | Licença | Decisão |
| --- | --- | --- | --- |
| Dash / dodge | lewuat/Roblox-DashPlace (só `.rbxl`, 2 scripts); módulos do DevForum | Unlicense / sem licença | **Construir** |
| Parkour (wall run, slide, mantle) | Slubbie/slubbie; carlos123344222/robloxgame | **sem licença** | ⛔; **construir** |
| Parkour completo | MaxDevLol/Roblox-Parkour-System-by-max (só `.rbxl`, 134 scripts, ~186 animações) | MIT (código); animações de proveniência não documentada | 📖 referência; não reutilizar animações |
| Melee movement | shmove/roblox-melee-movement-system | Unlicense, arquivado 2023 | 📖 |
| Grapple | Ecliptorhizes/Hooksystem | MIT, 2 stars | 📖 |
| Gravidade/paredes | EgoMoose wallstick / Gravity-Controller | MIT | 🛠️ / 📖 |
| Voo / hover | posts do DevForum (Flight System for RPGs, Universal Flying Script) | não verificados | **Construir** (AlignPosition/LinearVelocity sob Server Authority) |
| Climb / ledge | CCL Climb (escadas/treliças); posts do DevForum de ledge climb | oficial / não verificados | Base CCL + ledge próprio |
| Stamina | posts do DevForum | não verificados | **Construir** (recurso no `AbilityRuntime`) |
| Movimento "anime" | Anime Movement System (DevForum, baseado em Knit, abandonado) | sem licença | ⛔ |

## Regras para coexistência com o combate

1. Um único dono do estado do personagem, o `CharacterStateService`. Movimento e combate **pedem** transições; não escrevem estado diretamente.
2. Toda ability de movimento declara `Blocks`/`Stops` sobre estados de combate. Exemplo: dash bloqueado em hitstun e cancelado por stagger. É o mesmo modelo de regras do CCL.
3. Knockback é uma "ability imposta" pelo servidor (sem input), com a mesma rota de rollback.
4. Voo e hover mudam o `ControllerManager` para um controller de ar próprio. Não usar `BodyVelocity` legado.
