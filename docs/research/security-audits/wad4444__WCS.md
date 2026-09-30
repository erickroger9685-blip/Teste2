# Auditoria — `wad4444/WCS`

- **URL:** https://github.com/wad4444/WCS
- **Commit auditado:** `091a53e2e82b` (último commit 2025-11-12)
- **Licença (arquivo):** LICENSE.txt → detectado: MIT
- **Escopo:** 8 arquivos Luau (570 linhas), 0 com `--!strict` no arquivo, 0 arquivos de teste, 3 workflows de CI
- **Binários (.rbxm/.rbxl):** 0
- **Manifestos:** default.project.json, docs/package.json, package.json, rokit.toml, tsconfig.json, wally.toml
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
| `OnServerEvent` | fronteira de confiança: revisar validação | 0 | — |
| `OnServerInvoke` | fronteira de confiança: revisar validação | 0 | — |

Em toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.

## Revisão manual

**Status:** OK com ressalvas

- `src/source/server.ts`: `requestSkill` confere se `character.Player == Player` e se a skill existe. `Skill.Start` checa debounce/cooldown, `MutualExclusives`, `Requirements` e `ShouldStart`.
- Os parâmetros enviados pelo cliente vão direto para `skill.Start(...Params)`. Validar em `ShouldStart` é responsabilidade de quem escreve a skill. Mensagens têm `Validators` opcionais.
- Não há rate limit nos eventos.
- O pacote Wally `cheetiedotpy/wcs` embute `node_modules` (@flamework/core, @flamework/networking, @rbxts/charm, charm-sync, janitor, t, timer…). Isso significa uma pilha de rede e de runtime paralela à do projeto.

## Veredito de segurança

✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)

> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).
