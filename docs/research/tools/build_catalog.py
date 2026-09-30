"""Build docs/research/data/catalog.csv and B-master-table.md from entries.py + evidence files.
Never estimates: missing values become 'NÃO VERIFICADO'."""
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
EVID = os.path.join(HERE, '..', 'data', 'evidence')
sys.path.insert(0, HERE)
from entries import E

REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.normpath(os.path.join(HERE, '..', '..', '..'))
OUT_CSV = os.path.join(REPO, 'docs/research/data/catalog.csv')
OUT_MD = os.path.join(REPO, 'docs/research/B-master-table.md')
VERIFIED_ON = '2026-09-29'
NV = 'NÃO VERIFICADO'

meta = json.load(open(os.path.join(EVID, 'meta_by_repo.json')))
analysis = {k.lower(): v for k, v in json.load(open(os.path.join(EVID, 'analysis.json'))).items()}
lite = json.load(open(os.path.join(EVID, 'lite.json')))
ungh = {k.lower(): v for k, v in json.load(open(os.path.join(EVID, 'ungh.json'))).items()}
LIVE_ARCH = {x.lower() for x in ['TeamSwordphin/ShapecastHitbox','prooheckcp/RoQuest','michaelvqq/RollbackHitbox','Brawldude2/RagdollService',
    'MaximumADHD/Character-Realism','EgoMoose/rbx-wallstick','MadStudioRoblox/ProfileStore','Sleitnick/RbxCameraShaker','Fraktality/spr',
    'wrello/Animations','zilibobi/forge-vfx','Pyseph/ObjectCache','Sleitnick/Knit','Roblox/testez','anthony0br/DocumentService','1Axen/blink',
    'Zyn-ic/Stoway','centau/vide','easy-games/chickynoid','grayzcale/simplepath','csqrl/sift','welcomestohell/prvdmwrong']}
# stars fetched directly from github.com pages (WebFetch, 2026-09-29) for repos not indexed by ecosyste.ms
GH_STARS = {'grayzcale/simplepath': 70, 'csqrl/sift': 92, 'welcomestohell/prvdmwrong': 36,
            'lab2securityprojectsr/inventory-logic-nogoodui': 0}

CAT_ORDER = ['tooling', 'core-frameworks', 'networking-security', 'combat', 'movement', 'abilities-status-effects',
             'transformations', 'npc-ai', 'quests', 'inventory-items-economy', 'persistence', 'character-customization',
             'camera', 'animation', 'vfx', 'ui', 'world-map', 'performance']
COLS = ['category', 'subcategory', 'project', 'url', 'source_type', 'license', 'license_evidence', 'stars', 'stars_source',
        'last_commit', 'archived', 'commits', 'contributors', 'releases_tags', 'wally', 'rojo', 'strict_typing', 'tests',
        'security_status', 'recommendation', 'notes', 'verified_on']

rows = []
for e in E:
    src = e.get('src', 'github')
    name = e['name']
    key = name.lower()
    url = e.get('url') or (f'https://github.com/{name}' if src == 'github' else '')
    m = meta.get(key); a = analysis.get(key); l = lite.get(key)
    r = dict(category=e['cat'], subcategory=e['sub'], project=name, url=url, source_type=src, license=e['lic'],
             license_evidence=e['lic_ev'], security_status=e['sec'], recommendation=e['rec'], notes=e['notes'],
             verified_on=VERIFIED_ON)
    if src != 'github':
        for c in ['stars', 'stars_source', 'last_commit', 'archived', 'commits', 'contributors', 'releases_tags', 'wally', 'rojo', 'strict_typing', 'tests']:
            r[c] = 'n/a'
        rows.append(r); continue
    # stars: live value from ungh.cc (GitHub API proxy); fallback ecosyste.ms snapshot
    u = ungh.get(key)
    if u and u.get('stars') is not None:
        r['stars'] = u['stars']; r['stars_source'] = 'ungh.cc (proxy da API do GitHub), 2026-09-30'
        if u.get('repo') and u['repo'].lower() != key:
            r['url'] = f"https://github.com/{u['repo']}"
            r['notes'] = r['notes'] + f" Repositório redirecionado: nome atual {u['repo']}."
    elif m and m.get('stargazers_count') is not None:
        r['stars'] = m['stargazers_count']; r['stars_source'] = f"ecosyste.ms (sync {str(m.get('last_synced_at'))[:10]})"
    else:
        r['stars'] = NV; r['stars_source'] = NV
    r['archived'] = ('sim' if m['archived'] else 'não') if m else NV
    if key in LIVE_ARCH: r['archived'] += ' (confirmado no GitHub 2026-09-30)'
    elif m: r['archived'] += f" (ecosyste.ms sync {str(m.get('last_synced_at'))[:10]})"
    if a:
        r['last_commit'] = a['last_commit'] + ' (git)'
        r['commits'] = a['commits']; r['contributors'] = a['contributors']; r['releases_tags'] = a['tags']
        r['wally'] = 'sim' if any(x.endswith('wally.toml') for x in a['manifests']) else 'não'
        r['rojo'] = 'sim' if any(x.endswith('default.project.json') for x in a['manifests']) else 'não'
        r['strict_typing'] = f"{a['strict']}/{a['lua_files']} arquivos" + (f" + .luaurc={a['luaurc_mode']}" if a.get('luaurc_mode') else '')
        r['tests'] = a['n_tests']
    elif l:
        r['last_commit'] = l['last_commit'] + ' (git)'
        r['commits'] = NV; r['contributors'] = NV
        r['releases_tags'] = NV
        r['wally'] = 'sim' if any(x.endswith('wally.toml') for x in l['manifests']) else 'não'
        r['rojo'] = 'sim' if any(x.endswith('default.project.json') for x in l['manifests']) else 'não'
        r['strict_typing'] = NV; r['tests'] = NV
    else:
        r['last_commit'] = (str(m['pushed_at'])[:10] + ' (último push, ecosyste.ms)') if m and m.get('pushed_at') else NV
        for c in ['commits', 'contributors', 'wally', 'rojo', 'strict_typing', 'tests']:
            r[c] = NV
        r['releases_tags'] = (f"{m['tags_count']} tags" if m and m.get('tags_count') is not None else NV)
    rows.append(r)

