"""Minimal Roblox binary model (.rbxm/.rbxl) script extractor, for audit only.
Usage: rbxm_dump.py file.rbxm outdir  -> writes each script Source to outdir/<Class>_<idx>_<Name>.lua and prints class counts."""
import sys, struct, os, re, lz4.block, zstandard
def rstr(b, o):
    n = struct.unpack_from('<I', b, o)[0]; o += 4
    return b[o:o+n], o+n
data = open(sys.argv[1], 'rb').read()
out = sys.argv[2]; os.makedirs(out, exist_ok=True)
assert data[:8] == b'<roblox!', 'not binary rbxm'
o = 8 + 6 + 2 + 4 + 4 + 8
classes = {}; props = {}
while o < len(data):
    name = data[o:o+4]; clen, ulen = struct.unpack_from('<II', data, o+4); o += 16
    if clen == 0:
        chunk = data[o:o+ulen]; o += ulen
    else:
        raw = data[o:o+clen]; o += clen
        chunk = zstandard.ZstdDecompressor().decompress(raw, max_output_size=ulen) if raw[:4] == b'\x28\xb5\x2f\xfd' else lz4.block.decompress(raw, uncompressed_size=ulen)
    if name == b'INST':
        cid = struct.unpack_from('<I', chunk, 0)[0]; cname, p = rstr(chunk, 4); p += 1
        cnt = struct.unpack_from('<I', chunk, p)[0]
        classes[cid] = (cname.decode(errors='replace'), cnt)
    elif name == b'PROP':
        cid = struct.unpack_from('<I', chunk, 0)[0]; pname, p = rstr(chunk, 4); t = chunk[p]; p += 1
        if t == 0x01 and pname in (b'Source', b'Name'):
            cnt = classes.get(cid, ('?', 0))[1]; vals = []
            for _ in range(cnt):
                v, p = rstr(chunk, p); vals.append(v.decode(errors='replace'))
            props[(cid, pname.decode())] = vals
    elif name == b'END\x00':
        break
counts = {}
for cid, (cname, cnt) in classes.items():
    counts[cname] = counts.get(cname, 0) + cnt
    srcs = props.get((cid, 'Source'))
    if srcs:
        names = props.get((cid, 'Name'), [''] * len(srcs))
        for i, s in enumerate(srcs):
            fn = re.sub(r'[^A-Za-z0-9_.-]', '_', f"{cname}_{i}_{names[i]}")[:120] + '.lua'
            open(os.path.join(out, fn), 'w').write(s)
print(sorted(counts.items(), key=lambda x: -x[1]))
