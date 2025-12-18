#!/bin/bash

POWER_OPTIONS="$HOME/.config/sway/scripts/gtk-power-menu-options.py"

# Verificar se o script está rodando
if pgrep -f "$POWER_OPTIONS" > /dev/null; then
    # Se estiver rodando, fecha o processo
    pkill -f "$POWER_OPTIONS"
else
    # Não está rodando, então executa
    python3 "$POWER_OPTIONS" &
fi
