# Auditoria — `evaera/Cmdr`

- **URL:** https://github.com/evaera/Cmdr
- **Commit auditado:** `338c0e9a28b4` (último commit 2026-09-29)
- **Licença (arquivo):** LICENSE → detectado: MIT
- **Escopo:** 86 arquivos Luau (7258 linhas), 0 com `--!strict` no arquivo, 0 arquivos de teste, 3 workflows de CI
- **Binários (.rbxm/.rbxl):** 0
- **Manifestos:** default.project.json, package.json, rokit.toml, selene.toml, stylua.toml, wally.toml
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
| `HttpService` | pode indicar tráfego externo; conferir método | 12 | `Cmdr/BuiltInCommands/Debug/fetchServer.luau:1`, `Cmdr/BuiltInCommands/Debug/fetchServer.luau:1`, `Cmdr/BuiltInCommands/Debug/fetchServer.luau:4` |
| `PostAsync`/`RequestAsync`/`GetAsync(url)` | requisição HTTP externa | 1 | `Cmdr/BuiltInCommands/Debug/fetchServer.luau:4` |
| `webhook`/`discord` | exfiltração para webhooks | 0 | — |
| `InsertService` | inserção de assets em runtime | 0 | — |
| `TeleportService` | teleporte de jogadores | 12 | `Cmdr/BuiltInCommands/Admin/gotoPlaceServer.luau:1`, `Cmdr/BuiltInCommands/Admin/gotoPlaceServer.luau:1`, `Cmdr/BuiltInCommands/Admin/gotoPlaceServer.luau:10` |
| `MarketplaceService` | prompts de compra ocultos | 0 | — |
| `:Kick(` | expulsão de jogadores | 1 | `Cmdr/BuiltInCommands/Admin/kickServer.luau:23` |
| comparação com UserId fixo | admin/whitelist escondido | 0 | — |
| `string.char(n,n,n…)` | ofuscação | 0 | — |
| escapes `\ddd` longos | ofuscação | 0 | — |
| `OnServerEvent` | fronteira de confiança: revisar validação | 0 | — |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 1 | `Cmdr/init.luau:142` |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** OK (seguro por padrão, com ressalvas)

- `Cmdr/init.luau:142`: o `OnServerInvoke` limita a entrada a 10.000 caracteres e delega ao `Dispatcher`.
- `CmdrClient/Shared/Dispatcher.luau:276`: fora do Studio, **comandos são bloqueados se nenhum hook `BeforeRun` estiver configurado** ('Command blocked for security as no BeforeRun hook is configured').
- Os comandos built-in incluem `fetch` (`BuiltInCommands/Debug/fetchServer.luau:4`, `HttpService.GetAsync(url)`), `kick` e teleporte. Registrar só os necessários e restringir via `BeforeRun` a grupos/IDs no servidor.
- Usa sintaxe Luau recente (`const`); exige toolchain atual.

## Veredito de segurança

✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
