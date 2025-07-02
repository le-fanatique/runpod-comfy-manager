#!/bin/bash
systemctl stop nginx 2>/dev/null || true
systemctl disable nginx 2>/dev/null || true
pkill -f nginx || true

echo "https://$RUNPOD_POD_ID-8889.proxy.runpod.net/"
cd /workspace/runpod-comfy-manager
source venv/bin/activate
python comfy_manager.py


# === Affichage URL Web Interface ===
POD_HOSTNAME=$(hostname)
echo ""
