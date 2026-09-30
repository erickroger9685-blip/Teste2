# Auditoria — `nezuo/lapis`

- **URL:** https://github.com/nezuo/lapis
- **Commit auditado:** `e217a2244f9c` (último commit 2025-02-11)
- **Licença (arquivo):** LICENSE → detectado: MIT
- **Escopo:** 23 arquivos Luau (3559 linhas), 1 com `--!strict` no arquivo, 7 arquivos de teste, 0 workflows de CI
- **Binários (.rbxm/.rbxl):** 0
- **Manifestos:** default.project.json, examples/developer-product-handling/default.project.json, examples/developer-product-handling/test/default.project.json, examples/developer-product-handling/test/wally.toml, examples/developer-product-handling/wally.toml, examples/player-data/default.project.json, examples/player-data/wally.toml, selene.toml, test/default.project.json, wally.toml
- **Submódulos:** nenhum
- **Código vendorizado:** nenhum detectado
- **Data da auditoria:** 2026-09-29

## Dependências Wally declaradas

- `examples/developer-product-handling/test/wally.toml`: `nezuo/midori@0.1.3`, `evaera/promise@4.0.0`, `csqrl/sift@0.0.8`, `osyrisrblx/t@3.0.0`, `nezuo/data-store-service-mock@0.3.5`
- `examples/developer-product-handling/wally.toml`: `evaera/promise@4.0.0`, `csqrl/sift@0.0.8`, `osyrisrblx/t@3.0.0`
- `examples/player-data/wally.toml`: `osyrisrblx/t@3.0.0`, `evaera/promise@4.0.0`

## Varredura automática (grep)

| Padrão | Risco | Ocorrências | Exemplos |
| --- | --- | ---: | --- |
| `require(<assetId>)` | carrega código remoto em runtime (vetor clássico de backdoor) | 0 | — |
| `getfenv`/`setfenv` | manipulação de ambiente; proibido em assets distribuídos pela Roblox | 0 | — |
| `loadstring` | execução de código dinâmico | 0 | — |
| `HttpService` | pode indicar tráfego externo; conferir método | 3 | `src/Collection.luau:1`, `src/Collection.luau:1`, `src/Collection.luau:65` |
| `PostAsync`/`RequestAsync`/`GetAsync(url)` | requisição HTTP externa | 0 | — |
| `webhook`/`discord` | exfiltração para webhooks | 0 | — |
| `InsertService` | inserção de assets em runtime | 0 | — |
| `TeleportService` | teleporte de jogadores | 0 | — |
| `MarketplaceService` | prompts de compra ocultos | 13 | `examples/developer-product-handling/src/server/init.server.luau:1`, `examples/developer-product-handling/src/server/init.server.luau:1`, `examples/developer-product-handling/src/server/init.server.luau:107` |
| `:Kick(` | expulsão de jogadores | 2 | `examples/developer-product-handling/src/server/init.server.luau:40`, `examples/player-data/src/server/init.server.luau:36` |
| comparação com UserId fixo | admin/whitelist escondido | 0 | — |
| `string.char(n,n,n…)` | ofuscação | 0 | — |
| escapes `\ddd` longos | ofuscação | 0 | — |
| `OnServerEvent` | fronteira de confiança: revisar validação | 0 | — |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 0 | — |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** OK

- `MarketplaceService`/`Kick` aparecem só em `examples/`.

## Veredito de segurança

✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
