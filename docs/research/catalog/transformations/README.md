# Transformações

> Brief §7: mudança de atributos, aparência, VFX, animações, duração, energia, cooldown, habilidades desbloqueadas, transformação progressiva, tudo definido por configuração.

## Veredito

**Nenhum candidato reutilizável encontrado.** As buscas no GitHub, no registro Wally e no DevForum (transformation, form, awakening, mode) só retornaram exemplos acoplados a jogos específicos, sem licença, ou nada relevante. **Construir do zero**. É a área que mais depende da identidade original do Genesis, e o custo é baixo quando o runtime de habilidades e status já existe.

## Desenho recomendado

A transformação é um **status effect especial** (`kind = "Form"`), então herda duração, stacking, custos e cancelamento do `StatusRuntime`:

```text
FormDefinition (content/forms/*.luau)
  id, tier, requires{ bloodline?, gene?, mutation?, level, questFlag? },
  costs{ activateEnergy, drainPerSecond }, duration? (nil = até energia acabar), cooldown,
  statModifiers{ strength=+x%, speed=+y, ... },
  appearance{ humanoidDescriptionPatch?, accessoriesAdd[], materialOverrides[], auraVfxId },
  animationSet?, abilityGrants[], abilityRevokes[],
  stages[ {at=0, ...}, {at=30s, ...} ]   -- transformação progressiva
  onExit{ exhaustion status, cooldown }
```

- **Aparência:** aplicar `HumanoidDescription` (oficial) ou acessórios no servidor. Aura e VFX só no cliente.
- **Progressão genética:** `requires` lê o perfil genético do jogador (Origin → Bloodline → Gene → Mutation → Potential). Raridade **abre caminhos** (formas e árvores distintas), não multiplica dano.
- **Risco:** mudanças de rig ou escala interagem com o CCL e as hitboxes; testar em protótipo na Fase 4.
