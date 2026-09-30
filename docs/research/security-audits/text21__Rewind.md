# Auditoria — `text21/Rewind`

- **URL:** https://github.com/text21/Rewind
- **Commit auditado:** `1bb0703f20d3` (último commit 2026-01-09)
- **Licença (arquivo):** NENHUM → detectado: NÃO IDENTIFICADO
- **Escopo:** 623 arquivos Luau (51511 linhas), 35 com `--!strict` no arquivo, 73 arquivos de teste, 1 workflows de CI
- **Binários (.rbxm/.rbxl):** 4 — scripts extraídos com parser próprio e submetidos ao mesmo grep
- **Manifestos:** DevPackages/_Index/roblox_testez@0.4.1/testez/.gitmodules, DevPackages/_Index/roblox_testez@0.4.1/testez/default.project.json, DevPackages/_Index/roblox_testez@0.4.1/testez/foreman.toml, DevPackages/_Index/roblox_testez@0.4.1/testez/wally.toml, DevPackages/_Index/sirmallard_iris@2.5.0/iris/default.project.json, DevPackages/_Index/sirmallard_iris@2.5.0/iris/wally.toml, Packages/_Index/evaera_promise@4.0.0/promise/aftman.toml, Packages/_Index/evaera_promise@4.0.0/promise/default.project.json, Packages/_Index/evaera_promise@4.0.0/promise/foreman.toml, Packages/_Index/evaera_promise@4.0.0/promise/modules/testez/.gitmodules, Packages/_Index/evaera_promise@4.0.0/promise/modules/testez/default.project.json, Packages/_Index/evaera_promise@4.0.0/promise/modules/testez/foreman.toml, Packages/_Index/evaera_promise@4.0.0/promise/selene.toml, Packages/_Index/evaera_promise@4.0.0/promise/wally.toml, Packages/_Index/osyrisrblx_t@3.1.1/t/.luaurc, Packages/_Index/osyrisrblx_t@3.1.1/t/default.project.json, Packages/_Index/osyrisrblx_t@3.1.1/t/wally.toml, Packages/_Index/sleitnick_signal@2.0.3/signal/wally.toml, Packages/_Index/sleitnick_table-util@1.2.1/table-util/wally.toml, Packages/_Index/sleitnick_trove@1.8.0/trove/wally.toml, default.project.json, docs/package.json, selene.toml, wally.toml
- **Submódulos:** nenhum
- **Código vendorizado:** DevPackages/_Index DevPackages/iris.lua DevPackages/testez.lua Packages/_Index Packages/promise.lua Packages/signal.lua Packages/t.lua Packages/table-util.lua
- **Data da auditoria:** 2026-09-29

## Dependências Wally declaradas

- nenhuma declarada

## Varredura automática (grep)

| Padrão | Risco | Ocorrências | Exemplos |
| --- | --- | ---: | --- |
| `require(<assetId>)` | carrega código remoto em runtime (vetor clássico de backdoor) | 0 | — |
| `getfenv`/`setfenv` | manipulação de ambiente; proibido em assets distribuídos pela Roblox | 16 | `DevPackages/_Index/roblox_testez@0.4.1/testez/modules/lemur/lib/Habitat.lua:123`, `DevPackages/_Index/roblox_testez@0.4.1/testez/modules/lemur/lib/baste.lua:186`, `DevPackages/_Index/roblox_testez@0.4.1/testez/src/TestPlan.lua:192` |
| `loadstring` | execução de código dinâmico | 4 | `DevPackages/_Index/roblox_testez@0.4.1/testez/modules/lemur/lib/Habitat.lua:120`, `DevPackages/_Index/roblox_testez@0.4.1/testez/modules/lemur/lib/baste.lua:179`, `Packages/_Index/evaera_promise@4.0.0/promise/modules/testez/modules/lemur/lib/Habitat.lua:120` |
| `HttpService` | pode indicar tráfego externo; conferir método | 54 | `DevPackages/_Index/roblox_testez@0.4.1/testez/modules/lemur/lib/instances/Game.lua:11`, `DevPackages/_Index/roblox_testez@0.4.1/testez/modules/lemur/lib/instances/Game.lua:11`, `DevPackages/_Index/roblox_testez@0.4.1/testez/modules/lemur/lib/instances/Game.lua:42` |
| `PostAsync`/`RequestAsync`/`GetAsync(url)` | requisição HTTP externa | 0 | — |
| `webhook`/`discord` | exfiltração para webhooks | 0 | — |
| `InsertService` | inserção de assets em runtime | 20 | `DevPackages/_Index/roblox_testez@0.4.1/testez/modules/lemur/lib/instances/Game.lua:12`, `DevPackages/_Index/roblox_testez@0.4.1/testez/modules/lemur/lib/instances/Game.lua:12`, `DevPackages/_Index/roblox_testez@0.4.1/testez/modules/lemur/lib/instances/Game.lua:43` |
| `TeleportService` | teleporte de jogadores | 0 | — |
| `MarketplaceService` | prompts de compra ocultos | 28 | `DevPackages/_Index/roblox_testez@0.4.1/testez/modules/lemur/lib/instances/Game.lua:15`, `DevPackages/_Index/roblox_testez@0.4.1/testez/modules/lemur/lib/instances/Game.lua:15`, `DevPackages/_Index/roblox_testez@0.4.1/testez/modules/lemur/lib/instances/Game.lua:45` |
| `:Kick(` | expulsão de jogadores | 3 | `src/shared/Rewind/Server/AbuseTracker.lua:318`, `src/shared/Rewind/Server/AbuseTracker.lua:418`, `src/shared/Rewind/Server/AbuseTracker.lua:479` |
| comparação com UserId fixo | admin/whitelist escondido | 0 | — |
| `string.char(n,n,n…)` | ofuscação | 0 | — |
| escapes `\ddd` longos | ofuscação | 0 | — |
| `OnServerEvent` | fronteira de confiança: revisar validação | 2 | `src/shared/Rewind/Replication/init.lua:95`, `src/shared/Rewind/Server/Server.lua:877` |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 1 | `src/shared/Rewind/ClockSync/Server.lua:28` |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** OK (mas sem licença)

- Fonte e 4 builds `.rbxm` foram extraídos. `getfenv`/`loadstring` aparecem só no TestEZ/lemur vendorizado. `AbuseTracker.lua` faz Kick/ban automático por heurística, o que exige revisão de falsos positivos.
- **Sem arquivo de licença**, portanto não pode ser usado.

## Veredito de segurança

⛔ Bloqueado por licença

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
