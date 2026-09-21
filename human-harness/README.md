# Human harness: posto de supervisão de agentes

Configuração mínima e comentada para montar um posto de trabalho onde uma pessoa conduz vários agentes ao mesmo tempo, mais o protocolo para medir se isso está funcionando.

Material da aula sobre **interação humano-agente** de Criatividade Computacional 2026.2.

## A ideia em uma frase

O *harness* de um agente é o andaime em volta do modelo: prompt, contexto, ferramentas, runtime. O **human harness** é o andaime em volta da pessoa: o que ela vê, onde ela decide, o que consegue interromper e como retoma depois de sair.

Só um dos dois vem sendo projetado. Isto aqui é uma tentativa de projetar o outro.

## O que tem aqui

| pasta | o que é |
|---|---|
| `tmux/` | a configuração do posto, com cor por papel e um script que sobe tudo |
| `protocolo/` | como medir o tempo entre um agente precisar de você e você perceber |
| `coletor/` | exemplo mínimo de ler o que os agentes já emitem em OpenTelemetry |

## Começando

```bash
git clone https://github.com/filipecalegario/criacomp.git
cd criacomp/human-harness
./tmux/posto.sh
```

`Ctrl-b d` sai sem matar nada. `tmux attach -t posto` volta.

## As três perguntas que o material responde

**Onde cada agente mora?** No tmux, você decide e memoriza. Ferramentas como o `herdr` decidem por você, agrupando por estado do agente (bloqueado, trabalhando, pronto, parado). A diferença não é de recurso, é de quem carrega o mapa.

**Como você percebe que um agente parou e espera?** É o problema que a OpenAI diz resolver com hardware, no Codex Micro, e que ninguém mede em público. O `protocolo/` é uma tentativa de medir.

**O que o agente conta sobre si?** Mais do que se imagina. Claude Code, Codex e Copilot já emitem traços em OpenTelemetry. O `coletor/` mostra como ler.

## Aviso importante

**Perceber mais rápido e ser interrompido menos são objetivos opostos.** Todo dispositivo que faz você notar o agente antes também faz você ser arrancado da sua tarefa mais vezes. Retomar uma sessão de código leva mais de um minuto em 90% das vezes.

Se você montar este posto e a única coisa que melhorar for a velocidade com que você atende os agentes, você piorou o seu dia e melhorou o indicador. O protocolo mede os dois lados de propósito.
