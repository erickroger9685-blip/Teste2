# Auditoria — `YetAnotherClown/planck`

- **URL:** https://github.com/YetAnotherClown/planck
- **Commit auditado:** `c0c61804f7b2` (último commit 2026-09-24)
- **Licença (arquivo):** LICENSE.md → detectado: MIT
- **Escopo:** 35 arquivos Luau (6257 linhas), 0 com `--!strict` no arquivo + `.luaurc` languageMode=`strict` (vale p/ o projeto), 6 arquivos de teste, 0 workflows de CI
- **Binários (.rbxm/.rbxl):** 0
- **Manifestos:** .luaurc, default.project.json, package.json, rokit.toml, selene.toml, src/planck/default.project.json, src/planck/package.json, src/planck/wally.toml, src/planck_jabby/default.project.json, src/planck_jabby/package.json, src/planck_jabby/wally.toml, src/planck_matter_debugger/default.project.json, src/planck_matter_debugger/package.json, src/planck_matter_debugger/wally.toml, src/planck_matter_hooks/default.project.json, src/planck_matter_hooks/package.json, src/planck_matter_hooks/wally.toml, src/planck_runservice/default.project.json, src/planck_runservice/package.json, src/planck_runservice/wally.toml, stylua.toml, tsconfig.json, wally.toml
- **Submódulos:** nenhum
- **Código vendorizado:** nenhum detectado
- **Data da auditoria:** 2026-09-29

## Dependências Wally declaradas

- `src/planck/wally.toml`: `jsdotlua/jest@3.6.1-rc.2`, `jsdotlua/jest-globals@3.6.1-rc.2`
- `src/planck_jabby/wally.toml`: `jsdotlua/jest@3.6.1-rc.2`, `jsdotlua/jest-globals@3.6.1-rc.2`, `yetanotherclown/planck@^0.3.0-rc.2`, `alicesaidhi/jabby@0.5.1`
- `src/planck_matter_debugger/wally.toml`: `yetanotherclown/planck@^0.3.0-rc.2`

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

- Scheduler puro, sem remotes nem serviços sensíveis. `.luaurc` strict.

## Veredito de segurança

✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
