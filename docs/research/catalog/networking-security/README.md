# Rede e segurança

## Veredito

Duas mudanças oficiais de 2026 reorganizam esta categoria:

1. **[Server Authority](https://create.roblox.com/docs/projects/server-authority)**: `Workspace.AuthorityMode = Server`. Ativa automaticamente `NextGenerationReplication`, `PlayerScriptsUseInputActionSystem`, `SignalBehavior = Deferred`, `UseFixedSimulation` e `StreamingEnabled`. A lógica de jogo roda em `RunService:BindToSimulation()` nos dois lados; o cliente prediz e faz rollback; o estado predito vive em **atributos**. A documentação o descreve como pronto para produção, e a Roblox o anunciou publicamente em 2026-07-09.
2. **[Input Action System](https://create.roblox.com/docs/input/input-action-system)**: `InputContext` e `InputAction` cross-platform. Full release em junho de 2026. Sob Server Authority, **inputs que afetam a simulação devem vir do IAS**, não do `UserInputService`.

Com isso, **dano, cooldowns e movimento autoritativo com resposta imediata** passam a ser da engine. Bibliotecas de rede continuam necessárias para **eventos discretos** (UI, quests, inventário, chat de NPC, VFX cosméticos). A documentação avisa que RemoteEvents **não são ordenados em relação às atualizações de propriedades**.

| Função | Escolha | Licença | Evidência | Decisão |
| --- | --- | --- | --- | --- |
| Autoridade, predição e rollback | **Server Authority (oficial)** | Termos Roblox | docs + newsroom 2026-07-09 | ✅ fundação (fazer spike na Fase 1) |
| Input cross-platform | **IAS (oficial)** | Termos Roblox | full release 2026-06 | ✅ |
| Eventos discretos tipados | **1Axen/blink** | MIT | 489 commits, 16 autores, 91 tags, 42 commits em 12m, strict no projeto | ✅ READY |
| Alternativa IDL | red-blox/zap | MIT | 334 commits, 22 autores, último 2026-06 | 📖 (equivalente; escolher UM) |
| Validação runtime | **osyrisrblx/t** | MIT | 302 commits, 19 autores; estável | ✅ READY (configs e payloads complexos) |
| Rate limiting | — | — | nenhum módulo licenciado e maduro encontrado | **Construir** (token bucket por jogador e por evento; poucas dezenas de linhas) |
| Lag compensation (à distância) | michaelvqq/RollbackHitbox | MIT (desde 2026-07-09) | 10 commits | 🛠️ só para hitscan e projéteis |
| Anti-cheat | — | — | módulos avulsos (TAC etc.) pouco usados | **Construir** a partir da autoridade do servidor e da telemetria |

## Por que Blink

- **Compatibilidade:** gera um módulo Luau por contrato (`net/*.blink`). Os serviços chamam funções tipadas e não há `RemoteEvent` exposto no código de jogo. Isso centraliza a fronteira de confiança num lugar só.
- **Segurança:** o código gerado valida tipos e tamanhos na desserialização do servidor, antes de chegar ao handler.
- **Maturidade e atividade:** é o mais ativo entre os IDLs (42 commits nos últimos 12 meses contra 17 do Zap e 0 do ByteNet).
- **Performance:** serialização em `buffer` e batching.
- **Risco:** o código gerado precisa ser **commitado e revisado** (diff) a cada atualização do compilador.

## Descartados

ByteNet (sem commits em 12m), BridgeNet2 (predecessor), Red (2024-02), rbx-net (orientado a TS), Warp, NetRay, Packet (só Creator Store, com vulnerabilidades relatadas pela comunidade), `mrchigurh/Suphi-Packet` (mirror de terceiro sem licença).

## Regras de fronteira de confiança (Genesis)

1. O cliente envia **intenções** (`UseAbility(id, aimDir)`, `EquipItem(uuid)`, `AcceptQuest(id)`), nunca resultados.
2. Todo handler faz: rate limit → validação de tipo (gerada) → validação semântica (estado, distância, posse, cooldown) → ação.
3. XP, moeda, itens, raridade, rolls, dano e recompensas são calculados **só** no servidor, por serviços únicos (`DamageService`, `RewardService`, `RngService`).
4. Retransmissão para outros clientes só com payload **gerado pelo servidor**.
