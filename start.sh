#!/bin/bash
cd /workspace/3dWar_launch
source venv/bin/activate
python comfy_manager.py


# === Affichage URL Web Interface ===
POD_HOSTNAME=$(hostname)
echo ""
echo "✅ ComfyUI Manager lancé."
echo "🌐 Accède à l'interface Web ici :"
echo "➡️  https://${POD_HOSTNAME}-8889.proxy.runpod.net/"
