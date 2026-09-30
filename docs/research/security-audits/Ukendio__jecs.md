# Auditoria — `Ukendio/jecs`

- **URL:** https://github.com/Ukendio/jecs
- **Commit auditado:** `0ca7a3b54a06` (último commit 2026-09-17)
- **Licença (arquivo):** LICENSE → detectado: MIT
- **Escopo:** 193 arquivos Luau (34816 linhas), 14 com `--!strict` no arquivo + `.luaurc` languageMode=`strict` (vale p/ o projeto), 13 arquivos de teste, 4 workflows de CI
- **Binários (.rbxm/.rbxl):** 1 — scripts extraídos com parser próprio e submetidos ao mesmo grep
- **Manifestos:** .luaurc, default.project.json, package.json, rokit.toml, test/benches/default.project.json, test/benches/visual/wally.toml, tsconfig.json, wally.toml
- **Submódulos:** nenhum
- **Código vendorizado:** nenhum detectado
- **Data da auditoria:** 2026-09-29

## Dependências Wally declaradas

- `test/benches/visual/wally.toml`: `matter-ecs/matter@0.8.0`, `centau/ecr@0.8.0`

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
| `OnServerEvent` | fronteira de confiança: revisar validação | 3 | `examples/networking/networking_send.luau:105`, `examples/networking/remotes.luau:8`, `modules/Jabby/modules/net.luau:158` |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 0 | — |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** OK

- Sem revisão manual linha a linha além da varredura. Os handlers de rede apontados na tabela devem ser revisados antes da integração.

## Veredito de segurança

✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
