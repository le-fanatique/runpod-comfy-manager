#!/bin/bash
echo "https://$RUNPOD_POD_ID-8889.proxy.runpod.net/"
cd /workspace/runpod-comfy-manager
source venv/bin/activate
python comfy_manager.py


# === Affichage URL Web Interface ===
POD_HOSTNAME=$(hostname)
echo ""
