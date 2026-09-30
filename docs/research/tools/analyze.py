import os, re, subprocess, json, glob, sys
CL = os.environ.get('CLONES_DIR', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'clones'))
def sh(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True).stdout.strip()
LIC_PAT = [('MIT', r'Permission is hereby granted, free of charge'), ('Apache-2.0', r'Apache License'), ('MPL-2.0', r'Mozilla Public License'),
           ('GPL-3.0', r'GNU GENERAL PUBLIC LICENSE\s+Version 3'), ('LGPL', r'GNU LESSER GENERAL PUBLIC'), ('BSD', r'Redistribution and use in source and binary forms'),
           ('Unlicense', r'This is free and unlicensed software'), ('ISC', r'Permission to use, copy, modify, and/or distribute this software'), ('CC', r'Creative Commons')]
SEC = {
 'require_assetid': r'require\s*\(\s*\d{5,}',
 'getfenv_setfenv': r'\b(getfenv|setfenv)\s*\(',
 'loadstring': r'\bloadstring\s*\(',
 'HttpService': r'HttpService',
 'http_post': r'(PostAsync|RequestAsync|HttpService[.:]GetAsync|GetAsync\s*\(\s*["\']https?)',
 'webhook_discord': r'(discord(app)?\.com/api/webhooks|webhook)',
 'InsertService': r'InsertService',
 'TeleportService': r'TeleportService',
 'MarketplaceService': r'MarketplaceService',
 'kick': r':Kick\s*\(',
 'userid_whitelist': r'(UserId\s*==\s*\d{3,}|\.UserId\s*~=\s*\d{3,})',
 'string_char_obf': r'string\.char\s*\(\s*\d+\s*,\s*\d+\s*,\s*\d+',
 'long_escape_obf': r'(\\\d{2,3}){12,}',
 'OnServerEvent': r'OnServerEvent',
 'OnServerInvoke': r'OnServerInvoke',
}
out = {}
for d in sorted(os.listdir(CL)):
    p = os.path.join(CL, d)
    if not os.path.isdir(os.path.join(p, '.git')): continue
    r = {'repo': d.replace('_', '/', 1)}
    r['last_commit'] = sh("git log -1 --format=%cs", p)
    r['first_commit'] = sh("git log --reverse --format=%cs | head -1", p)
    r['commits'] = int(sh("git rev-list --count HEAD", p) or 0)
    r['contributors'] = int(sh("git log --format='%aN' | sort -u | wc -l", p) or 0)
    r['commits_last_12m'] = int(sh("git rev-list --count --since=2025-09-29 HEAD", p) or 0)
    r['tags'] = int(sh("git tag | wc -l", p) or 0)
    r['latest_tag'] = sh("git describe --tags --abbrev=0 2>/dev/null", p)
    lic_files = [f for f in os.listdir(p) if re.match(r'(?i)^(licen[sc]e|copying)', f)]
    r['license_files'] = lic_files
    lt = ''
    for f in lic_files:
        try: lt += open(os.path.join(p, f), errors='ignore').read()
        except: pass
    r['license_detected'] = [n for n, pat in LIC_PAT if re.search(pat, lt, re.I)]
    r['license_head'] = ' '.join(lt.split())[:160]
    files = sh("git ls-files", p).splitlines()
    code = [f for f in files if f.endswith(('.lua', '.luau'))]
    r['lua_files'] = len(code)
    loc = 0; strict = 0; nonstrict = 0; nocheck = 0
    hits = {k: [] for k in SEC}
    for f in code:
        try: t = open(os.path.join(p, f), errors='ignore').read()
        except: continue
        loc += t.count('\n')
        head = t[:300]
        if re.search(r'^\s*--!strict', t, re.M): strict += 1
        if '--!nonstrict' in head: nonstrict += 1
        if '--!nocheck' in head: nocheck += 1
        for k, pat in SEC.items():
            for m in re.finditer(pat, t, re.I if k == 'webhook_discord' else 0):
                ln = t.count('\n', 0, m.start()) + 1
                hits[k].append(f"{f}:{ln}")
    lp = os.path.join(p, '.luaurc'); mm = re.search(r'"languageMode"\s*:\s*"(\w+)"', open(lp).read()) if os.path.exists(lp) else None
    r['luaurc_mode'] = mm.group(1) if mm else None
    r['loc'] = loc; r['strict'] = strict; r['nonstrict'] = nonstrict; r['nocheck'] = nocheck
    r['sec'] = {k: v for k, v in hits.items() if v}
    r['binaries'] = [f for f in files if f.lower().endswith(('.rbxm', '.rbxl', '.rbxmx', '.rbxlx'))]
    r['manifests'] = [f for f in files if os.path.basename(f) in ('wally.toml','default.project.json','aftman.toml','rokit.toml','foreman.toml','selene.toml','stylua.toml','.stylua.toml','pesde.toml','package.json','.gitmodules','.luaurc','tsconfig.json')]
    r['tests'] = [f for f in files if re.search(r'(\.spec\.luau?$|\.test\.luau?$|(^|/)tests?/|jest\.config)', f)][:5]
    r['n_tests'] = len([f for f in files if re.search(r'(\.spec\.luau?$|\.test\.luau?$|(^|/)tests?/.*\.luau?$)', f)])
    r['ci'] = [f for f in files if f.startswith('.github/workflows/')]
    r['ts_files'] = len([f for f in files if f.endswith('.ts') and not f.endswith('.d.ts')])
    wally = [f for f in files if os.path.basename(f) == 'wally.toml']
    r['wally'] = {}
    for w in wally[:3]:
        t = open(os.path.join(p, w), errors='ignore').read()
        name = re.search(r'name\s*=\s*"([^"]+)"', t); ver = re.search(r'version\s*=\s*"([^"]+)"', t); lic = re.search(r'license\s*=\s*"([^"]+)"', t)
        deps = re.findall(r'^\s*(\w+)\s*=\s*"([a-z0-9_\-]+/[a-z0-9_\-]+@[^"]+)"', t, re.M)
        r['wally'][w] = {'name': name and name.group(1), 'version': ver and ver.group(1), 'license': lic and lic.group(1), 'deps': [d[1] for d in deps]}
    out[r['repo']] = r
json.dump(out, open(os.environ.get('ANALYSIS_OUT', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'evidence', 'analysis.json')), 'w'), indent=1)
for k, r in out.items():
    print(f"{k:42s} lic={','.join(r['license_detected']) or 'NONE'}({len(r['license_files'])}) last={r['last_commit']} c={r['commits']} c12m={r['commits_last_12m']} ppl={r['contributors']} tags={r['tags']} files={r['lua_files']} loc={r['loc']} strict={r['strict']} tests={r['n_tests']} ci={len(r['ci'])} bin={len(r['binaries'])} ts={r['ts_files']}")
