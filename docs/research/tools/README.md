# Ferramentas da pesquisa (reprodutibilidade)

São scripts auxiliares da **pesquisa**, não código do jogo. Com eles dá para regenerar o catálogo e as auditorias a partir das evidências salvas em [`../data/evidence/`](../data/evidence/).

| Script | Função | Precisa de rede? |
| --- | --- | --- |
| `entries.py` | Curadoria manual: categoria, recomendação, licença verificada, status de segurança e notas de cada candidato | não |
| `build_catalog.py` | Junta `entries.py` com as evidências e gera `data/catalog.csv` + `B-master-table.md` | não |
| `build_audits.py` | Gera `security-audits/*.md` a partir de `analysis.json` e das notas de revisão manual | não |
| `analyze.py` | Mede os clones: LICENSE, commits, autores, tags, `--!strict`/`.luaurc`, testes, CI, binários, grep de segurança → `analysis.json` | não (usa clones locais em `CLONES_DIR`) |
| `rbxm_dump.py` | Extrator mínimo de scripts de arquivos binários `.rbxm`/`.rbxl`, para auditar código distribuído só em binário | não (requer `pip install lz4 zstandard`) |
| `meta.py` | Consulta metadados no ecosyste.ms | sim |
| `wally_search.py` | Busca no registro Wally | sim |

## Regenerar

```bash
python3 docs/research/tools/build_catalog.py   # CSV + tabela mestre
python3 docs/research/tools/build_audits.py    # notas de auditoria
```

Para refazer a medição dos repositórios, clone-os **fora do repositório**, com `git clone --filter=blob:none https://github.com/<owner>/<repo> <owner>_<repo>`, e rode:

```bash
CLONES_DIR=/caminho/dos/clones python3 docs/research/tools/analyze.py
```

As evidências em `data/evidence/`:

- `analysis.json`: métricas dos 49 clones (2026-09-29/30).
- `ungh.json`: stars ao vivo via ungh.cc (2026-09-30).
- `meta_by_repo.json`: snapshot do ecosyste.ms (arquivamento, último push, datas de sync).
- `lite.json`: clones rasos (LICENSE e último commit).
- `extra.txt`: SHA auditado, submódulos e código vendorizado de cada clone.
