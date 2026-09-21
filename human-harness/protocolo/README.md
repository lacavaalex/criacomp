# Protocolo: quanto tempo entre o agente parar e você perceber

A OpenAI vendeu um aparelho de 230 dólares para resolver este problema e não publicou nenhum número. Nem eles nem ninguém. Isto aqui é uma tentativa de medir, feita para caber numa aula e para ser repetida por qualquer pessoa no próprio setup.

## A pergunta

**Quanto tempo passa entre um agente precisar de decisão e a pessoa perceber?**

E a pergunta que quase todo mundo esquece de fazer junto:

**Quanto custa essa percepção?**

## Antes de começar

Você precisa de **uma tarefa sua em primeiro plano**. Isto é o mais importante do protocolo e o mais fácil de errar.

Medir o tempo de percepção de quem está esperando o agente mede reflexo, não supervisão. A situação real é você tentando fazer outra coisa enquanto seis agentes rodam. Escolha algo que exija concentração: escrever, ler código, resolver um exercício.

## As quatro rodadas

Cada rodada dura 20 minutos, com os mesmos agentes rodando as mesmas tarefas.

| Rodada | Condição |
|---|---|
| **A** | Painéis visíveis, sem cor, sem som. Só olhar. |
| **B** | Cor de fundo por papel. |
| **C** | Som no evento de bloqueio. |
| **D** | Fora da tela: notificação de sistema, ou hardware se você tiver. |

## O que anotar

Para cada vez que um agente parou e esperou por você:

| campo | o que é |
|---|---|
| `t_bloqueio` | quando o agente entrou em espera |
| `t_percepcao` | quando você notou |
| `t_retomada` | quando você voltou à sua tarefa depois de resolver |
| `fazendo_o_que` | o que você estava fazendo no momento do bloqueio |
| `demorei_a_achar` | quanto tempo levou para lembrar onde você estava na sua tarefa |

Use `registro.csv`.

Os dois últimos campos são qualitativos e **valem mais que os números**. O campo `demorei_a_achar` é a versão caseira de um achado antigo de fatores humanos: depois de sair do circuito, o tempo que você gasta não é o de agir, é o de descobrir onde você estava.

## Como ler o resultado, sem se enganar

`t_percepcao` vai cair da rodada A para a D. **Isso é esperado e não é a descoberta.** Se você parar de medir aqui, você reproduziu o erro da indústria.

A descoberta está em duas outras contas:

**1. `t_retomada` menos `t_percepcao`.** É o custo de voltar. Pesquisa de interrupção em programação encontrou que só 10% das sessões de código recomeçam em menos de um minuto.

**2. O número total de interrupções na rodada.** Se a condição D fez você perceber mais rápido **e** ser arrancado da sua tarefa mais vezes, o dispositivo melhorou o indicador e piorou o seu dia.

> Perceber mais rápido e ser interrompido menos são objetivos opostos. Qualquer leitura que só olhe para o primeiro está torta.

## Carga percebida

Ao fim de cada rodada, responda de 1 a 10:

- quanto esforço mental a rodada exigiu
- quanto você se sentiu apressado
- quanto você se sentiu no controle
- quanto você acha que rendeu na **sua** tarefa

É uma versão curta e informal de um instrumento de carga de trabalho usado em fatores humanos. Não vale como medida científica e vale muito como comparação entre as suas próprias rodadas.

## Vira Peça de Portfólio sem esforço

O formato já responde às quatro perguntas:

- **o que você quis tentar**: medir se cor e som reduzem o tempo de perceber
- **o que usou**: seu setup, seus agentes, este protocolo
- **o que aconteceu**: a tabela, e principalmente o que deu errado na medição
- **o que aprendeu**: o que você faria diferente, e se o custo compensou

Resultado que contraria a expectativa é o melhor resultado possível aqui. A literatura não fechou esta questão.
