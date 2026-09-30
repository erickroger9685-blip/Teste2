# Auditoria — `Sleitnick/RbxUtil`

- **URL:** https://github.com/Sleitnick/RbxUtil
- **Commit auditado:** `31f9120fca02` (último commit 2026-07-27)
- **Licença (arquivo):** LICENSE.md → detectado: MIT
- **Escopo:** 69 arquivos Luau (16363 linhas), 16 com `--!strict` no arquivo, 14 arquivos de teste, 3 workflows de CI
- **Binários (.rbxm/.rbxl):** 0
- **Manifestos:** default.project.json, modules/buffer-util/package.json, modules/buffer-util/wally.toml, modules/comm/wally.toml, modules/component/wally.toml, modules/concur/wally.toml, modules/enum-list/wally.toml, modules/find/package.json, modules/find/wally.toml, modules/input/wally.toml, modules/loader/wally.toml, modules/log/wally.toml, modules/net/wally.toml, modules/option/wally.toml, modules/pid/package.json, modules/pid/wally.toml, modules/quaternion/package.json, modules/quaternion/wally.toml, modules/query/package.json, modules/query/wally.toml, modules/sequent/package.json, modules/sequent/wally.toml, modules/ser/wally.toml, modules/shake/package.json, modules/shake/wally.toml, modules/signal/package.json, modules/signal/wally.toml, modules/silo/wally.toml, modules/spring/package.json, modules/spring/wally.toml, modules/stream/package.json, modules/stream/wally.toml, modules/streamable/wally.toml, modules/symbol/wally.toml, modules/table-util/wally.toml, modules/task-queue/wally.toml, modules/timer/wally.toml, modules/tree/wally.toml, modules/trove/wally.toml, modules/typed-remote/wally.toml, modules/wait-for/wally.toml, package.json, rokit.toml, selene.toml, stylua.toml, test/wally.toml, tsconfig.json
- **Submódulos:** nenhum
- **Código vendorizado:** nenhum detectado
- **Data da auditoria:** 2026-09-29

## Dependências Wally declaradas

- `modules/comm/wally.toml`: `sleitnick/signal@2`, `sleitnick/option@1`, `evaera/promise@4`
- `modules/component/wally.toml`: `sleitnick/signal@^2`, `sleitnick/symbol@^2`, `sleitnick/trove@^1`, `evaera/promise@^4`

## Varredura automática (grep)

| Padrão | Risco | Ocorrências | Exemplos |
| --- | --- | ---: | --- |
| `require(<assetId>)` | carrega código remoto em runtime (vetor clássico de backdoor) | 0 | — |
| `getfenv`/`setfenv` | manipulação de ambiente; proibido em assets distribuídos pela Roblox | 0 | — |
| `loadstring` | execução de código dinâmico | 0 | — |
| `HttpService` | pode indicar tráfego externo; conferir método | 12 | `modules/log/init.luau:128`, `modules/log/init.luau:128`, `modules/log/init.luau:260` |
| `PostAsync`/`RequestAsync`/`GetAsync(url)` | requisição HTTP externa | 0 | — |
| `webhook`/`discord` | exfiltração para webhooks | 0 | — |
| `InsertService` | inserção de assets em runtime | 0 | — |
| `TeleportService` | teleporte de jogadores | 0 | — |
| `MarketplaceService` | prompts de compra ocultos | 0 | — |
| `:Kick(` | expulsão de jogadores | 0 | — |
| comparação com UserId fixo | admin/whitelist escondido | 0 | — |
| `string.char(n,n,n…)` | ofuscação | 0 | — |
| escapes `\ddd` longos | ofuscação | 0 | — |
| `OnServerEvent` | fronteira de confiança: revisar validação | 7 | `modules/comm/Server/RemoteSignal.luau:47`, `modules/comm/Server/RemoteSignal.luau:82`, `modules/net/init.luau:93` |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 13 | `modules/comm/Server/init.luau:62`, `modules/comm/Server/init.luau:73`, `modules/comm/Server/init.luau:73` |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** OK

- `HttpService` só para JSON em `modules/log`. Os handlers de `Comm`/`Net` são infraestrutura de rede genérica (não revisados linha a linha); validar payloads continua sendo responsabilidade do consumidor.

## Veredito de segurança

✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
