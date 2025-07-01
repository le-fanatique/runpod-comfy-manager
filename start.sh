#!/bin/bash
cd /workspace/runpod-comfy-manager
source venv/bin/activate
python comfy_manager.py


# === Affichage URL Web Interface ===
POD_HOSTNAME=$(hostname)
echo ""
