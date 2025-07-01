#!/bin/bash
if [ -f /workspace/ComfyUI/comfy.pid ]; then
    kill $(cat /workspace/ComfyUI/comfy.pid) && rm /workspace/ComfyUI/comfy.pid
    echo "ComfyUI arrêté."
else
    echo "Aucun PID trouvé pour ComfyUI."
fi
