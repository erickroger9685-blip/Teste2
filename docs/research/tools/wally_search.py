import json, urllib.request, urllib.parse, sys, concurrent.futures
kws = sys.argv[1:]
def s(k):
    u = "https://api.wally.run/v1/package-search?query=" + urllib.parse.quote(k)
    req = urllib.request.Request(u, headers={"User-Agent":"genesis-research/1.0"})
    try:
        return k, json.load(urllib.request.urlopen(req, timeout=60))
    except Exception as e:
        return k, str(e)
with concurrent.futures.ThreadPoolExecutor(6) as ex:
    for k, res in ex.map(s, kws):
        print(f"\n## {k}")
        if isinstance(res, str): print("ERR", res); continue
        for p in res:
            print(f"  {p['scope']}/{p['name']} v{p['versions'][0] if p['versions'] else '?'} ({len(p['versions'])} vers) - {(p.get('description') or '')[:90]}")
