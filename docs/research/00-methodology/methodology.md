# Metodologia

> Pesquisa realizada entre **2026-09-29 e 2026-09-30**. Todos os números (stars, commits, datas) são uma fotografia desse momento.

## Objetivo

Responder: **"Quais partes do Genesis Realms já existem no ecossistema Roblox e podem ser reutilizadas legal, técnica e arquiteturalmente?"**

Esta pesquisa não implementa nada do jogo. O repositório recebe só documentação e um catálogo em CSV, e **nenhum código de terceiros foi copiado para cá**.

## Pipeline

```text
1. Descoberta (longlist)          → 800+ pistas brutas (653 pacotes Wally únicos em 36 buscas, ~150 entradas do gist-semente, ~35 buscas web, 3 listas curadas)
2. Triagem + verificação          → 168 candidatos catalogados com licença e atividade verificadas (os demais foram descartados como re-uploads, forks, duplicatas ou fora de escopo)
3. Shortlist + análise profunda   → 49 repositórios clonados (blobless) no scratchpad
4. Auditoria de segurança         → grep estático + extração de .rbxm/.rbxl + leitura manual de remotes
5. Assets e licenças              → Creator Store, CC0, Mixamo, áudio
6. Síntese                        → seções A–G, top candidates, arquitetura, plano incremental
```

### 1. Descoberta

| Fonte | Como foi usada |
| --- | --- |
| Web search | Todas as consultas da §20 do brief, mais variações (anime battlegrounds, parkour, status effects, lag compensation, procedural terrain etc.). Ver [`../data/search-log.md`](../data/search-log.md). |
| GitHub | Páginas de repositório, tópicos e listas curadas (`awesome-roblox/awesome-roblox`, `loominatrx/useful-roblox-resources`, `Coyenn/awesome-roblox-ts`). |
| Registro Wally (`api.wally.run`) | Busca por ~40 palavras-chave (combat, hitbox, ability, quest, inventory, npc, pathfinding, behavior tree, state machine, camera, vfx, animation, pool, zone…). |
| DevForum (Community Resources e Announcements) | Leitura dos posts para autor, data, licença declarada e forma de distribuição. |
| Documentação oficial Roblox | Server Authority, Input Action System, Character Controller Library, Creator Store, Limited Use License, MCP embutido no Studio. |
| Gist "Roblox Combat & Movement Systems — Complete Catalog" | Usado **só como lista de pistas**. Nenhum dado dele entrou no catálogo sem verificação própria. |

### 2. Verificação de metadados

- **Licença:** vem do **arquivo LICENSE do clone** sempre que houve clone. Sem clone, vem do campo `license` do ecosyste.ms. Nos posts do DevForum, vale o texto do post. Quando fontes divergem, as duas aparecem no CSV (ex.: RoQuest com README MIT e LICENSE Apache-2.0; RagdollService com LICENSE MIT e ecosyste.ms LGPL-3.0).
- **Stars:** valor ao vivo via [ungh.cc](https://ungh.cc) (proxy público da API do GitHub), coletado em 2026-09-30 para as 152 linhas do GitHub. A primeira coleta, feita no [ecosyste.ms](https://repos.ecosyste.ms), estava desatualizada em 104 das 152 (ex.: ProfileStore 147 × 338 ao vivo), por isso foi substituída. O ecosyste.ms continua sendo a fonte de **arquivamento** e de **último push** quando não houve clone, e a data do sync fica registrada na coluna `archived`. Arquivamento dos candidatos recomendados cujo sync era antigo foi confirmado na página do GitHub.
- **Renomeações:** 6 repositórios redirecionam para um novo dono (ex.: `grayzcale/simplepath` → `ahmicy/simplepath`, `csqrl/sift` → `cxmeel/sift`). O CSV mantém o nome original na coluna `project`, usa a URL atual e explica o redirecionamento em `notes`.
- **Último commit, nº de commits, contributors, tags:** calculados com `git log`/`git shortlog` no clone (`--filter=blob:none`, histórico completo sem blobs antigos).
- Sem fonte verificável, o campo fica **`NÃO VERIFICADO`**. Nenhum valor foi estimado.

### 3. Análise profunda (49 repositórios)

Nos clones foram medidos:

- LICENSE real e arquivos de licença extras (ex.: `LICENSE-ART` do FastCast2);
- manifestos (`wally.toml`, `default.project.json`, `rokit.toml`/`aftman.toml`/`foreman.toml`, `pesde.toml`, `.gitmodules`);
- número de arquivos Luau, linhas, arquivos com `--!strict`, arquivos de teste e workflows de CI;
- binários `.rbxm`/`.rbxl`;
- leitura dos módulos principais para avaliar arquitetura, APIs, acoplamento e fronteiras de confiança.

### 4. Auditoria de segurança

Ver [`security-checklist.md`](security-checklist.md) e [`../security-audits/`](../security-audits/README.md).

- Grep por 15 padrões de risco em todo o código Luau (inclui `HttpService.GetAsync`, ampliado após a auditoria do Cmdr).
- **Arquivos binários:** foi escrito um extrator mínimo do formato binário Roblox (header `<roblox!`, chunks LZ4/zstd, `INST`/`PROP`, propriedade `Source`) para tirar o código de dentro de `.rbxm`/`.rbxl` e passá-lo pelo mesmo grep. Assim foram auditados MuchachoHitbox, Rewind, AMS, Chickynoid, Character-Realism e outros que distribuem código só em binário.
- Leitura manual dos handlers `OnServerEvent`/`OnServerInvoke` dos candidatos que expõem remotes próprios: Stoway, WCS, ClientCast, Wallstick, Character-Realism, RoQuest, Cmdr e Chickynoid. Em infraestrutura de rede genérica ou código gerado (RbxUtil `Comm`, template do gerador Blink), a leitura não foi linha a linha; a validação de payload fica anotada como responsabilidade do consumidor.

## Limitações conhecidas

1. **Creator Store** (create.roblox.com/store) é renderizado por JavaScript e tem acesso limitado por fetch. Itens de lá foram avaliados pelo post do DevForum correspondente. **Qualquer item do Creator Store precisa ser inspecionado dentro do Studio** (ver checklist).
2. **Stars e atividade** são snapshots de 2026-09-30. O ecosyste.ms pode atrasar meses (visto nesta pesquisa), por isso as stars vêm de uma fonte ao vivo e o sync do arquivamento fica registrado.
3. **Projetos em roblox-ts** (WCS, refx, AMS) foram avaliados pelo fonte TypeScript e pelo pacote Luau distribuído via Wally.
4. **Recursos oficiais** novos (Server Authority, CCL Custom Abilities API) ainda estão evoluindo. A situação descrita é a de 2026-09-30.
5. **Auditoria estática ≠ garantia.** Ela reduz o risco de backdoor e confiança indevida, mas não substitui testes nem revisão a cada atualização.
6. **Não sou advogado.** A classificação de licenças segue a prática comum de engenharia. Licenças custom (VFX-DL-1.1, TopbarPlus, DataStore2) e copyleft precisam de revisão jurídica antes do uso comercial.
7. A pesquisa priorizou **profundidade** nos candidatos com chance real de integração. Itens de nicho aparecem no CSV com dados parciais (`NÃO VERIFICADO`).
