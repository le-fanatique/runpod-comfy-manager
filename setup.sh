#!/bin/bash
cd /workspace/runpod-comfy-manager
python3 -m venv venv
source venv/bin/activate
pip install flask
chmod +x start_comfy.sh stop_comfy.sh start.sh
ln -s /workspace/runpod-comfy-manager/start.sh /workspace/start.sh
