# Auditoria — `easy-games/chickynoid`

- **URL:** https://github.com/easy-games/chickynoid
- **Commit auditado:** `8c3b643526f2` (último commit 2024-01-03)
- **Licença (arquivo):** LICENSE → detectado: MIT
- **Escopo:** 51 arquivos Luau (11163 linhas), 0 com `--!strict` no arquivo, 0 arquivos de teste, 0 workflows de CI
- **Binários (.rbxm/.rbxl):** 14 — scripts extraídos com parser próprio e submetidos ao mesmo grep
- **Manifestos:** default.project.json, foreman.toml, package.json, selene.toml, stylua.toml, tsconfig.json, wally.toml
- **Submódulos:** nenhum
- **Código vendorizado:** /Packages/Chickynoid /Vendor/CrunchTable.lua /Vendor/DeltaTable.lua /Vendor/FastSignal.lua /Vendor/Profiler.lua /Vendor/QuickHull2.lua /Vendor/ReadBuffer.lua /Vendor/TrianglePart.lua
- **Data da auditoria:** 2026-09-29

## Dependências Wally declaradas

- nenhuma declarada

## Varredura automática (grep)

| Padrão | Risco | Ocorrências | Exemplos |
| --- | --- | ---: | --- |
| `require(<assetId>)` | carrega código remoto em runtime (vetor clássico de backdoor) | 0 | — |
| `getfenv`/`setfenv` | manipulação de ambiente; proibido em assets distribuídos pela Roblox | 0 | — |
| `loadstring` | execução de código dinâmico | 0 | — |
| `HttpService` | pode indicar tráfego externo; conferir método | 0 | — |
| `PostAsync`/`RequestAsync`/`GetAsync(url)` | requisição HTTP externa | 0 | — |
| `webhook`/`discord` | exfiltração para webhooks | 0 | — |
| `InsertService` | inserção de assets em runtime | 0 | — |
| `TeleportService` | teleporte de jogadores | 0 | — |
| `MarketplaceService` | prompts de compra ocultos | 0 | — |
| `:Kick(` | expulsão de jogadores | 1 | `src/ServerScriptService/Packages/Chickynoid/Server/ServerModule.lua:221` |
| comparação com UserId fixo | admin/whitelist escondido | 0 | — |
| `string.char(n,n,n…)` | ofuscação | 0 | — |
| escapes `\ddd` longos | ofuscação | 0 | — |
| `OnServerEvent` | fronteira de confiança: revisar validação | 2 | `src/ServerScriptService/Packages/Chickynoid/Server/ServerModule.lua:115`, `src/ServerScriptService/Packages/Chickynoid/Server/ServerModule.lua:125` |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 0 | — |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** OK

- O servidor recebe comandos de input e simula de forma autoritativa. O único `:Kick` encontrado (`ServerModule.lua:221`) é para 'Server full'.
- 14 arquivos binários (`.rbxm`/`.rbxl`) foram extraídos. Contêm UI, efeitos, rig R15 e um mapa de exemplo com 11 scripts de animação de textura. Nenhum achado.

## Veredito de segurança

✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
