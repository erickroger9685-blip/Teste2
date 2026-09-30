# Auditoria — `dphfox/Fusion`

- **URL:** https://github.com/dphfox/Fusion
- **Commit auditado:** `2790f7b6272b` (último commit 2026-02-01)
- **Licença (arquivo):** LICENSE → detectado: MIT
- **Escopo:** 114 arquivos Luau (12112 linhas), 98 com `--!strict` no arquivo + `.luaurc` languageMode=`strict` (vale p/ o projeto), 49 arquivos de teste, 2 workflows de CI
- **Binários (.rbxm/.rbxl):** 0
- **Manifestos:** .luaurc, aftman.toml, default.project.json, package.json, selene.toml, wally.toml
- **Submódulos:** nenhum
- **Código vendorizado:** nenhum detectado
- **Data da auditoria:** 2026-09-29

## Dependências Wally declaradas

- nenhuma declarada

## Varredura automática (grep)

| Padrão | Risco | Ocorrências | Exemplos |
| --- | --- | ---: | --- |
| `require(<assetId>)` | carrega código remoto em runtime (vetor clássico de backdoor) | 0 | — |
| `getfenv`/`setfenv` | manipulação de ambiente; proibido em assets distribuídos pela Roblox | 210 | `test/Spec/Animation/springCoefficients.spec.luau:11`, `test/Spec/Animation/springCoefficients.spec.luau:14`, `test/Spec/Animation/springCoefficients.spec.luau:25` |
| `loadstring` | execução de código dinâmico | 0 | — |
| `HttpService` | pode indicar tráfego externo; conferir método | 3 | `src/RobloxExternal.luau:10`, `src/RobloxExternal.luau:10`, `src/RobloxExternal.luau:71` |
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

- As 210 ocorrências de `getfenv`/`setfenv` estão só em `test/Spec`. `HttpService` só para GUID.

## Veredito de segurança

✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
