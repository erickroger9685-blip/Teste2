# Genesis Realms: pesquisa de sistemas open-source Roblox/Luau

> Pesquisa técnica de 2026-09-29/30. Pergunta central: **"Quais partes do Genesis Realms já existem no ecossistema Roblox e podem ser reutilizadas legal, técnica e arquiteturalmente?"**
> Este diretório contém **só documentação e dados**. Nenhum código de terceiros foi copiado para o repositório, e nada do jogo foi implementado.

## Comece por aqui

1. [**Seção A: Executive Summary**](A-executive-summary.md)
2. [**Seção G: Stack recomendada**](architecture/recommended-stack.md)
3. [**Mapa de integração**](architecture/integration-map.md) (brief §25/§26)
4. [**Plano de implementação com Claude Code**](implementation-plan.md) (brief §29)

## Mapa do brief → arquivos

| Item do brief | Arquivo |
| --- | --- |
| Seção A: Executive Summary | [`A-executive-summary.md`](A-executive-summary.md) |
| Seção B: Master Table | [`B-master-table.md`](B-master-table.md) (gerada de [`data/catalog.csv`](data/catalog.csv)) |
| Seção C: Combat | [`catalog/combat/`](catalog/combat/README.md) |
| Seção D: Movement | [`catalog/movement/`](catalog/movement/README.md) |
| Seção E: NPC / Quest / Inventory / Persistence | [`catalog/npc-ai/`](catalog/npc-ai/README.md) · [`catalog/quests/`](catalog/quests/README.md) · [`catalog/inventory-items-economy/`](catalog/inventory-items-economy/README.md) · [`catalog/persistence/`](catalog/persistence/README.md) |
| Seção F: World / Assets (código × assets separados) | [`catalog/world-map/`](catalog/world-map/README.md) (**open source code**) · [`assets/`](assets/README.md) (**assets**) |
| Seção G: Arquitetura final | [`architecture/recommended-stack.md`](architecture/recommended-stack.md) |
| §21 Licenças | [`00-methodology/license-policy.md`](00-methodology/license-policy.md) |
| §22 Segurança | [`00-methodology/security-checklist.md`](00-methodology/security-checklist.md) · [`security-audits/`](security-audits/README.md) (49 auditorias) |
| §23/§24 Critérios e classificação | [`00-methodology/evaluation-criteria.md`](00-methodology/evaluation-criteria.md) |
| §25/§26 Anti-"colcha de retalhos" e integração | [`architecture/integration-map.md`](architecture/integration-map.md) |
| §28 Top candidates (critérios objetivos) | [`architecture/top-candidates.md`](architecture/top-candidates.md) |
| §29 Plano incremental (Claude Code) | [`implementation-plan.md`](implementation-plan.md) |
| Metodologia e limitações | [`00-methodology/methodology.md`](00-methodology/methodology.md) · [`data/search-log.md`](data/search-log.md) |
| Evidências brutas e scripts (reprodutibilidade) | [`data/evidence/`](data/evidence/) · [`tools/`](tools/README.md) |

## Catálogo por domínio (`catalog/`)

| Domínio | Brief | Veredito curto |
| --- | --- | --- |
| [tooling](catalog/tooling/README.md) | §19 | ✅ maduro: Rojo, Rokit, Wally, Selene, StyLua, luau-lsp, Lune, Jest-Lua, Blink, Asphalt, MCP do Studio |
| [core-frameworks](catalog/core-frameworks/README.md) | arquitetura | Bootstrap próprio + RbxUtil, Charm e Cmdr; Knit arquivado |
| [networking-security](catalog/networking-security/README.md) | §4/§22 | Server Authority + IAS (oficiais) + Blink + `t` |
| [combat](catalog/combat/README.md) | §4 | Construir o núcleo; adaptar ShapecastHitbox, FastCast2 e RagdollService |
| [movement](catalog/movement/README.md) | §5 | CCL oficial + abilities próprias |
| [abilities-status-effects](catalog/abilities-status-effects/README.md) | §6 | Construir (WCS como referência de design) |
| [transformations](catalog/transformations/README.md) | §7 | Construir (nenhum candidato) |
| [npc-ai](catalog/npc-ai/README.md) | §8 | SimplePath + brain próprio; jecs após benchmark |
| [quests](catalog/quests/README.md) | §9 | RoQuest adaptado (licença a confirmar) ou próprio |
| [inventory-items-economy](catalog/inventory-items-economy/README.md) | §10 | Construir (Stoway como referência; achado crítico) |
| [persistence](catalog/persistence/README.md) | §11 | DocumentService (ou ProfileStore) |
| [character-customization](catalog/character-customization/README.md) | §3/§12 | APIs oficiais + genética própria |
| [camera](catalog/camera/README.md) | §13 | CameraDirector próprio + spr + RbxCameraShaker |
| [animation](catalog/animation/README.md) | §14 | Animator oficial + wrello/Animations adaptado |
| [vfx](catalog/vfx/README.md) | §15 | ObjectCache + VfxPlayer próprio |
| [ui](catalog/ui/README.md) | §16 | Vide + Charm; Iris (debug) |
| [world-map](catalog/world-map/README.md) | §17 | APIs oficiais + RegionService próprio |
| [performance](catalog/performance/README.md) | §18 | ObjectCache, Trove, Parallel Luau, jecs (condicional) |

## Legenda de recomendação (§24)

✅ **READY TO INTEGRATE** · 🛠️ **REQUIRES ADAPTATION** · 📖 **USE AS REFERENCE ONLY** · ⛔ **DO NOT USE**. Sem licença explícita: **"NÃO CONFIRMADO — NÃO USAR ATÉ VERIFICAR"**.

## Como atualizar

- `data/catalog.csv` é a **fonte única de verdade**. É gerado por `tools/build_catalog.py` a partir de `tools/entries.py` (curadoria) e `data/evidence/`. `B-master-table.md` sai do mesmo script, e as fichas de `catalog/` resumem as decisões.
- Toda reavaliação precisa registrar a data em `verified_on` e repetir o [checklist de segurança](00-methodology/security-checklist.md) na nova versão.
- Stars e atividade são **fotografias**. Nunca tratar stars como sinal de qualidade.
