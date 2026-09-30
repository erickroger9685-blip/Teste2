# Seção E.1 — NPC / IA

> Escopo: framework de NPC, IA inimiga e de combate, pathfinding, patrulha, aggro, seleção de alvo, perseguição, decisão de ataque, IA de chefe, FSM/behavior trees, NPCs de treino, mercado e quest, e escala (muitos NPCs).

## Veredito da categoria

- **Pathfinding:** resolvido pela API oficial `PathfindingService` + **SimplePath** (MIT, pequeno, maduro).
- **Behavior trees:** as opções clássicas são **GPL-3.0** (BehaviorTree3) ou **sem licença** (behaviortree.rbxlua). Não há BT permissiva e madura, então é preciso **construir** (uma BT leve ou utility AI é algo pequeno).
- **Framework de NPC completo com escala:** não encontrado com licença e maturidade. Repositórios que prometem isso estão vazios (KURVOX) ou são pacotes Wally novos e não auditados (`ppeter2/npc-engine`, fora do catálogo).
- **Escala:** a base viável é **jecs** (ECS, MIT, 860 commits, 54 autores) + **Parallel Luau** + StreamingEnabled + LOD de IA, tudo integrado por código próprio.
- **CCL:** o suporte a NPC está "coming soon". Até lá, NPCs usam Humanoid/ControllerManager diretamente.

**Decisão:** **construir** o `NpcRuntime` (brains orientados a dados), **reutilizar** SimplePath e PathfindingService, e **avaliar jecs** a partir da Fase 5, com benchmark.

---

### Projeto: grayzcale/simplepath
- **URL:** https://github.com/grayzcale/simplepath (redireciona para o nome atual `ahmicy/simplepath`) · docs: https://blackinkq.github.io/simplepath/
- **Licença:** MIT (clone) · 70 stars (ungh.cc, 2026-09-30) · 176 commits · 10 autores · último commit 2026-06-11 · 5 tags · CI com TestEZ
- **Arquitetura:** um ModuleScript (~450 linhas) sobre `PathfindingService`; eventos `Reached`, `WaypointReached`, `Blocked`, `Error`; funciona com Humanoid e com modelos sem Humanoid.
- **Pontos fortes:** pequeno, estável e amplamente usado (outros módulos como o NoobPath declaram compatibilidade com a API dele).
- **Problemas:** o original não tem suporte a `ControllerManager` (existe um fork no Wally, `tabby0x/simplepath`, não auditado). É distribuído por release ou modelo, sem `wally.toml` no repo.
- **Compatibilidade:** ✅ **READY TO INTEGRATE**, atrás de um `PathAdapter`.
- **Integração (§25):** o brain do NPC pede `MoveTo(goal)` → `PathAdapter` → SimplePath. Não depende de nada além de PathfindingService. O conflito possível é com o controle de movimento do CCL quando ele suportar NPCs; o adapter isola essa troca.

### Projeto: Ukendio/jecs
- **URL:** https://github.com/Ukendio/jecs · **Licença:** MIT
- **Maturidade:** 860 commits, 54 autores, 63 tags, 92 commits em 12 meses, testes e CI.
- **Recursos:** ECS por arquétipos, relacionamentos entre entidades, queries em cache; o README declara "800.000 entidades a 60 FPS" (benchmark do autor, não reproduzido aqui).
- **Compatibilidade:** 🛠️ **REQUIRES ADAPTATION**. Mudar o modelo de dados de NPCs, projéteis e status para ECS é decisão arquitetural; justifica-se se o profiling mostrar gargalo em centenas de NPCs por servidor. A replicação (replecs) precisa ser avaliada contra o Server Authority nativo.

### Behavior trees: por que não reutilizar

| Projeto | Licença | Motivo |
| --- | --- | --- |
| Defaultio/BehaviorTree3 (+ editor visual BTrees) | **GPL-3.0** | Copyleft forte, incompatível com código fechado |
| howmanysmall / seyaidev `behaviortree.rbxlua` | **sem licença** | NÃO CONFIRMADO |
| `thunn/behavior-tree`, `axp3cter/arbor` (Wally) | não verificado | Pistas para uma segunda rodada |

### Outros

| Projeto | Licença | Decisão |
| --- | --- | --- |
| NoobPath (DevForum/Creator Store) | sem licença | ⛔ |
| kozuidev/PathForge (A* em grid) | sem licença | ⛔ |
| imezx/JPSPlus (Jump Point Search) | LGPL-3.0 | ⛔ no runtime |
| KURVOX/roblox-ai-npc | MIT, **sem código** | ⛔ |
| Gzeu/roblox-procedural-worlds `MobAI.lua` (cone de visão, audição, memória) | MIT | 📖 referência de percepção |

## Arquitetura recomendada de NPC (construir)

```text
NpcDefinition (dados)  ──►  NpcRuntime (servidor)
  arquétipo, stats,          ├─ Perception (visão/audição/aggro, spatial hash/octree)
  brain, loot, diálogo       ├─ Brain: FSM curta + utility scoring (ataque/defesa/fuga/skill)
                             ├─ Locomotion: PathAdapter (SimplePath) → Humanoid/ControllerManager
                             ├─ Combat: usa o MESMO AbilityRuntime/CombatService dos jogadores
                             └─ LOD: tick rate por distância ao jogador mais próximo; dormir fora do streaming
Boss = NpcDefinition + fases (thresholds de HP) + padrões de ataque em dados
Trainer/Merchant/Quest NPC = NpcDefinition com componentes de interação (sem brain de combate)
```

Pontos centrais: **NPCs usam exatamente o mesmo pipeline de habilidades e dano dos jogadores** (sem sistema paralelo). O tick da IA é escalonado (budget por frame) e as queries pesadas podem ir para Actors (Parallel Luau).
