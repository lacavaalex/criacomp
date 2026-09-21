# Coletor: ler o que os agentes já contam sobre si

O ponto mais surpreendente da pesquisa sobre supervisão de agentes é este:

> **Claude Code, Codex e GitHub Copilot já emitem traços em OpenTelemetry.**

Quem quiser construir um painel de supervisão não precisa instrumentar nada, nem pedir nada a nenhum fabricante. O dado já está saindo, num padrão aberto. O gargalo não é instrumentação, é interface.

## O que eles emitem

As convenções semânticas GenAI do OpenTelemetry definem a execução de um agente como uma árvore:

```
invoke_agent
├── chat            cada chamada ao modelo
├── execute_tool    cada ferramenta chamada
└── chat
```

Cada nó traz início, duração, e atributos como modelo, contagem de tokens e nome da ferramenta.

## Rodar

```bash
python3 coletor.py
```

Sobe um receptor OTLP mínimo em `http://localhost:4318`. Depois, aponte o agente para ele:

```bash
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
export OTEL_TRACES_EXPORTER=otlp
# e o interruptor de telemetria do seu agente, que varia por ferramenta
```

O coletor imprime cada span recebido. É de propósito burro: o exercício é ver o dado cru chegando, não construir observabilidade de verdade.

## O exercício que vale a pena

Depois de ver os spans chegando, a pergunta é de projeto, não de código:

> **Quais desses eventos merecem interromper a pessoa?**

Hoje ninguém responde isso. O padrão resolveu o transporte e deixou a política em aberto: a decisão de interromper está espalhada entre o agente, o multiplexador de terminal e o sistema operacional, sem dono.

Quem construir uma regra defensável para isso tem um Projeto Ferramenta pronto.

## Aviso

Traço completo que ninguém consegue ler é o mesmo problema de antes, com mais dados dentro. Instrumentar é condição necessária e não suficiente.
