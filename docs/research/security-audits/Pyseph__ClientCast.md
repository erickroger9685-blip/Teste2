# Auditoria — `Pyseph/ClientCast`

- **URL:** https://github.com/Pyseph/ClientCast
- **Commit auditado:** `3e3c0bd7b329` (último commit 2023-09-25)
- **Licença (arquivo):** LICENSE → detectado: MIT
- **Escopo:** 6 arquivos Luau (1241 linhas), 0 com `--!strict` no arquivo, 0 arquivos de teste, 0 workflows de CI
- **Binários (.rbxm/.rbxl):** 0
- **Manifestos:** aftman.toml, default.project.json, foreman.toml
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
| `OnServerEvent` | fronteira de confiança: revisar validação | 2 | `lib/init.luau:151`, `testing/server/Testing.server.luau:54` |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 0 | — |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** ATENÇÃO (confiança no cliente)

- `lib/init.luau:151-173`: o servidor aceita o `RaycastResult` serializado que vem do cliente e só confere `Player == Owner`, o ID do caster e se o resultado é desserializável. Não há checagem de distância, tempo ou geometria.
- Cada `Start()` conecta um novo handler `OnServerEvent` no mesmo remote, o que dá custo O(n) por evento com muitos casters.

## Veredito de segurança

⚠️ Usar com mitigação

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
