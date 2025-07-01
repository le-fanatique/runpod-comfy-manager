#!/bin/bash
cd /workspace/ComfyUI
source venv/bin/activate
nohup python3 main.py --port 3001 --listen 0.0.0.0 > /workspace/ComfyUI/user/comfyui_3001.log 2>&1 &
echo $! > /workspace/ComfyUI/comfy.pid
