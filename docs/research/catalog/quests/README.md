# Seção E.2 — Quests

> Escopo: quests, objetivos, cadeias, recompensas (XP, moeda, itens), requisitos de nível e diálogo, persistência de estado, repetíveis, diárias, de chefe e ocultas.

## Veredito da categoria

Há **um** candidato sério: **RoQuest**. Ele cobre boa parte do modelo desejado, tem a fronteira de confiança correta e persistência agnóstica. É beta e tem uma divergência de licença a resolver.

---

### Projeto: prooheckcp/RoQuest
- **URL:** https://github.com/prooheckcp/RoQuest · docs: https://prooheckcp.github.io/RoQuest/ · DevForum: https://devforum.roblox.com/t/roquest-beta-an-abstract-quest-system/2971922
- **Licença:** ⚠️ o arquivo **LICENSE é Apache-2.0** e o **README diz MIT**. Tratar como Apache-2.0 (manter LICENSE/NOTICE) e pedir confirmação ao autor.
- **Maturidade:** 124 commits, 3 autores, 4 tags, último commit 2025-05-22, marcado como **Beta**. 13 arquivos `--!strict`.
- **Arquitetura:** `RoQuest/Server`, `RoQuest/Client`, `RoQuest/Shared` (classes `Quest`, `QuestObjective`, `ObjectiveInfo`, `QuestLifeCycle`; enums `QuestAcceptType`, `QuestDeliverType`, `QuestRepeatableType`, `QuestStatus`). Quests declaradas como ModuleScripts e carregadas com `LoadDirectory`.
- **API de servidor:** `Init`, `GiveQuest`, `CanGiveQuest`, `AddObjective`/`SetObjective`/`RemoveObjective`, `CompleteQuest`, `DeliverQuest`, `CancelQuest`, `MakeQuestAvailable`, `GetPlayerData`/`SetPlayerData`, sinais `OnQuestCompleted`/`OnQuestDelivered`/`OnQuestAvailable`/…
- **Segurança:** o cliente **só lê** (`GetPlayerData`, `GetQuests`, `GetAvailableQuests`, `GetUnAvailableQuests`). Todo progresso passa pela API de servidor ([auditoria](../../security-audits/prooheckcp__RoQuest.md)).
- **Pontos fortes:** repetição nativa (`QuestRepeatableType`: `NonRepeatable`, `Infinite`, `Daily`, `Weekly`, `Custom`), janelas de disponibilidade em UTC (`QuestStart`/`QuestEnd`, úteis para eventos), pré-requisitos (`RequiredQuests`), lifecycles por quest (hooks de início e fim), replicação automática para a UI, persistência plugável (`SetPlayerData` na carga, `GetPlayerData` no save).
- **Problemas:** beta, sem commits há mais de 12 meses. **Vendoriza Red** (networking, último push 2024-02), Promise, Signal e Trove, o que cria uma segunda pilha de rede. Recompensas ficam a cargo do integrador (bom para o Genesis). Não há conceito nativo de quest "oculta" nem de requisito de nível ou diálogo; os dois se implementam com disponibilidade condicionada (`MakeQuestAvailable`/`CanGiveQuest`) no adapter.
- **Compatibilidade:** 🛠️ **REQUIRES ADAPTATION**.
- **O que reutilizar:** o modelo de dados (Quest/Objective/Progress/Status) e a lógica de estados e disponibilidade.
- **O que reescrever:** a camada de rede (trocar o Red vendorizado por eventos Blink do projeto), a ligação dos objetivos a **eventos de domínio** (`EnemyKilled`, `ItemCollected`, `NpcTalkedTo`, `RegionEntered`) e a entrega de recompensas via `RewardService` único.
- **Integração (§25):** (1) consome eventos do `DomainEventBus` e escreve em `PlayerData.quests` via `DataService`; (2) Red/Promise/Signal/Trove vendorizados; (3) API de servidor acima; (4) assume que a persistência carrega e salva o `PlayerQuestData`; (5) conflito de rede com Blink; (6) estimativa: ~3–5 arquivos de adaptação; (7) é viável usar só `Shared/` + `Server/` e reescrever `Client/`.

## Alternativa: construir

Se a licença não for esclarecida ou o beta não evoluir, o modelo pedido no brief é simples de implementar como dados:

```text
QuestDefinition { id, npcId, requirements{level, questsDone, flags}, objectives[{type, target, count}],
                  rewards{xp, currency, items[]}, repeat{kind=none|daily|weekly, resetUtc}, hidden=bool }
QuestProgress   { questId, status, objectives{[id]=count}, acceptedAt, completedAt }  -- persistido
```

O motor faz três coisas: escuta eventos de domínio, atualiza o progresso e chama o `RewardService`, que é o único ponto que concede XP, moeda e itens.
