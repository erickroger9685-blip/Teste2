# Auditoria — `Gzeu/roblox-procedural-worlds`

- **URL:** https://github.com/Gzeu/roblox-procedural-worlds
- **Commit auditado:** `304ae16b814f` (último commit 2026-04-14)
- **Licença (arquivo):** LICENSE → detectado: MIT
- **Escopo:** 73 arquivos Luau (9601 linhas), 19 com `--!strict` no arquivo, 0 arquivos de teste, 2 workflows de CI
- **Binários (.rbxm/.rbxl):** 0
- **Manifestos:** default.project.json, rojo/default.project.json, selene.toml
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
| `TeleportService` | teleporte de jogadores | 3 | `src/TeleportManager.lua:6`, `src/TeleportManager.lua:6`, `src/TeleportManager.lua:98` |
| `MarketplaceService` | prompts de compra ocultos | 10 | `src/DeveloperProductHandler.lua:14`, `src/DeveloperProductHandler.lua:14`, `src/DeveloperProductHandler.lua:109` |
| `:Kick(` | expulsão de jogadores | 1 | `src/AntiExploit.lua:49` |
| comparação com UserId fixo | admin/whitelist escondido | 0 | — |
| `string.char(n,n,n…)` | ofuscação | 0 | — |
| escapes `\ddd` longos | ofuscação | 0 | — |
| `OnServerEvent` | fronteira de confiança: revisar validação | 4 | `src/NPCDialogue.lua:298`, `src/PartySystem.lua:213`, `src/PartySystem.lua:217` |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 2 | `src/InventoryRemote.lua:27`, `src/SeedShare.lua:23` |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** OK (escopo amplo)

- Inclui `DeveloperProductHandler`, `TeleportManager` e `AntiExploit`, fora do escopo de geração de mundo. O Kick de `AntiExploit.lua:49` acontece após N flags heurísticas. O grep não achou backdoor, mas o repositório não foi lido por inteiro. Tem cara de coleção 'kitchen-sink': não importar em bloco.

## Veredito de segurança

✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
