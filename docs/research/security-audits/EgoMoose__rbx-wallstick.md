# Auditoria — `EgoMoose/rbx-wallstick`

- **URL:** https://github.com/EgoMoose/rbx-wallstick
- **Commit auditado:** `02793758b912` (último commit 2026-06-04)
- **Licença (arquivo):** LICENSE → detectado: MIT
- **Escopo:** 14 arquivos Luau (1671 linhas), 14 com `--!strict` no arquivo, 0 arquivos de teste, 0 workflows de CI
- **Binários (.rbxm/.rbxl):** 1 — scripts extraídos com parser próprio e submetidos ao mesmo grep
- **Manifestos:** .luaurc, default.project.json, rokit.toml, selene.toml, stylua.toml, wally.toml
- **Submódulos:** nenhum
- **Código vendorizado:** nenhum detectado
- **Data da auditoria:** 2026-09-29

## Dependências Wally declaradas

- `wally.toml`: `sleitnick/trove@=1.5.0`, `sleitnick/typed-remote@0.3.0`, `egomoose/raycast-helper@3.0.0`, `egomoose/character-sounds@0.2.1`, `egomoose/character-animate@0.0.3`, `upliftgames/playermodule@700.0.7000935`

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
| `OnServerEvent` | fronteira de confiança: revisar validação | 1 | `src/client/Wallstick/Replication.luau:51` |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 1 | `src/client/Wallstick/Replication.luau:64` |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** ATENÇÃO

- `src/client/Wallstick/Replication.luau:51`: `OnServerEvent(player, part, offset)` armazena e retransmite para **todos** os clientes sem validar tipos nem aplicar rate limit. Um cliente malicioso pode inundar os outros.
- A replicação é opcional (`Replication.ENABLED`).

## Veredito de segurança

⚠️ Usar com mitigação

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
