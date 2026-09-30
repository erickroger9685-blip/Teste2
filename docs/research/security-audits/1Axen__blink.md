# Auditoria — `1Axen/blink`

- **URL:** https://github.com/1Axen/blink
- **Commit auditado:** `86b04ef50101` (último commit 2026-09-19)
- **Licença (arquivo):** LICENSE → detectado: MIT
- **Escopo:** 52 arquivos Luau (10517 linhas), 12 com `--!strict` no arquivo + `.luaurc` languageMode=`strict` (vale p/ o projeto), 4 arquivos de teste, 2 workflows de CI
- **Binários (.rbxm/.rbxl):** 2 — scripts extraídos com parser próprio e submetidos ao mesmo grep
- **Manifestos:** .luaurc, benchmark/default.project.json, default.project.json, docs/package.json, docs/tsconfig.json, pesde.toml, plugin/default.project.json, rokit.toml, stylua.toml
- **Submódulos:** nenhum
- **Código vendorizado:** nenhum detectado
- **Data da auditoria:** 2026-09-29

## Dependências Wally declaradas

- nenhuma declarada

## Varredura automática (grep)

| Padrão | Risco | Ocorrências | Exemplos |
| --- | --- | ---: | --- |
| `require(<assetId>)` | carrega código remoto em runtime (vetor clássico de backdoor) | 0 | — |
| `getfenv`/`setfenv` | manipulação de ambiente; proibido em assets distribuídos pela Roblox | 0 | — |
| `loadstring` | execução de código dinâmico | 0 | — |
| `HttpService` | pode indicar tráfego externo; conferir método | 5 | `benchmark/src/client/init.client.luau:4`, `benchmark/src/client/init.client.luau:4`, `benchmark/src/client/init.client.luau:159` |
| `PostAsync`/`RequestAsync`/`GetAsync(url)` | requisição HTTP externa | 0 | — |
| `webhook`/`discord` | exfiltração para webhooks | 0 | — |
| `InsertService` | inserção de assets em runtime | 0 | — |
| `TeleportService` | teleporte de jogadores | 0 | — |
| `MarketplaceService` | prompts de compra ocultos | 0 | — |
| `:Kick(` | expulsão de jogadores | 0 | — |
| comparação com UserId fixo | admin/whitelist escondido | 0 | — |
| `string.char(n,n,n…)` | ofuscação | 0 | — |
| escapes `\ddd` longos | ofuscação | 0 | — |
| `OnServerEvent` | fronteira de confiança: revisar validação | 6 | `benchmark/src/server/init.server.luau:79`, `benchmark/src/server/init.server.luau:92`, `src/Generator/init.luau:1217` |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 1 | `benchmark/src/server/init.server.luau:88` |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** OK

- Sem revisão manual linha a linha além da varredura. Os handlers de rede apontados na tabela devem ser revisados antes da integração.

## Veredito de segurança

✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
