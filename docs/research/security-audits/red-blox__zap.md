# Auditoria — `red-blox/zap`

- **URL:** https://github.com/red-blox/zap
- **Commit auditado:** `8cd17ab78192` (último commit 2026-06-23)
- **Licença (arquivo):** LICENSE → detectado: MIT
- **Escopo:** 3 arquivos Luau (261 linhas), 1 com `--!strict` no arquivo + `.luaurc` languageMode=`nocheck` (vale p/ o projeto), 2 arquivos de teste, 3 workflows de CI
- **Binários (.rbxm/.rbxl):** 0
- **Manifestos:** .luaurc, package.json, selene.toml
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
| `HttpService` | pode indicar tráfego externo; conferir método | 0 | — |
| `PostAsync`/`RequestAsync`/`GetAsync(url)` | requisição HTTP externa | 0 | — |
| `webhook`/`discord` | exfiltração para webhooks | 0 | — |
| `InsertService` | inserção de assets em runtime | 0 | — |
| `TeleportService` | teleporte de jogadores | 0 | — |
| `MarketplaceService` | prompts de compra ocultos | 0 | — |
| `:Kick(` | expulsão de jogadores | 0 | — |
| comparação com UserId fixo | admin/whitelist escondido | 0 | — |
| `string.char(n,n,n…)` | ofuscação | 0 | — |
| escapes `\ddd` longos | ofuscação | 0 | — |
| `OnServerEvent` | fronteira de confiança: revisar validação | 2 | `zap/tests/lune/base.luau:38`, `zap/tests/lune/base.luau:44` |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 0 | — |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** OK

- Sem revisão manual linha a linha além da varredura. Os handlers de rede apontados na tabela devem ser revisados antes da integração.

## Veredito de segurança

✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
