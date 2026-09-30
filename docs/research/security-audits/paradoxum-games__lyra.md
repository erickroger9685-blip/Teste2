# Auditoria — `paradoxum-games/lyra`

- **URL:** https://github.com/paradoxum-games/lyra
- **Commit auditado:** `e8927a9daa7c` (último commit 2026-03-25)
- **Licença (arquivo):** LICENSE → detectado: MIT
- **Escopo:** 44 arquivos Luau (14038 linhas), 0 com `--!strict` no arquivo + `.luaurc` languageMode=`strict` (vale p/ o projeto), 23 arquivos de teste, 2 workflows de CI
- **Binários (.rbxm/.rbxl):** 0
- **Manifestos:** .luaurc, .lune/.luaurc, default.project.json, rokit.toml, selene.toml, stylua.toml, test/Lyra/.luaurc, wally.toml
- **Submódulos:** nenhum
- **Código vendorizado:** nenhum detectado
- **Data da auditoria:** 2026-09-29

## Dependências Wally declaradas

- `wally.toml`: `evaera/promise@4.0.0`, `osyrisrblx/t@3.1.1`, `jsdotlua/jest@3.10.0`, `jsdotlua/jest-globals@3.10.0`

## Varredura automática (grep)

| Padrão | Risco | Ocorrências | Exemplos |
| --- | --- | ---: | --- |
| `require(<assetId>)` | carrega código remoto em runtime (vetor clássico de backdoor) | 0 | — |
| `getfenv`/`setfenv` | manipulação de ambiente; proibido em assets distribuídos pela Roblox | 0 | — |
| `loadstring` | execução de código dinâmico | 0 | — |
| `HttpService` | pode indicar tráfego externo; conferir método | 42 | `src/Files.luau:28`, `src/Files.luau:28`, `src/Files.luau:116` |
| `PostAsync`/`RequestAsync`/`GetAsync(url)` | requisição HTTP externa | 0 | — |
| `webhook`/`discord` | exfiltração para webhooks | 0 | — |
| `InsertService` | inserção de assets em runtime | 0 | — |
| `TeleportService` | teleporte de jogadores | 10 | `test/Lyra/__tests__/Simulation/sim.spec.luau:25`, `test/Lyra/__tests__/Simulation/sim.spec.luau:25`, `test/Lyra/__tests__/Simulation/sim.spec.luau:32` |
| `MarketplaceService` | prompts de compra ocultos | 1 | `src/Store.luau:1171` |
| `:Kick(` | expulsão de jogadores | 2 | `src/PlayerStore.luau:200`, `src/PlayerStore.luau:206` |
| comparação com UserId fixo | admin/whitelist escondido | 7 | `test/Lyra/__tests__/Simulation/basic.spec.luau:90`, `test/Lyra/__tests__/Simulation/basic.spec.luau:93`, `test/Lyra/__tests__/Simulation/basic.spec.luau:106` |
| `string.char(n,n,n…)` | ofuscação | 0 | — |
| escapes `\ddd` longos | ofuscação | 0 | — |
| `OnServerEvent` | fronteira de confiança: revisar validação | 0 | — |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 0 | — |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** OK

- `HttpService` só para JSON/GUID. Os `Kick` em `PlayerStore.luau:200/206` ficam no helper interno `_kickPlayer`, documentado como 'kick players when data errors occur'. `TeleportService` e as comparações de UserId aparecem só em `test/`.

## Veredito de segurança

✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
