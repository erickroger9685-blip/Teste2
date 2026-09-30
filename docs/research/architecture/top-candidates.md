# Top candidates por categoria (brief §28)

> **Sem ranking geral nem notas arbitrárias.** Em cada categoria, o melhor candidato é indicado **em cada critério objetivo** (ver [critérios](../00-methodology/evaluation-criteria.md)), com a evidência medida em 2026-09-29/30. Quando nenhum candidato atende um critério, a célula traz "—".

Legenda dos critérios: **Arq** = compatibilidade arquitetural (Server Authority, IAS, uma pilha de rede) · **Mat** = maturidade · **Doc** = documentação · **Int** = menor esforço de integração · **Seg** = segurança · **Cob** = cobertura funcional.

## Combate: hitbox

| Critério | Melhor | Evidência |
| --- | --- | --- |
| Arq | ShapecastHitbox | sem rede própria; solvers puros adaptáveis a `BindToSimulation` |
| Mat | RaycastHitboxV4 | 26 commits, 6 autores, mais tempo em uso (porém 2021) |
| Doc | MuchachoHitbox | post do DevForum detalhado (o README do ShapecastHitbox está vazio) |
| Int | ShapecastHitbox | zero dependências, Wally oficial `teamswordphin/shapecasthitbox` |
| Seg | ShapecastHitbox / MuchachoHitbox | sem remotes; auditoria limpa (ClientCast confia no cliente) |
| Cob | ShapecastHitbox | raycast + blockcast + spherecast + attachment + bone |

## Combate: projéteis

| Critério | Melhor | Evidência |
| --- | --- | --- |
| Arq / Cob / Mat (atividade) | FastCast2 | Parallel Luau; 3 tipos de cast; 1.205 commits em 12m, 9 autores |
| Seg | Secure-Cast | desenhado server-authoritative, porém **arquivado** |
| Doc | FastCast2 | site de docs próprio |

## Combate: framework, skills e status

| Critério | Melhor | Evidência |
| --- | --- | --- |
| Cob / Doc / Mat | WCS | Skill/Holdable/Status/Moveset/damage; docs; 512 commits, 22 tags |
| Arq / Int | — (**construir**) | WCS traz Flamework + rede + charm-sync paralelos; nenhum runtime Luau compatível com Server Authority |
| Seg | WCS (como referência) | valida dono do personagem, cooldown e requisitos; sem rate limit |

## Movimento

| Critério | Melhor | Evidência |
| --- | --- | --- |
| Arq / Seg / Int | CCL (oficial) | compatível com Server Authority e IAS; mantido pela Roblox |
| Mat | Chickynoid | 399 commits, 17 autores (porém inativo desde 2024-01) |
| Cob (mobilidade especial) | — (**construir**) | projetos de parkour sem licença ou só `.rbxl` |

## Rede

| Critério | Melhor | Evidência |
| --- | --- | --- |
| Arq / Seg | Blink ≈ Zap | IDL com validação gerada; única fronteira |
| Mat (atividade 12m) | Blink | 42 commits contra 17 (Zap) e 0 (ByteNet) |
| Doc | Blink / Zap | ambos com site de docs ([blink](https://1axen.github.io/blink/), [zap](https://zap.redblox.dev)) |
| Int | Blink ≈ Zap | ambos são compiladores (CLI) instalados via Rokit; o código Luau gerado vai para o repositório, sem pacote de runtime a gerenciar. Blink é escrito em Luau (strict no projeto) e Zap em Rust |

## Persistência

| Critério | Melhor | Evidência |
| --- | --- | --- |
| Cob (§11) | DocumentService / Lyra | migrações + validação + lock (Lyra soma transações e sharding) |
| Mat | DocumentService | 389 commits, 13 autores, 21 tags, ativo; ProfileStore = legado mais usado |
| Seg (dados) | DocumentService | Result types, validação, retries; Lyra se declara early development |
| Int | ProfileStore | arquivo único, API mínima |
| Doc | DocumentService / Lyra | sites de docs |
| Arq | DocumentService | zero dependências |

## UI e estado

| Critério | Melhor | Evidência |
| --- | --- | --- |
| Mat / Doc | Fusion | 933 commits, 53 autores, 49 testes, docs extensos |
| Atividade / Arq (com Charm) | Vide | commit 2026-09-28; binding `vide-charm` |
| Int | Vide | leve; strict no projeto |

## NPC / IA

| Critério | Melhor | Evidência |
| --- | --- | --- |
| Pathfinding (todos os critérios) | SimplePath | MIT, 176 commits, 10 autores, CI, ativo |
| Behavior tree | — (**construir**) | BehaviorTree3 é GPL; as demais sem licença |
| Escala | jecs | 860 commits, 54 autores, 92 commits em 12m, testes |

## Quests / inventário

| Categoria | Critério | Melhor | Evidência |
| --- | --- | --- | --- |
| Quests | Cob / Seg / Arq | RoQuest | Daily/Weekly/Custom, `RequiredQuests`, cliente só lê; persistência plugável |
| Quests | Mat | RoQuest | único candidato (beta; 124 commits) |
| Inventário | Arq (padrões) | Stoway | operações validadas + lock; porém **debug aberto** (achado crítico) |
| Inventário | Seg | — (**construir**) | nenhum candidato seguro por padrão |

## Câmera / animação / VFX / pooling

| Categoria | Melhor | Evidência |
| --- | --- | --- |
| Shake | RbxCameraShaker | port do EZ Camera Shake; MIT; estável |
| Springs | spr | MIT; arquivo único; 84 commits |
| Animação | wrello/Animations | 171 commits, 15 tags, ativo em 2026 |
| Pooling | ObjectCache | MIT, `--!strict`, 173 linhas |
| Emissão de VFX | forge-vfx | ativo (138 commits em 12m), mas **licença custom** |

## Mundo

| Critério | Melhor | Evidência |
| --- | --- | --- |
| Todos | APIs oficiais (StreamingEnabled, Places, TeleportService) | nenhum framework comunitário maduro e licenciado |
| Referência procedural | Gzeu/roblox-procedural-worlds | MIT; biomas, FBM, cavernas, chunks (1 autor, 2026) |
