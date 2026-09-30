# UI

> Brief §16: HUD, barras de vida e energia, quest UI, inventário, skills, criação de personagem, notificações, diálogo, menus, UI responsiva.

## Veredito

A categoria é madura. Há três bibliotecas reativas com licença MIT. **Escolher uma** e manter o resto como referência.

| Critério | **Vide** | Fusion | react-lua |
| --- | --- | --- | --- |
| Licença | MIT | MIT | MIT |
| Commits / autores | 207 / 25 | 933 / 53 | (não clonado) |
| Commits em 12 meses | 22 | 5 | NÃO VERIFICADO (último push 2025-05-23) |
| Último commit | 2026-09-28 | 2026-02-01 | push 2025-05-23 |
| Tipagem | strict no projeto (`.luaurc`) | strict no projeto (`.luaurc`) + 98/114 arquivos | — |
| Testes (arquivos) | 7 | 49 | — |
| Peso / modelo | leve, reatividade fina | reatividade fina, docs extensos | virtual DOM (React 17) |
| Integração com Charm | pacote `vide-charm` no repo do Charm | via adapters | pacote `react-charm` |

**Decisão:** ✅ **Vide + Charm (+ vide-charm)**. É o mais ativo, leve, strict e tem binding oficial com o Charm, que já foi escolhido para estado e replicação. **Fusion** fica como alternativa madura, se o time preferir a documentação dele.

| Função | Escolha | Licença | Decisão |
| --- | --- | --- | --- |
| UI de debug (só dev) | **SirMallard/Iris** | MIT | ✅ (desligar em produção) |
| Storybook | **flipbook** | MIT | ✅ ferramenta |
| Storybook alternativo | UI Labs | GPL-3.0 | 📖 só como ferramenta; nunca incorporar código |
| Ícones de topbar | TopbarPlus | MPL-2.0 + **cláusula de crédito** | 🛠️ só com o crédito na descrição do jogo |
| Motion de UI | spr (já escolhido) | MIT | ✅ |
| Componentes prontos | onyx-ui, Lydie (para Fusion) | MIT | 📖 |
| Legado | Roact | Apache-2.0 (arquivado) | ⛔ |

## Diretrizes

- UI **nunca** decide nada: lê atoms do Charm (sincronizados pelo servidor) e envia intenções pelo Blink.
- Responsivo: layout por `UIAspectRatioConstraint`/`UIScale` e testes em resoluções de mobile e console. O IAS fornece o mapeamento de gamepad e toque.
- Diálogos e quests: componentes alimentados pelos dados de `content/`, não por texto fixo no código.
