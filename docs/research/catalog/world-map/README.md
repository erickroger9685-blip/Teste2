# Seção F.1 — Mundo e mapa: OPEN SOURCE CODE

> Brief §17: frameworks de mundo aberto, regiões e zonas, streaming, terreno e geração procedural, portais, teleporte, transições, dungeons, cavernas, cidades e ambientes.
> **Assets** (mapas, construções, texturas, sons) têm outro regime de licença e estão em [`../../assets/README.md`](../../assets/README.md).

## Veredito

Não existe "framework de mundo aberto" maduro com licença limpa. A base é **oficial**, e o que falta é código próprio (pequeno):

| Necessidade | Solução | Licença | Decisão |
| --- | --- | --- | --- |
| Streaming de mundo grande | **StreamingEnabled** (obrigatório sob Server Authority) + `ModelStreamingMode` por modelo | Termos Roblox | ✅ |
| Reinos separados (Spiritual, Celestial, Abyss, Void) | **Places do mesmo universo** + `TeleportService` (com `TeleportData` validado no destino) | Termos Roblox | ✅ |
| Regiões, zonas e perigo | 1ForeverHD/ZonePlus | MIT; último commit 2024-02; sem strict | 📖 → **construir** `RegionService` com spatial queries/octree e dados de região (nível de perigo, bioma, música, spawns) |
| Terreno procedural | Gzeu/roblox-procedural-worlds | MIT; 1 autor; criado em 2026; builder offline em Python + módulos "kitchen-sink" | 📖 referência (biomas, FBM, cavernas, chunks) |
| Terreno procedural | TheArturZh/RTerrainGenerator | MIT; 2020 | 📖 |
| Dungeons e cavernas | geradores do repositório Gzeu (salas + corredores) | MIT | 📖 |
| Octree / spatial hash | Nevermore Octree; `sleitnick/octo-tree` (Wally) | MIT | 📖 → usar em Perception de NPC e RegionService |

## Recomendação de arquitetura de mundo

```text
Universo Genesis
├── Place "Overworld" (mundo contínuo; StreamingEnabled; regiões de risco baixo/médio/extremo)
├── Place "Spiritual Realm"   ┐
├── Place "Celestial Realm"   ├─ entrada por portais (TeleportService), estado do jogador salvo antes
├── Place "Abyss Realm"       │  do teleporte; destino revalida tudo (nunca confia em TeleportData)
└── Place "Void Realm"        ┘
RegionDefinition (content/regions/*.luau): bounds, dangerTier, recommendedLevel, spawns[], music, ambience, discoverFlag
```

- **Comunicação de perigo** (brief §2): ao entrar numa região de tier alto, a UI avisa (nível recomendado, cor, música) mas **não bloqueia** o jogador.
- **Procedural vs. feito à mão:** para um mundo com identidade, o recomendado é terreno **feito à mão com ferramentas** (editor de terreno oficial e geração assistida offline via Lune), não geração em runtime. A geração em runtime fica restrita a dungeons ou cavernas instanciadas.
