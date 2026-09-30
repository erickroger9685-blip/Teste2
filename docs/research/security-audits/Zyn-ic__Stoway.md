# Auditoria — `Zyn-ic/Stoway`

- **URL:** https://github.com/Zyn-ic/Stoway
- **Commit auditado:** `ed64b7e46df8` (último commit 2026-03-07)
- **Licença (arquivo):** LICENSE → detectado: MIT
- **Escopo:** 35 arquivos Luau (5858 linhas), 0 com `--!strict` no arquivo, 0 arquivos de teste, 0 workflows de CI
- **Binários (.rbxm/.rbxl):** 0
- **Manifestos:** aftman.toml, default.project.json, rokit.toml, selene.toml, wally.toml
- **Submódulos:** nenhum
- **Código vendorizado:** nenhum detectado
- **Data da auditoria:** 2026-09-29

## Dependências Wally declaradas

- `wally.toml`: `howmanysmall/janitor@1.18.3`, `acecateer/fusion@0.3.1`

## Varredura automática (grep)

| Padrão | Risco | Ocorrências | Exemplos |
| --- | --- | ---: | --- |
| `require(<assetId>)` | carrega código remoto em runtime (vetor clássico de backdoor) | 0 | — |
| `getfenv`/`setfenv` | manipulação de ambiente; proibido em assets distribuídos pela Roblox | 0 | — |
| `loadstring` | execução de código dinâmico | 0 | — |
| `HttpService` | pode indicar tráfego externo; conferir método | 3 | `src/server/StowayServerV1_2/Utils/UUID.luau:6`, `src/server/StowayServerV1_2/Utils/UUID.luau:6`, `src/server/StowayServerV1_2/Utils/UUID.luau:9` |
| `PostAsync`/`RequestAsync`/`GetAsync(url)` | requisição HTTP externa | 0 | — |
| `webhook`/`discord` | exfiltração para webhooks | 0 | — |
| `InsertService` | inserção de assets em runtime | 0 | — |
| `TeleportService` | teleporte de jogadores | 0 | — |
| `MarketplaceService` | prompts de compra ocultos | 0 | — |
| `:Kick(` | expulsão de jogadores | 0 | — |
| comparação com UserId fixo | admin/whitelist escondido | 0 | — |
| `string.char(n,n,n…)` | ofuscação | 0 | — |
| escapes `\ddd` longos | ofuscação | 0 | — |
| `OnServerEvent` | fronteira de confiança: revisar validação | 1 | `src/server/StowayServerV1_2/init.luau:489` |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 2 | `src/server/StowayServerV1_2/Replication/Replicator.luau:84`, `src/server/StowayServerV1_2/init.luau:462` |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** ACHADO CRÍTICO

- `src/server/StowayServerV1_2/init.luau:64` chama `ChatCommands.Register(player, InventoryService)` para **todo** jogador que entra, sem checar permissão, `RunService:IsStudio()` ou flag de debug.
- `Debug/ChatCommands.luau` expõe `/add [itemId] [amount]` (linha 55, chama `InventoryService.AddItem` com item e quantidade arbitrários), além de `/clear`, `/set_limit`, `/set_max_stack`, `/toggle_limit` etc. Em produção, **qualquer jogador cria itens pelo chat**.
- O remote `InventoryAction` valida a operação (whitelist `OperationHandlers`), o tipo dos args e usa lock por jogador. É um bom padrão.
- Dependência `fusion = "acecateer/fusion@0.3.1"`: o escopo Wally **não é o do autor do Fusion**. Risco de supply chain; trocar pelo pacote oficial.
- `HttpService` é usado só para `GenerateGUID` (UUID de itens).

## Veredito de segurança

⛔ Bloqueado até correção

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
