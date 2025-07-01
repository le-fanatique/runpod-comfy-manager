#!/bin/bash
cd /workspace/3dWar_launch
python3 -m venv venv
source venv/bin/activate
pip install flask
chmod +x start_comfy.sh stop_comfy.sh start.sh
