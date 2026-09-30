# Seção A — Executive Summary

> Pesquisa de 2026-09-29/30 · 168 candidatos catalogados · 49 repositórios clonados e auditados · 0 linhas de código de terceiros copiadas para este repositório.

## Números

| Métrica | Valor |
| --- | --- |
| Pistas brutas analisadas | 800+ (653 pacotes Wally únicos, ~150 entradas do gist-semente, ~35 buscas web, 3 listas curadas) |
| Candidatos catalogados ([CSV](data/catalog.csv)) | **168** (152 GitHub, 8 recursos oficiais Roblox, 8 posts DevForum/Creator Store) |
| ✅ READY TO INTEGRATE | **34** (13 são ferramentas de build; 8 são recursos oficiais da plataforma) |
| 🛠️ REQUIRES ADAPTATION | **16** |
| 📖 USE AS REFERENCE ONLY | **83** |
| ⛔ DO NOT USE | **35** (22 sem licença; outros: proprietário, GPL/LGPL, arquivado com sucessor, repositório vazio, desaconselhado pelo autor) |
| Repositórios auditados (grep + extração de binários + leitura de remotes) | **49** |
| Achados de segurança relevantes | 1 crítico (Stoway: comandos de debug abertos a todos os jogadores), 3 de atenção (ClientCast, Wallstick, Character-Realism) |
| Backdoors clássicos encontrados (`require(id)`, webhook, exfiltração HTTP, ofuscação) | **0**. A única chamada HTTP de saída é o comando admin `fetch` do Cmdr, bloqueado in-game sem hook `BeforeRun` |

## A mudança mais importante: a plataforma absorveu o "difícil"

Em 2026 a Roblox entregou oficialmente três peças que mudam a arquitetura do Genesis:

1. **Server Authority** (anúncio público em 2026-07-09): o servidor é a fonte da verdade, com predição e rollback no cliente e lógica em `RunService:BindToSimulation()`. Isso resolve na engine o dano autoritativo com resposta imediata que antes exigia Chickynoid, Rewind etc.
2. **Input Action System** (full release em junho de 2026): input cross-platform para PC, mobile e console. É obrigatório para inputs que afetam a simulação sob Server Authority.
3. **Character Controller Library** (full release em 2026-04-08; **Custom Abilities API** em beta desde 2026-09-10): locomoção em Luau, compatível com Server Authority e extensível.

**Consequência:** vários projetos comunitários populares de 2021–2024 (Chickynoid, frameworks com rede própria, lag compensation caseira) viraram **referência**, não dependência.

## Categorias com soluções maduras (reutilizar)

- **Tooling:** Rojo, Rokit, Wally, Selene, StyLua, luau-lsp, Lune, Jest-Lua, Asphalt, e o MCP embutido do Studio (integração oficial com Claude Code).
- **Rede:** Blink (IDL com validação gerada) + `t`.
- **Persistência:** DocumentService (principal), ProfileStore (alternativa), Lyra (transações, em avaliação).
- **UI e estado:** Vide + Charm/charm-sync; Iris para debug.
- **Utilitários:** RbxUtil (Signal, Trove…), ObjectCache (pooling), spr, RbxCameraShaker, Cmdr.
- **Pathfinding:** PathfindingService + SimplePath.

## Categorias com peças reutilizáveis, mas que exigem adaptação

- **Hitbox:** ShapecastHitbox (solvers bons; loop precisa ser centralizado).
- **Projéteis:** FastCast2 (código MIT; a arte é NC-ND).
- **Ragdoll:** RagdollService. **Lag comp. à distância:** RollbackHitbox.
- **Quests:** RoQuest (cobre repetíveis, cadeias e persistência plugável; **licença divergente** a confirmar e rede vendorizada).
- **Animação:** wrello/Animations (ajuste ao rollback). **VFX:** forge-vfx (licença custom).
- **Escala de NPC:** jecs (decidir com benchmark).

## Áreas **sem** bons sistemas reutilizáveis (construir do zero)

| Área | Por quê |
| --- | --- |
| Núcleo de combate (FSM de estados, combos com branching, block/guard break/parry/dodge, hitstun, knockback, pipeline de dano) | Nada licenciado e compatível com Server Authority. O WCS é o melhor modelo, mas é TS/Flamework com rede paralela. |
| Runtime de habilidades, status e **transformações** | Idem. Transformações: nenhum candidato encontrado. |
| Lock-on e câmera de combate | EzLockOn sem licença; o resto são scripts de exploit. |
| Movimento de mobilidade (dash, air dash, wall run, voo) | Projetos sem licença, só binário ou abandonados. A base CCL cobre locomoção. |
| IA de NPC (brain, percepção, LOD, chefes) | Behavior trees clássicas são GPL ou sem licença. |
| Inventário, itens, loot, trade | O único candidato forte (Stoway) tem achado crítico e dependência não oficial. |
| Sistema genético (Origin → Bloodline → Gene → Mutation → Potential) e criação de personagem | É identidade do jogo; só há APIs oficiais de aparência. |
| Regiões, reinos e mundo | Só APIs oficiais (Streaming, Places, Teleport). Não há mapas licenciados de qualidade. |
| Framework base (bootstrap) | Knit arquivado; sucessores imaturos ou em TS. Um bootstrap próprio é pequeno. |

## Recomendação em uma frase

Montar o Genesis sobre **Server Authority + IAS + CCL**, com **tooling e bibliotecas utilitárias maduras** (Rojo/Wally/Blink/Charm/Vide/DocumentService/SimplePath), **adaptar** hitbox, projéteis e ragdoll atrás de adapters, e **construir** o que é identidade e contrato central do jogo (combate, habilidades, transformações, genética, inventário, IA e mundo). O [mapa de integração](architecture/integration-map.md) define um dono por estado, uma fronteira de rede e eventos de domínio.

## Próximos passos

1. Aprovar a stack ([Seção G](architecture/recommended-stack.md)).
2. **Fase 1** do [plano](implementation-plan.md), com o spike de Server Authority como go/no-go.
3. Pedir confirmação de licença ao autor do RoQuest e revisão jurídica do forge-vfx e do TopbarPlus, se forem usados.
