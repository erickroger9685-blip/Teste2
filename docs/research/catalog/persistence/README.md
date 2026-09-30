# Seção E.4 — Persistência e dados

> Escopo: DataStore, perfis de jogador, versionamento de schema, migrações, autosave, session locking, rollback, validação e serialização. **O cliente nunca é fonte de verdade** para dinheiro, XP, nível, itens, raridade, dano, recompensas ou rolls.

## Veredito da categoria

É a categoria **mais madura** do ecossistema. Há três bibliotecas com licença limpa e auditoria sem achados. Elas diferem em **migrações/validação** (essenciais para o brief §11) e em **transações** (essenciais para troca).

| Critério (§11) | DocumentService | ProfileStore | Lyra | Lapis |
| --- | --- | --- | --- | --- |
| Licença | MIT | Apache-2.0 | MIT | MIT |
| Session locking | ✅ (opcional por documento) | ✅ | ✅ | ✅ |
| Migrações de schema | ✅ | ❌ (manual) | ✅ | ✅ |
| Validação de dados | ✅ (runtime + tipos) | ❌ (template/reconcile) | ✅ (`t`) | ✅ |
| Transações multi-chave | ❌ (objetivo futuro no README) | ❌ | ✅ (`txAsync`) | ❌ |
| Sharding de dados grandes | ❌ | ❌ | ✅ | ❌ |
| Tipagem estrita | 16/28 arquivos `--!strict` | 0/2 | strict no projeto inteiro (`.luaurc`) | 1/23 |
| Testes (arquivos) | 10 | 0 | 23 | 7 |
| Commits / autores | 389 / 13 | 32 / 5 | 552 / 8 | 198 / 5 |
| Último commit | 2026-09-07 | 2025-07-31 | 2026-03-25 | 2025-02-11 |
| Aviso do autor | README cita produção com 156K CCU | — | **"early development… avoid where data loss would be catastrophic"** | **"not battle-tested in a large production game"** |
| Dependências de runtime (wally.toml) | nenhuma | nenhuma | `evaera/promise`, `osyrisrblx/t` | `evaera/promise` |

(Dados medidos nos clones em 2026-09-29. As declarações de uso em produção são dos próprios READMEs e não foram verificadas de forma independente.)

**Decisão:** ✅ **DocumentService** como biblioteca principal: migrações, validação, tipagem estrita, testes, atividade recente, sem dependências. ✅ **ProfileStore** é a alternativa conservadora (mais usada historicamente, mínima) caso o time prefira. Nesse caso, migrações e validação ficam no `DataService` próprio. 🛠️ **Lyra** fica em avaliação só para **transações de troca**, depois de passar em testes de carga, ou então usa-se escrow com DocumentService.

---

### Projeto: anthony0br/DocumentService
- **URL:** https://github.com/anthony0br/DocumentService · docs: https://anthony0br.github.io/DocumentService/docs/intro
- **Licença:** MIT
- **Arquitetura:** `DocumentStore` + `Document` com `Result` types (erros explícitos), cache imutável, hooks e sinais antes e depois das operações, retries com backoff exponencial, BindToClose, injeção de DataStore (mock), checagem de compatibilidade JSON.
- **Pontos fortes:** atende quase todo o §11 (migrações, validação, session lock, autosave, retries); sem dependências; build via darklua/rojo.
- **Problemas:** sem transações multi-documento; API única para documentos com e sem lock (o autor planeja separar).
- **Compatibilidade:** ✅ **READY TO INTEGRATE**, atrás de `DataService`.
- **Integração (§25):** `DataService` (próprio) é o **único** módulo que importa DocumentService. Os outros serviços leem e escrevem pelo `DataService` (`GetProfile`, `Update(fn)`). Migrações ficam versionadas em `src/server/Data/Migrations/`. Schema validado com `t`.

### Projeto: MadStudioRoblox/ProfileStore
- **URL:** https://github.com/MadStudioRoblox/ProfileStore · **Licença:** Apache-2.0
- **Arquitetura:** um arquivo (~3k linhas). `ProfileStore.New(name, template)`, `:StartSessionAsync(key)`, `Profile.Data`, `:Reconcile()`, `.Mock`, sinais `OnError`/`OnOverwrite`/`OnCriticalToggle`.
- **Pontos fortes:** sucessor do ProfileService (padrão de fato por anos); simples.
- **Problemas:** sem migrações nem validação; último commit 2025-07-31; pacote oficial Wally sob `lm-loleris/profilestore`, com **24 escopos de terceiros** publicando pacotes homônimos.
- **Compatibilidade:** ✅ **READY TO INTEGRATE** (alternativa).

### Projeto: paradoxum-games/lyra
- **URL:** https://github.com/paradoxum-games/lyra · docs: https://paradoxum-games.github.io/lyra/ · **Licença:** MIT
- **Recursos:** `createPlayerStore`, `loadAsync`/`unloadAsync`, `updateAsync`, **`txAsync({p1,p2}, fn)`** atômico, sharding automático, migrações, validação (`t`).
- **Compatibilidade:** 🛠️ **REQUIRES ADAPTATION / avaliação**: o próprio README desaconselha uso onde perda de dados seria catastrófica.

## Replicação de estado para o cliente

| Projeto | Licença | Decisão |
| --- | --- | --- |
| littensy/charm + **charm-sync** | MIT | ✅ escolhido (estado atômico no cliente, sincronizado por patches; combina com Vide) |
| MadStudioRoblox/Replica | Apache-2.0 | 📖 alternativa |
| MadStudioRoblox/ReplicaService | Apache-2.0 | ⛔ legado (substituído pelo Replica) |

## Outros

`nezuo/lapis` (📖), `noahrepublic/DataKeep` (📖), `Kampfkarren/Roblox` (DataStore2, licença custom, legado, 📖), Suphi's DataStore Module (licença ISC-like no post, só Creator Store, 📖), `MadStudioRoblox/ProfileService` (⛔ legado).

## Regras de segurança de dados (valem para qualquer biblioteca)

1. Os remotes **nunca** recebem valores de moeda, XP, item ou roll. Recebem **intenções** (ex.: "usar item uuid X"), que o servidor valida.
2. Toda mutação passa por `DataService.Update(player, reason, fn)`, com `reason` registrado (auditoria e rollback).
3. Versão de schema no documento e migrações puras e testadas (Lune + Jest-Lua com DataStore mock).
4. Rollback: backups periódicos (versões do DataStore) e ferramenta de admin (Cmdr) com permissão restrita.
