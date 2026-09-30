# Política de licenças (brief §21)

> Não é aconselhamento jurídico. Esta política serve para tomar decisões de engenharia. Os casos marcados como **revisão jurídica** precisam de parecer antes do lançamento comercial.

## Regra de ouro

**Um projeto público não pode ser usado comercialmente só por estar público.** Sem licença explícita, a classificação é:

> **NÃO CONFIRMADO — NÃO USAR ATÉ VERIFICAR**

Isso vale também para "open source" dito num post do DevForum sem texto de licença, para "free to use", para modelos do Creator Store sem licença no código e para places "uncopylocked". Deixar um place copiável não concede licença sobre o código ou os assets dele.

## Classificação usada no catálogo

| Licença | Uso no runtime do jogo | Obrigações | Situação no catálogo |
| --- | --- | --- | --- |
| **MIT / ISC / BSD / Unlicense / CC0** | ✅ Permitido | Manter aviso de copyright/licença (MIT/BSD/ISC) | Maioria dos candidatos |
| **Apache-2.0** | ✅ Permitido | Manter LICENSE e NOTICE; indicar modificações | ProfileStore, Replica, RoQuest (LICENSE), purse |
| **MPL-2.0** | ✅ Permitido com cuidado | Copyleft **por arquivo**: modificações em arquivos MPL precisam ficar disponíveis em fonte | Rojo/Wally/Selene/StyLua/Lune (ferramentas; não entram no jogo), Satchel, Character-Realism, prvdmwrong, hoarcekat |
| **MPL-2.0 + cláusula extra** | ⚠️ Revisão | TopbarPlus exige manter o atributo **ou** creditar na descrição do jogo | TopbarPlus |
| **LGPL-2.1/3.0** | ⛔ Evitar no runtime | Exige permitir relink/substituição da biblioteca, o que é impraticável num jogo Roblox | JPSPlus, Pronghorn (runtime). Lync é só ferramenta. |
| **GPL-3.0** | ⛔ Não usar no runtime | Copyleft forte; incompatível com código fechado | BehaviorTree3, UI Labs (plugin: ok usar a ferramenta, nunca incorporar o código) |
| **CC BY-NC-ND** | ⛔ Não usar | Proíbe uso comercial e derivados | Arte/logos do FastCast2 (o código é MIT) |
| **Custom** | ⚠️ Revisão jurídica | Ler caso a caso | forge-vfx (VFX-DL-1.1: só em jogos Roblox, derivados com a mesma licença, uso comercial permitido); DataStore2 (licença própria do autor) |
| **Proprietária** | ⛔ Não usar | — | inventory-logic-NoGoodUi ("PORTFOLIO EVALUATION ONLY") |
| **Research-only (RAIL)** | ⛔ Não usar p/ produção | — | Roblox/cube (Cube3D: "RESEARCH-ONLY RAIL-MS LICENSE") |
| **Sem licença** | ⛔ NÃO CONFIRMADO | — | 22 entradas do catálogo (repositórios e posts do DevForum) |

## Divergências encontradas (verificar antes de usar)

| Projeto | Divergência | Ação |
| --- | --- | --- |
| prooheckcp/RoQuest | README diz MIT e o arquivo LICENSE é Apache-2.0 | Tratar como Apache-2.0 (a mais restritiva das duas) e pedir confirmação ao autor |
| Brawldude2/RagdollService | LICENSE atual é MIT (alterada em 2026-03-04/16); o ecosyste.ms ainda indica LGPL-3.0 | Fixar a versão adotada e guardar cópia da LICENSE daquele commit |
| michaelvqq/RollbackHitbox | Sem licença até 2026-07-09, quando recebeu MIT | Usar só commits a partir de 2026-07-09 |
| wad4444/WCS | Post do DevForum não cita licença; o repositório tem `LICENSE.txt` MIT; o pacote Wally está sob o escopo `cheetiedotpy` | Confirmar que o escopo Wally pertence ao mesmo autor antes de instalar |

## Dependências, submódulos e assets de terceiros

A licença do repositório **não cobre automaticamente**:

- **dependências vendorizadas:** RoQuest (Red, Promise, Signal, Trove), RobloxStateMachine (Signal, Trove), TopbarPlus (GoodSignal, Janitor), Chickynoid (vários em `Vendor/`), Rewind (Packages/_Index);
- **submódulos:** forge-vfx (`kohltastrophe/Z`, `dphfox/tiniest`), charm (gist do autor), t e simplepath (TestEZ, só dev);
- **assets dentro de `.rbxl`/`.rbxm`:** animações, meshes, sons e texturas podem ter proveniência diferente do código. Exemplo: o `.rbxl` do MaxDevLol Parkour tem ~186 `KeyframeSequence` sem proveniência documentada;
- **créditos obrigatórios:** TopbarPlus (cláusula de crédito), CC-BY (quando houver), NOTICE de projetos Apache.

**Processo:** antes de adicionar qualquer pacote ao `wally.toml`, registre na tabela de terceiros do projeto (a ser criada na Fase 1, ver [plano](../implementation-plan.md)) o nome, a versão exata, o escopo, a licença, o commit, as dependências transitivas e o link da auditoria.
