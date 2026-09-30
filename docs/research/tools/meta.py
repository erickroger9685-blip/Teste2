#!/usr/bin/env python3
"""Lookup GitHub repo metadata via repos.ecosyste.ms. Usage: meta.py owner/repo ... ; appends to meta.jsonl"""
import sys, json, urllib.request, urllib.parse, concurrent.futures, os
OUT = os.environ.get('META_OUT', 'meta.jsonl')
def get(full):
    url = "https://repos.ecosyste.ms/api/v1/hosts/GitHub/repositories/" + urllib.parse.quote(full, safe='')
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "genesis-research/1.0 (curl-compatible)"})
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.load(r)
        keep = {k: d.get(k) for k in ['full_name','description','archived','fork','pushed_at','stargazers_count','forks_count','open_issues_count','default_branch','last_synced_at','topics','language','license','tags_count','created_at','html_url','homepage']}
        keep['query'] = full
        return keep
    except Exception as e:
        return {'query': full, 'error': str(e)}
names = [a.strip() for a in sys.argv[1:] if a.strip()]
with concurrent.futures.ThreadPoolExecutor(8) as ex:
    res = list(ex.map(get, names))
with open(OUT, 'a') as f:
    for r in res:
        f.write(json.dumps(r) + "\n")
for r in res:
    if 'error' in r:
        print("ERR", r['query'], r['error'])
    else:
        print(f"{r['stargazers_count']}\t{r['full_name']}\t{r['license']}\t{(r['pushed_at'] or '')[:10]}\tarch={r['archived']}\tsync={(r['last_synced_at'] or '')[:10]}\t{(r['description'] or '')[:70]}")
