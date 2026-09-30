# Checklist de segurança (brief §22)

Aplicar em **todo** pacote, modelo ou script externo, **e a cada atualização de versão**.

## A. Varredura automática (usada nesta pesquisa)

| # | Padrão (regex simplificada) | Por que importa |
| --- | --- | --- |
| 1 | `require\s*\(\s*\d{5,}` | Carrega um ModuleScript remoto por asset ID em runtime. É o vetor nº 1 de backdoor em Free Models. |
| 2 | `getfenv` / `setfenv` | Manipulação de ambiente. Proibido em assets distribuídos no Creator Store. |
| 3 | `loadstring` | Execução dinâmica de código. |
| 4 | `HttpService` + `PostAsync`/`RequestAsync`/`GetAsync(url)` | Tráfego externo e possível exfiltração. `GenerateGUID`/`JSONEncode` é benigno. |
| 5 | `webhook`, `discord(app).com/api/webhooks` | Exfiltração de dados e logs. |
| 6 | `InsertService` | Inserção de assets remotos em runtime. |
| 7 | `MarketplaceService` | Prompts de compra escondidos. |
| 8 | `TeleportService` | Redirecionamento de jogadores. |
| 9 | `:Kick(` | Expulsão; pode esconder ban arbitrário. |
| 10 | `UserId ==/~= <número>` | Admin ou whitelist escondido. |
| 11 | `string.char(n,n,n…)`, escapes `\ddd` longos | Ofuscação. |
| 12 | `OnServerEvent` / `OnServerInvoke` | Fronteira de confiança: sempre revisar à mão. |

Executar em todo o fonte **e** no código extraído de `.rbxm`/`.rbxl`/`.rbxmx`. Arquivos XML (`.rbxmx`) podem passar direto pelo grep. Os binários precisam de extração (Lune `roblox` lib, ou um parser como o usado nesta pesquisa).

## B. Revisão manual das fronteiras de confiança

Para cada remote do componente:

- [ ] O servidor **valida tipos** (`typeof`, `t`, código gerado por Blink/Zap) e **rejeita NaN/inf**.
- [ ] O servidor **valida semântica**: distância, alcance, linha de visão, estado atual, cooldown, posse do item, se o alvo é válido.
- [ ] **Rate limit** por jogador e por remote.
- [ ] O cliente **nunca** decide dano, XP, level, moeda, itens, raridade, rolls ou recompensas.
- [ ] Nada de `FireAllClients` retransmitindo payload do cliente sem validação (amplificação/spam).
- [ ] Comandos de debug e admin só existem em Studio **ou** atrás de checagem de permissão no servidor.
- [ ] Nenhum handler conectado por instância num remote compartilhado (custo O(n)).

## C. Supply chain (Wally/pesde)

- [ ] O **escopo** do pacote pertence ao autor do repositório original. O registro Wally tem dezenas de re-uploads: 24 escopos distintos publicam um pacote chamado `profilestore`, e há forks de RaycastHitbox, PartCache, CameraShaker e outros.
- [ ] A versão está **fixada** (`=x.y.z`) e o `wally.lock` foi commitado.
- [ ] As dependências transitivas foram listadas e auditadas.
- [ ] Submódulos e código vendorizado estão identificados.
- [ ] Nenhum pacote baixado via `InsertService:LoadAsset(id)` como "instalação".

## D. Creator Store e Free Models

**Nunca** inserir um Free Model só por ter muitas avaliações. Antes de trazer qualquer item para o place de produção:

1. Abrir num **place isolado** (sem DataStore/API services habilitados). Usar a opção de desabilitar scripts do objeto no Explorer, como recomenda a documentação do Creator Store.
2. Listar todos os `Script`, `LocalScript` e `ModuleScript`, inclusive os escondidos (nomes em branco, parentados em Parts, `Archivable=false`, dentro de `Folder`s aninhados).
3. Rodar o grep da seção A em todos.
4. Conferir `require` por ID, criação dinâmica de scripts, `Source` alterado em runtime, `Parent` para `ServerScriptService`, e plugins que pedem permissão de script injection ou HTTP.
5. Verificar **assets referenciados** (`rbxassetid://…`): animações, sons e meshes de terceiros podem sumir (moderação/privacidade) ou ter restrições.
6. Checar a licença e o autor. A documentação da Roblox proíbe em assets distribuídos: `getfenv`/`setfenv`, VMs Lua, requires remotos e código ofuscado. Encontrar qualquer um deles basta para rejeitar.
7. Só depois disso **copiar a lógica para o repositório (Rojo)** como código próprio revisado, se a licença permitir. Nunca manter o modelo "vivo" no place sem controle de versão.
