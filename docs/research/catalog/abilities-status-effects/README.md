# Habilidades, skills e status effects

> Brief §6: abilities, skills, spells, cooldowns, recursos, estados, targeting, cast time, channel, projéteis, AoE, buffs/debuffs, status effects, ultimates. É preciso suportar centenas de habilidades sem virar um monólito.

## Veredito

| Candidato | Licença | Situação | Decisão |
| --- | --- | --- | --- |
| **wad4444/WCS** | MIT | Melhor modelo conceitual, mas TS/Flamework com rede própria; 1 commit em 12m | 📖 referência de design ([ficha](../combat/README.md)) |
| CCL Custom Abilities API (oficial) | Termos Roblox | Studio Beta (2026-09-10); foco em **movimento**; `SyncedState` predito | 🛠️ usar para abilities de movimento quando sair do beta |
| Opxourc/statusify | MIT | Criado em 2026, 1 star | 📖 |
| WBlair1/StatusEffectManager | MIT | 2 stars; lifetime máximo de 30 s embutido | 📖 |
| Effectify (DevForum) | sem licença | bom modelo de stacking (Overwrite/Yield/Overlap) | ⛔ (só a ideia) |
| Thunder's Status Effects, Simple Status Effect Module (DevForum) | não verificados | pistas do gist | — |

**Não há runtime de habilidades em Luau, com licença, maduro e compatível com o Server Authority.** **Construir** um `AbilityRuntime` e um `StatusRuntime` orientados a dados, inspirados no vocabulário do WCS e nas regras de ativação do CCL.

## Desenho recomendado (construir)

```text
AbilityDefinition (dados em content/abilities/*.luau, validado por Lune+t)
  id, tags[], costs{energy, stamina, hp%}, cooldown, charges?, castTime?, channel?,
  targeting{mode=self|direction|lockOn|ground|cone|sphere, range},
  requires{statusAll[], statusNone[], states[]}, blocks[], cancels[],
  timeline[ {t=0.00, op="anim", id=...}, {t=0.12, op="hitbox", shape=..., damage=...},
            {t=0.20, op="projectile", ...}, {t=0.35, op="applyStatus", id="Burn", stacks=1} ],
  ultimate? { gauge }, transformOnly? { formId }

AbilityRuntime (servidor autoritativo, predito no cliente via BindToSimulation)
  CanActivate() → Activate() → executa timeline → emite eventos de domínio
StatusRuntime
  StatusDefinition { id, duration, tickRate?, stacking=refresh|add|independent|replace, maxStacks,
                     modifiers{stat→op}, tags[], onApply/onTick/onExpire (ops declarativas) }
```

- **Centenas de habilidades:** cada habilidade é **dado + (opcionalmente) um módulo de hook pequeno**. O motor é único.
- **Um pipeline de dano** (`DamageService`) para jogadores, NPCs, projéteis e status.
- **Cooldown:** o servidor grava `readyAt` (tempo do servidor) e o cliente só exibe.
- **VFX e animação** são eventos cosméticos disparados pela timeline e tocados no cliente (ver [VFX](../vfx/README.md)).
