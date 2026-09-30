# Criação e customização de personagem

> Brief §3 e §12: criação, aparência, corpo, cabelo, acessórios, roupas, cores, rosto, aura, cosméticos, e o sistema genético (Origin/Race → Bloodline → Gene → Mutation → Potential).

## Veredito

| Candidato | Licença | Decisão |
| --- | --- | --- |
| **HumanoidDescription / AvatarEditorService / criação no jogo (oficial)** | Termos Roblox | ✅ base ([docs](https://create.roblox.com/docs/characters/appearance)) |
| vocksel/Sugar (merge de HumanoidDescription) | MIT, 2019 | 📖 |
| MaximumADHD/Character-Realism | MPL-2.0 | 🛠️ polish opcional (olhar/cabeça) |
| Sistemas de "character creator" da comunidade | — | nenhum com licença e manutenção encontrado |

**Não existe sistema de criação de personagem reutilizável e maduro.** O sistema **genético e de raridade** é identidade do jogo e deve ser **construído**:

```text
GeneticsDefinition (content/genetics/*.luau)
  origins[]    { id, baseStats, allowedBloodlines[], appearanceRules }
  bloodlines[] { id, rarity, genePool[{geneId, weight}], formTrees[], abilityTrees[] }
  genes[]      { id, rarity, effects{...}, mutationChances[{mutationId, weight}] }
  potential    { curve, caps por atributo, crescimento por idade }

RngService (servidor): rolls com semente registrada no perfil (auditável e reproduzível), nunca no cliente.
Appearance: preset base por Origin + escolhas do jogador validadas no servidor → HumanoidDescription.
```

Pontos de atenção: roupas e acessórios do catálogo têm regras próprias ([IP licensing](https://create.roblox.com/docs/ip-licensing/creators) e Marketplace). Para a IP original, criar os próprios assets (ver [assets](../../assets/README.md)).
