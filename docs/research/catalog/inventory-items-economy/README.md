# Seção E.3 — Inventário, itens e economia

> Escopo: inventário, banco de itens, stack, equipamento (armas e armaduras), consumíveis, loot/drops, raridade, metadados, persistência e troca.

## Veredito da categoria

Não existe um sistema de inventário RPG maduro, com licença limpa e seguro por padrão. O mais próximo é o **Stoway**, que tem boa arquitetura server-authoritative, mas **um achado crítico de segurança** no commit auditado. O resto é UI (InventoryMaker, Satchel, NeoHotbar) ou está bloqueado por licença.

**Decisão:** **construir** o `ItemDatabase` (dados) e o `InventoryService` (servidor) sobre a camada de persistência escolhida. Estudar o Stoway como referência (validação por operação, lock por jogador, UUID por instância de item, replicação delta). Para **troca entre jogadores**, usar transações atômicas: avaliar `Lyra.txAsync` (ver [persistência](../persistence/README.md)) ou implementar escrow.

---

### Projeto: Zyn-ic/Stoway
- **URL:** https://github.com/Zyn-ic/Stoway · DevForum: https://devforum.roblox.com/t/stoway-modular-inventoryhotbar-system/4245330
- **Licença:** MIT · 73 commits (46 em 12 meses) · 2 autores · 6 tags · último commit 2026-03-07 · 0 arquivos `--!strict` · sem testes.
- **Arquitetura:** `src/server/StowayServerV1_2/` (Core: InventoryState, SlotManager, LimitChecker; Operations: Add/Remove/Swap/Equip/Drop; Replication: Actions/Replicator; World/ItemSpawner) e `src/client/StowayClientv1_2/` (store, drag, input, console mode, network). Um remote unificado `InventoryAction` com whitelist de operações.
- **Pontos fortes:** operações validadas no servidor; lock por jogador contra condições de corrida; UUID por item; peso e limites; suporte a console e gamepad; replicação delta com correção.
- **Problemas:**
  - 🔴 **CRÍTICO:** o `Debug/ChatCommands` é registrado **para todo jogador** sem checagem (`init.luau:64`). `/add <item> <qtd>` cria itens arbitrários em produção ([auditoria](../../security-audits/Zyn-ic__Stoway.md)).
  - Depende de `acecateer/fusion@0.3.1`, que **não é o escopo oficial do Fusion**.
  - Não tem persistência própria (é preciso ligar ao DataService), nem tipagem estrita, nem testes.
- **Compatibilidade:** 🛠️ **REQUIRES ADAPTATION** (na prática, **referência**, a menos que se faça fork, se remova o debug e se troque a UI pelo stack do projeto).
- **O que reutilizar:** o padrão de operações (`OperationHandlers` + lock + reenvio de estado em erro) e o modelo de slot e hotbar.
- **O que reescrever:** UI (Vide), rede (Blink), persistência (DocumentService), remoção de todo debug, tipagem estrita.

### Outros candidatos

| Projeto | Licença | Tipo | Decisão |
| --- | --- | --- | --- |
| Asiandayboy/InventoryMaker | MIT | Framework de **UI** de inventário (containers, drag, stack/split, filtros, busca, ordenação); 1 autor, 61 commits | 📖 referência de UX |
| ryanlua/satchel | MPL-2.0 | Substituto do Backpack nativo (Tools); muito ativo (1.020 commits) | 📖 só se o jogo usar Tools |
| ryanlua/purse | Apache-2.0 | Backpack padrão desacoplado do CoreGui | 📖 |
| ImAvafe/NeoHotbar | MIT | Hotbar | 📖 |
| lab2SecurityProjectsR/inventory-logic-NoGoodUi | **Proprietária** ("PORTFOLIO EVALUATION ONLY") | Inventário server-authoritative | ⛔ |
| LootPlan (DevForum, dogwarrior24) | não verificada | Tabelas de loot | pista não verificada |
| Pacotes Wally de loot/weighted random (`meowtsun/lootset`, `xsyrei/weighted-loot`…) | não verificados | — | pistas |

## Modelo recomendado (construir)

```text
ItemDefinition (dados, versionado)   { id, kind=weapon|armor|consumable|material|key, rarity, stackMax,
                                       stats{}, equipSlot?, abilityGrants[], transformReqs?, tags[] }
ItemInstance (persistido)            { uuid, defId, qty, rolls{}, boundTo?, createdAt, source }
Inventory (persistido)               { slots[], equipment{}, currency{}, capacity }

Regras:
- Só o servidor cria ItemInstance (RewardService, LootService, CraftService, Shop).
- Rolls (raridade, atributos) usam o RNG do servidor com semente auditável; o resultado fica no uuid.
- Operações idempotentes com id de operação, para evitar duplicação com retry.
- Trading = transação atômica sobre dois documentos (Lyra txAsync) ou escrow com estados.
```