rows.sort(key=lambda r: (CAT_ORDER.index(r['category']), r['subcategory'], str(r['project']).lower()))
os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
with open(OUT_CSV, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=COLS)
    w.writeheader()
    for r in rows:
        w.writerow(r)

# ---- master table markdown
def short_rec(r):
    return {'READY TO INTEGRATE': '✅ READY TO INTEGRATE', 'REQUIRES ADAPTATION': '🛠️ REQUIRES ADAPTATION',
            'USE AS REFERENCE ONLY': '📖 USE AS REFERENCE ONLY', 'DO NOT USE': '⛔ DO NOT USE'}[r['recommendation']]
def activity(r):
    if r['source_type'] != 'github':
        return 'oficial/DevForum'
    lc = str(r['last_commit']).split(' ')[0]
    arch = ' · ARQUIVADO' if str(r['archived']).startswith('sim') else ''
    return f"{lc}{arch}" if lc != 'NÃO' else NV
def quality(r):
    if r['source_type'] != 'github':
        return '—'
    parts = []
    if r['commits'] not in (NV, 'n/a'): parts.append(f"{r['commits']} commits/{r['contributors']} autores")
    if r['strict_typing'] not in (NV, 'n/a'):
        st = r['strict_typing']
        parts.append('strict (projeto, .luaurc)' if '.luaurc=strict' in st else f"strict {st.split(' ')[0]}")
    if r['tests'] not in (NV, 'n/a'): parts.append(f"testes {r['tests']}")
    return '; '.join(parts) if parts else NV
def integration(r):
    if r['source_type'] != 'github':
        return 'API da plataforma' if r['source_type'] == 'roblox-official' else 'Creator Store/rbxm'
    p = []
    if r['wally'] == 'sim': p.append('Wally')
    if r['rojo'] == 'sim': p.append('Rojo')
    return '+'.join(p) if p else ('—' if r['wally'] == 'não' else NV)

CAT_TITLES = {'tooling': 'Tooling', 'core-frameworks': 'Core / frameworks', 'networking-security': 'Rede & segurança',
    'combat': 'Combate', 'movement': 'Movimento', 'abilities-status-effects': 'Habilidades & status', 'transformations': 'Transformações',
    'npc-ai': 'NPC / IA', 'quests': 'Quests', 'inventory-items-economy': 'Inventário / itens / economia', 'persistence': 'Persistência',
    'character-customization': 'Customização de personagem', 'camera': 'Câmera', 'animation': 'Animação', 'vfx': 'VFX', 'ui': 'UI',
    'world-map': 'Mundo / mapa', 'performance': 'Performance'}

counts = {}
for r in rows:
    counts[r['recommendation']] = counts.get(r['recommendation'], 0) + 1
lines = []
lines.append('# Seção B — Master Table\n')
lines.append(f'> Gerada automaticamente a partir de [`data/catalog.csv`](data/catalog.csv) (fonte única de verdade). Dados coletados em **{VERIFIED_ON}**. '
             'Nenhum valor foi estimado: o que não foi verificado aparece como **NÃO VERIFICADO**.\n')
lines.append('**Como ler as colunas**\n')
lines.append('- **Stars**: valor ao vivo via ungh.cc (proxy da API do GitHub) em 2026-09-30. É só um indicador de popularidade, **não de qualidade**.')
lines.append('- **Atividade**: data do último commit na branch padrão (via `git clone`). Quando não houve clone, é o último push segundo o ecosyste.ms.')
lines.append('- **Qualidade**: fatos objetivos do clone (nº de commits e de autores, arquivos `--!strict` sobre o total de arquivos Luau, arquivos de teste). A leitura qualitativa de cada projeto está nas fichas de `catalog/`.')
lines.append('- **Integração**: se o projeto tem manifesto Wally e/ou projeto Rojo.')
lines.append('- **Recomendação**: segue os critérios de [`00-methodology/evaluation-criteria.md`](00-methodology/evaluation-criteria.md).\n')
lines.append(f"**Totais ({len(rows)} candidatos):** " + ' · '.join(f"{k}: {v}" for k, v in sorted(counts.items())) + '\n')
for cat in CAT_ORDER:
    cr = [r for r in rows if r['category'] == cat]
    if not cr:
        continue
    lines.append(f'\n## {CAT_TITLES[cat]}\n')
    lines.append('| Categoria | Projeto | URL | Licença | Stars | Atividade | Qualidade | Integração | Recomendação |')
    lines.append('| --------- | ------- | --- | ------- | ----: | --------- | --------- | ---------- | ------------ |')
    for r in cr:
        url = r['url']
        lines.append(f"| {r['subcategory']} | {r['project']} | [link]({url}) | {r['license']} | {r['stars']} | {activity(r)} | {quality(r)} | {integration(r)} | {short_rec(r)} |")
    if cat == 'transformations':
        pass
lines.append('\n## Transformações\n')
lines.append('Nenhum candidato reutilizável foi encontrado (buscas no GitHub, no Wally e no DevForum). **Construir do zero** sobre o runtime de habilidades e status. Ver [`catalog/transformations/`](catalog/transformations/README.md).\n')
open(OUT_MD, 'w').write('\n'.join(lines) + '\n')
print(len(rows), 'rows;', counts)
