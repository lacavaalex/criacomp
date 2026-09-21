#!/usr/bin/env bash
# Sobe o posto de supervisão: quatro painéis, um papel por cor.
#
#   ./posto.sh              usa comandos de exemplo
#   ./posto.sh --real       usa os comandos do arquivo agentes.txt
#
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SESSAO="posto"

tmux has-session -t "$SESSAO" 2>/dev/null && { tmux attach -t "$SESSAO"; exit 0; }

# Cada painel recebe um papel, um título e uma cor de fundo. A cor é o
# endereço: você aprende em dois dias que amarelo quer alguma coisa de
# você e que vermelho merece atenção antes de qualquer outro.
#
#   papel|título|cor de fundo (código 256)
PAINEIS=(
  "producao|PRODUCAO  cuidado|52"
  "decisao|ESPERANDO VOCE|58"
  "exploracao|exploracao|17"
  "leitura|leitura e logs|235"
)

tmux -f "$DIR/tmux.conf" new-session -d -s "$SESSAO" -x 200 -y 50

for i in "${!PAINEIS[@]}"; do
  IFS='|' read -r papel titulo cor <<< "${PAINEIS[$i]}"
  [ "$i" -gt 0 ] && tmux split-window -t "$SESSAO"
  tmux select-layout -t "$SESSAO" tiled >/dev/null
  alvo="$SESSAO.$((i+1))"
  tmux select-pane -t "$alvo" -P "bg=colour$cor"
  tmux select-pane -t "$alvo" -T "$titulo"
  tmux send-keys  -t "$alvo" "clear; echo '[$papel] painel pronto'" C-m
done

tmux select-pane -t "$SESSAO.1"
tmux attach -t "$SESSAO"
