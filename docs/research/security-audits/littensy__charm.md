# Auditoria — `littensy/charm`

- **URL:** https://github.com/littensy/charm
- **Commit auditado:** `b05f3a9de6fc` (último commit 2026-06-21)
- **Licença (arquivo):** LICENSE → detectado: MIT
- **Escopo:** 58 arquivos Luau (6786 linhas), 0 com `--!strict` no arquivo + `.luaurc` languageMode=`strict` (vale p/ o projeto), 30 arquivos de teste, 2 workflows de CI
- **Binários (.rbxm/.rbxl):** 0
- **Manifestos:** .gitmodules, .luaurc, default.project.json, package.json, packages/charm-sync/default.project.json, packages/charm-sync/package.json, packages/charm-sync/wally.toml, packages/charm/default.project.json, packages/charm/package.json, packages/charm/wally.toml, packages/deep-charm/default.project.json, packages/deep-charm/package.json, packages/deep-charm/wally.toml, packages/react-charm/default.project.json, packages/react-charm/package.json, packages/react-charm/wally.toml, packages/vide-charm/default.project.json, packages/vide-charm/package.json, packages/vide-charm/wally.toml, rokit.toml, stylua.toml, tsconfig.json
- **Submódulos:** https://gist.github.com/littensy/fa9afcc5d66d25e86538634982be4ee4
- **Código vendorizado:** packages/charm packages/charm-sync packages/deep-charm packages/react-charm packages/vide-charm
- **Data da auditoria:** 2026-09-29

## Dependências Wally declaradas

- `packages/charm-sync/wally.toml`: `littensy/charm@^0.11.0`
- `packages/deep-charm/wally.toml`: `littensy/charm@^0.11.0`

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
| `OnServerEvent` | fronteira de confiança: revisar validação | 0 | — |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 0 | — |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** OK

- O `.gitmodules` aponta para um gist do autor: é uma dependência de dev a fixar por commit.

## Veredito de segurança

✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
