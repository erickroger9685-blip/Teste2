# Performance

> Brief §18: object pooling, VFX pooling, otimização de NPCs, particionamento espacial, LOD, streaming, eventos, memória, cleanup, conexões e scheduling. Alvo: PC, mobile e console.

| Necessidade | Solução | Licença | Decisão |
| --- | --- | --- | --- |
| Pooling de Parts/Models | **Pyseph/ObjectCache** | MIT | ✅ |
| Cleanup e conexões | **Trove** (RbxUtil) | MIT | ✅ (um único padrão de cleanup) |
| Signals | **Signal** (RbxUtil) | MIT | ✅ |
| ECS para entidades em massa | **jecs** (+ planck como scheduler, opcional) | MIT | 🛠️ decidir com benchmark (Fase 5/10) |
| Paralelismo | **Parallel Luau / Actors** (oficial) | Termos Roblox | ✅ para percepção de NPC, pathfinding em lote, projéteis (FastCast2 já usa) |
| Streaming | **StreamingEnabled** (oficial) | Termos Roblox | ✅ obrigatório sob Server Authority |
| Particionamento espacial | Octree (Nevermore) / octo-tree | MIT | 📖 → implementar ou vendorizar após auditoria |
| Rede | Blink (buffers, batching) | MIT | ✅ |
| Profiling | MicroProfiler, Script Profiler e visualizador do Server Authority (`Ctrl+Shift+F6`) | oficial | ✅ |

## Anti-padrões encontrados nos candidatos (evitar no Genesis)

- **Uma conexão `PostSimulation` por hitbox ativa** (ShapecastHitbox): trocar por loop central.
- **Um handler `OnServerEvent` por instância** num remote compartilhado (ClientCast): usar um dispatcher.
- **`FireAllClients` retransmitindo payload do cliente sem rate limit** (Wallstick, Character-Realism): spam e amplificação.
- **Criar VFX no servidor**: o refx documenta o padrão correto (só cliente).

## Orçamentos iniciais sugeridos (validar em protótipo)

- Scheduler central com budget por frame para IA (tick por distância: perto 10 Hz, médio 4 Hz, longe dormindo).
- Limite de partículas por cue e qualidade de VFX por classe de dispositivo.
- Nenhum `while true do wait()`: tudo por `Scheduler` ou eventos.
