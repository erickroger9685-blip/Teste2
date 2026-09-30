"""Generate docs/research/security-audits/<owner>__<repo>.md from analysis.json + manual review notes."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
EVID = os.path.join(HERE, '..', 'data', 'evidence')
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.normpath(os.path.join(HERE, '..', '..', '..'))
OUT = os.path.join(REPO, 'docs/research/security-audits')
os.makedirs(OUT, exist_ok=True)
A = json.load(open(os.path.join(EVID, 'analysis.json')))
extra = {}
for line in open(os.path.join(EVID, 'extra.txt')):
    d, sha, gm, vend = (line.rstrip('\n').split('|') + ['', '', ''])[:4]
    extra[d.replace('_', '/', 1).lower()] = dict(sha=sha, gm=gm.strip(), vend=vend.strip())

PAT_DESC = {
 'require_assetid': ('`require(<assetId>)`', 'carrega código remoto em runtime (vetor clássico de backdoor)'),
 'getfenv_setfenv': ('`getfenv`/`setfenv`', 'manipulação de ambiente; proibido em assets distribuídos pela Roblox'),
 'loadstring': ('`loadstring`', 'execução de código dinâmico'),
 'HttpService': ('`HttpService`', 'pode indicar tráfego externo; conferir método'),
 'http_post': ('`PostAsync`/`RequestAsync`/`GetAsync(url)`', 'requisição HTTP externa'),
 'webhook_discord': ('`webhook`/`discord`', 'exfiltração para webhooks'),
 'InsertService': ('`InsertService`', 'inserção de assets em runtime'),
 'TeleportService': ('`TeleportService`', 'teleporte de jogadores'),
 'MarketplaceService': ('`MarketplaceService`', 'prompts de compra ocultos'),
 'kick': ('`:Kick(`', 'expulsão de jogadores'),
 'userid_whitelist': ('comparação com UserId fixo', 'admin/whitelist escondido'),
 'string_char_obf': ('`string.char(n,n,n…)`', 'ofuscação'),
 'long_escape_obf': ('escapes `\\ddd` longos', 'ofuscação'),
 'OnServerEvent': ('`OnServerEvent`', 'fronteira de confiança: revisar validação'),
 'OnServerInvoke': ('`OnServerInvoke`', 'fronteira de confiança: revisar validação'),
}

# Manual review (read by hand during the research)
MANUAL = {
 'zyn-ic/stoway': ("ACHADO CRÍTICO", [
   "`src/server/StowayServerV1_2/init.luau:64` chama `ChatCommands.Register(player, InventoryService)` para **todo** jogador que entra, sem checar permissão, `RunService:IsStudio()` ou flag de debug.",
   "`Debug/ChatCommands.luau` expõe `/add [itemId] [amount]` (linha 55, chama `InventoryService.AddItem` com item e quantidade arbitrários), além de `/clear`, `/set_limit`, `/set_max_stack`, `/toggle_limit` etc. Em produção, **qualquer jogador cria itens pelo chat**.",
   "O remote `InventoryAction` valida a operação (whitelist `OperationHandlers`), o tipo dos args e usa lock por jogador. É um bom padrão.",
   "Dependência `fusion = \"acecateer/fusion@0.3.1\"`: o escopo Wally **não é o do autor do Fusion**. Risco de supply chain; trocar pelo pacote oficial.",
   "`HttpService` é usado só para `GenerateGUID` (UUID de itens)."]),
 'wad4444/wcs': ("OK com ressalvas", [
   "`src/source/server.ts`: `requestSkill` confere se `character.Player == Player` e se a skill existe. `Skill.Start` checa debounce/cooldown, `MutualExclusives`, `Requirements` e `ShouldStart`.",
   "Os parâmetros enviados pelo cliente vão direto para `skill.Start(...Params)`. Validar em `ShouldStart` é responsabilidade de quem escreve a skill. Mensagens têm `Validators` opcionais.",
   "Não há rate limit nos eventos.",
   "O pacote Wally `cheetiedotpy/wcs` embute `node_modules` (@flamework/core, @flamework/networking, @rbxts/charm, charm-sync, janitor, t, timer…). Isso significa uma pilha de rede e de runtime paralela à do projeto."]),
 'pyseph/clientcast': ("ATENÇÃO (confiança no cliente)", [
   "`lib/init.luau:151-173`: o servidor aceita o `RaycastResult` serializado que vem do cliente e só confere `Player == Owner`, o ID do caster e se o resultado é desserializável. Não há checagem de distância, tempo ou geometria.",
   "Cada `Start()` conecta um novo handler `OnServerEvent` no mesmo remote, o que dá custo O(n) por evento com muitos casters."]),
 'egomoose/rbx-wallstick': ("ATENÇÃO", [
   "`src/client/Wallstick/Replication.luau:51`: `OnServerEvent(player, part, offset)` armazena e retransmite para **todos** os clientes sem validar tipos nem aplicar rate limit. Um cliente malicioso pode inundar os outros.",
   "A replicação é opcional (`Replication.ENABLED`)."]),
 'maximumadhd/character-realism': ("OK", [
   "`Realism.server.lua:15`: valida `type(pitch/yaw)=='number'`, rejeita NaN e faz clamp em [-1,1]. Não tem rate limit, e cada evento gera `FireAllClients`."]),
 'easy-games/chickynoid': ("OK", [
   "O servidor recebe comandos de input e simula de forma autoritativa. O único `:Kick` encontrado (`ServerModule.lua:221`) é para 'Server full'.",
   "14 arquivos binários (`.rbxm`/`.rbxl`) foram extraídos. Contêm UI, efeitos, rig R15 e um mapa de exemplo com 11 scripts de animação de textura. Nenhum achado."]),
 'text21/rewind': ("OK (mas sem licença)", [
   "Fonte e 4 builds `.rbxm` foram extraídos. `getfenv`/`loadstring` aparecem só no TestEZ/lemur vendorizado. `AbuseTracker.lua` faz Kick/ban automático por heurística, o que exige revisão de falsos positivos.",
   "**Sem arquivo de licença**, portanto não pode ser usado."]),
 'catsushi/muchachohitbox': ("OK", [
   "O repositório só distribui `MuchachoHitbox.rbxm`. Foram extraídos 4 ModuleScripts (MuchachoHitbox, DictDiff, GoodSignal, Types) e nenhum padrão suspeito foi encontrado."]),
 'prooheckcp/roquest': ("OK", [
   "Os handlers de rede (`RoQuest/Server/init.luau:664-684`) são só de leitura (GetPlayerData/GetQuests/GetAvailableQuests/GetUnAvailableQuests). O progresso de objetivos só muda pela API de servidor (`AddObjective`, `CompleteQuest`…).",
   "Vendoriza Red, Promise, Signal e Trove. Qualquer atualização de segurança desses pacotes precisa ser aplicada manualmente."]),
 'madstudioroblox/profilestore': ("OK", ["`HttpService` só para `GenerateGUID`. Arquivo único (~3k LOC)."]),
 'paradoxum-games/lyra': ("OK", ["`HttpService` só para JSON/GUID. Os `Kick` em `PlayerStore.luau:200/206` ficam no helper interno `_kickPlayer`, documentado como 'kick players when data errors occur'. `TeleportService` e as comparações de UserId aparecem só em `test/`."]),
 'nezuo/lapis': ("OK", ["`MarketplaceService`/`Kick` aparecem só em `examples/`."]),
 'gzeu/roblox-procedural-worlds': ("OK (escopo amplo)", ["Inclui `DeveloperProductHandler`, `TeleportManager` e `AntiExploit`, fora do escopo de geração de mundo. O Kick de `AntiExploit.lua:49` acontece após N flags heurísticas. O grep não achou backdoor, mas o repositório não foi lido por inteiro. Tem cara de coleção 'kitchen-sink': não importar em bloco."]),
 'sleitnick/rbxutil': ("OK", ["`HttpService` só para JSON em `modules/log`. Os handlers de `Comm`/`Net` são infraestrutura de rede genérica (não revisados linha a linha); validar payloads continua sendo responsabilidade do consumidor."]),
 'weenachuangkud/fastcast2': ("OK", ["`HttpService` só para `GenerateGUID`. A arte (logos) está sob CC BY-NC-ND e não pode ser reutilizada."]),
 'hatmatty/ams': ("OK", ["O `build.rbxl` foi extraído. `HttpService` só para `GenerateGUID`."]),
 'dphfox/fusion': ("OK", ["As 210 ocorrências de `getfenv`/`setfenv` estão só em `test/Spec`. `HttpService` só para GUID."]),
 'littensy/charm': ("OK", ["O `.gitmodules` aponta para um gist do autor: é uma dependência de dev a fixar por commit."]),
 'evaera/cmdr': ("OK (seguro por padrão, com ressalvas)", [
   "`Cmdr/init.luau:142`: o `OnServerInvoke` limita a entrada a 10.000 caracteres e delega ao `Dispatcher`.",
   "`CmdrClient/Shared/Dispatcher.luau:276`: fora do Studio, **comandos são bloqueados se nenhum hook `BeforeRun` estiver configurado** ('Command blocked for security as no BeforeRun hook is configured').",
   "Os comandos built-in incluem `fetch` (`BuiltInCommands/Debug/fetchServer.luau:4`, `HttpService.GetAsync(url)`), `kick` e teleporte. Registrar só os necessários e restringir via `BeforeRun` a grupos/IDs no servidor.",
   "Usa sintaxe Luau recente (`const`); exige toolchain atual."]),
 'yetanotherclown/planck': ("OK", ["Scheduler puro, sem remotes nem serviços sensíveis. `.luaurc` strict."]),
 'zilibobi/forge-vfx': ("OK (licença custom)", ["Os submódulos `kohltastrophe/Z` e `dphfox/tiniest` também precisam de verificação de licença antes do uso."]),
}

VERDICT_RULES = {'ACHADO CRÍTICO': '⛔ Bloqueado até correção', 'ATENÇÃO': '⚠️ Usar com mitigação'}

index_rows = []
for key_raw, a in sorted(A.items(), key=lambda x: x[0].lower()):
    key = key_raw.lower()
    ex = extra.get(key, {})
    fn = key_raw.replace('/', '__') + '.md'
    status, notes = MANUAL.get(key, ("OK", []))
    lines = [f"# Auditoria — `{key_raw}`\n",
             f"- **URL:** https://github.com/{key_raw}",
             f"- **Commit auditado:** `{ex.get('sha','?')}` (último commit {a['last_commit']})",
             f"- **Licença (arquivo):** {', '.join(a['license_files']) or 'NENHUM'} → detectado: {', '.join(a['license_detected']) or 'NÃO IDENTIFICADO'}",
             f"- **Escopo:** {a['lua_files']} arquivos Luau ({a['loc']} linhas), {a['strict']} com `--!strict` no arquivo" + (f" + `.luaurc` languageMode=`{a['luaurc_mode']}` (vale p/ o projeto)" if a.get('luaurc_mode') else '') + f", {a['n_tests']} arquivos de teste, {len(a['ci'])} workflows de CI",
             f"- **Binários (.rbxm/.rbxl):** {len(a['binaries'])}" + (" — scripts extraídos com parser próprio e submetidos ao mesmo grep" if a['binaries'] else ''),
             f"- **Manifestos:** {', '.join(a['manifests']) or 'nenhum'}",
             f"- **Submódulos:** {ex.get('gm') or 'nenhum'}",
             f"- **Código vendorizado:** {ex.get('vend') or 'nenhum detectado'}",
             f"- **Data da auditoria:** 2026-09-29\n"]
    deps = []
    for w, info in a.get('wally', {}).items():
        if info.get('deps'): deps.append(f"`{w}`: " + ', '.join(f'`{d}`' for d in info['deps']))
    lines.append("## Dependências Wally declaradas\n")
    lines.append('\n'.join(f'- {d}' for d in deps) if deps else '- nenhuma declarada')
    lines.append("\n## Varredura automática (grep)\n")
    lines.append("| Padrão | Risco | Ocorrências | Exemplos |")
    lines.append("| --- | --- | ---: | --- |")
    for k, (label, risk) in PAT_DESC.items():
        hits = a['sec'].get(k, [])
        exs = ', '.join(f'`{h}`' for h in hits[:3])
        lines.append(f"| {label} | {risk} | {len(hits)} | {exs or '—'} |")
    lines.append("\nEm toda a shortlist, a única chamada HTTP de saída encontrada é o comando administrativo built-in `fetch` do Cmdr (bloqueado sem hook `BeforeRun`). Nos demais, `HttpService` só aparece como `GenerateGUID`/`JSONEncode`/`JSONDecode`.\n")
    lines.append("## Revisão manual\n")
    lines.append(f"**Status:** {status}\n")
    lines.append('\n'.join(f'- {n}' for n in notes) if notes else '- Sem revisão manual linha a linha além da varredura. Os handlers de rede apontados na tabela devem ser revisados antes da integração.')
    verdict = next((v for k, v in VERDICT_RULES.items() if status.startswith(k)), '✅ Sem bloqueios de segurança (licença e arquitetura avaliadas no catálogo)')
    if 'sem licença' in status: verdict = '⛔ Bloqueado por licença'
    lines.append(f"\n## Veredito de segurança\n\n{verdict}\n")
    lines.append("> Uma auditoria estática não garante ausência de bugs. Toda nova versão importada precisa passar de novo pelo [checklist](../00-methodology/security-checklist.md).\n")
    open(os.path.join(OUT, fn), 'w').write('\n'.join(lines))
    index_rows.append((key_raw, fn, status, verdict, ex.get('sha', '?')))

idx = ["# Auditorias de segurança da shortlist\n",
       "Foram clonados 49 repositórios no scratchpad (fora deste repo). Nenhum código de terceiros foi copiado para cá. Em cada um rodou uma varredura estática (ver [checklist](../00-methodology/security-checklist.md)) e, nos candidatos a integração, houve leitura manual das fronteiras de confiança (`OnServerEvent`/`OnServerInvoke`).\n",
       "Os arquivos binários `.rbxm`/`.rbxl` não podem ser auditados por texto. Por isso os scripts foram **extraídos com um parser mínimo do formato binário** (LZ4/zstd, chunks INST/PROP, propriedade `Source`) e passaram pelo mesmo grep.\n",
       "## Resumo\n",
       "| Repositório | Commit | Status manual | Veredito |", "| --- | --- | --- | --- |"]
for key_raw, fn, status, verdict, sha in index_rows:
    idx.append(f"| [{key_raw}]({fn}) | `{sha}` | {status} | {verdict} |")
idx.append("\n## Principais achados\n")
idx.append("1. **Stoway: debug aberto em produção.** Qualquer jogador pode usar `/add <item> <qtd>` no chat (commit `ed64b7e46df8`). Também depende de um fork não oficial do Fusion (`acecateer/fusion`).")
idx.append("2. **ClientCast: confiança no cliente.** O servidor aceita o resultado do raycast do cliente sem validação geométrica.")
idx.append("3. **Wallstick e Character-Realism: remotes de retransmissão sem rate limit.** Wallstick também não valida tipos.")
idx.append("4. **Nenhum backdoor clássico encontrado:** nenhum `require(assetId)`, nenhum `loadstring` fora de libs de teste, nenhum webhook. A única chamada HTTP de saída é o comando admin `fetch` do Cmdr, bloqueado por padrão sem hook `BeforeRun`.")
idx.append("5. **Supply chain no Wally.** Há dezenas de re-uploads e forks de pacotes populares com escopos de terceiros (ex.: 24 escopos distintos publicam um pacote chamado `profilestore`). Fixe sempre o escopo do autor original e a versão exata.")
idx.append("6. **Repositórios vazios aparecem nas buscas.** `aziz8235/roblox-luau-game-framework` e `KURVOX/roblox-ai-npc` só têm README e LICENSE.")
open(os.path.join(OUT, 'README.md'), 'w').write('\n'.join(idx) + '\n')
print(len(index_rows), 'audits written')
