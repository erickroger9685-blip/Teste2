# Auditoria — `1ForeverHD/TopbarPlus`

- **URL:** https://github.com/1ForeverHD/TopbarPlus
- **Commit auditado:** `f44992bf0299` (último commit 2025-09-17)
- **Licença (arquivo):** LICENSE → detectado: MPL-2.0
- **Escopo:** 21 arquivos Luau (5521 linhas), 2 com `--!strict` no arquivo, 0 arquivos de teste, 1 workflows de CI
- **Binários (.rbxm/.rbxl):** 0
- **Manifestos:** aftman.toml, default.project.json, selene.toml, wally.toml
- **Submódulos:** nenhum
- **Código vendorizado:** /Packages/GoodSignal.lua /Packages/Janitor.lua
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
| `MarketplaceService` | prompts de compra ocultos | 1 | `src/VERSION.lua:23` |
| `:Kick(` | expulsão de jogadores | 0 | — |
| comparação com UserId fixo | admin/whitelist escondido | 0 | — |
| `string.char(n,n,n…)` | ofuscação | 0 | — |
| escapes `\ddd` longos | ofuscação | 0 | — |
| `OnServerEvent` | fronteira de confiança: revisar validação | 0 | — |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 0 | — |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** OK

- Sem revisão manual linha a linha além da varredura. Os handlers de rede apontados na tabela devem ser revisados antes da integração.

## Veredito de segurança

✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
