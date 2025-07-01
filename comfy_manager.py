from flask import Flask, jsonify, request, send_from_directory
import subprocess
import os

app = Flask(__name__, static_folder="static")

LOG_FILE = "/workspace/ComfyUI/user/comfyui_3001.log"
PID_FILE = "/workspace/ComfyUI/comfy.pid"

def is_comfy_running():
    if os.path.exists(PID_FILE):
        try:
            with open(PID_FILE, "r") as f:
                pid = int(f.read().strip())
            os.kill(pid, 0)
            return True
        except:
            return False
    return False

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/status")
def status():
    return jsonify({"running": is_comfy_running()})

@app.route("/logs")
def logs():
    if not is_comfy_running():
        return jsonify({"logs": ""})
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return jsonify({"logs": "".join(f.readlines()[-20:])})
    return jsonify({"logs": "No logs available."})

@app.route("/start", methods=["POST"])
def start():
    subprocess.Popen(["/bin/bash", "/workspace/3dWar_launch/start_comfy.sh"])
    return '', 204

@app.route("/stop", methods=["POST"])
def stop():
    subprocess.call(["/bin/bash", "/workspace/3dWar_launch/stop_comfy.sh"])
    return '', 204


@app.route("/download/huggingface", methods=["POST"])
def download_hf():
    data = request.get_json()
    url = data.get("url")
    model_type = data.get("model_type", "Model")
    hf_token = os.environ.get("HF_TOKEN")

    progress_file = "/workspace/3dWar_launch/hf_download_status.txt"
    with open(progress_file, "w") as f:
        f.write("Téléchargement en cours...\n")

    if not hf_token:
        with open(progress_file, "a") as f:
            f.write("Token HuggingFace non défini.\n")
        return jsonify({"detail": "HF_TOKEN non défini."}), 500

    dest_dir = "/workspace/ComfyUI/models" if model_type == "Model" else f"/workspace/ComfyUI/models/{model_type}"
    os.makedirs(dest_dir, exist_ok=True)

    cmd = ["wget", "--header", f"Authorization: Bearer {hf_token}", "-P", dest_dir, url]

    try:
        with open(progress_file, "a") as f:
            f.write(f"Téléchargement depuis {url} vers {dest_dir}\n")

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        with open(progress_file, "a") as f:
            for line in process.stdout:
                f.write(line)
        process.wait()

        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, cmd)

        with open(progress_file, "a") as f:
            f.write("Téléchargement terminé avec succès.\n")

        return '', 204
    except subprocess.CalledProcessError as e:
        with open(progress_file, "a") as f:
            f.write("Erreur pendant le téléchargement.\n")
        return jsonify({"detail": str(e)}), 500

@app.route("/download/progress")
def download_progress():
    try:
        with open("/workspace/3dWar_launch/hf_download_status.txt", "r") as f:
            return jsonify({"progress": f.read()})
    except:
        return jsonify({"progress": "Aucune activité de téléchargement."})

def download_hf():
    data = request.get_json()
    url = data.get("url")
    model_type = data.get("model_type", "Model")
    hf_token = os.environ.get("HF_TOKEN")

    if not hf_token:
        return jsonify({"detail": "HF_TOKEN non défini."}), 500

    dest_dir = "/workspace/ComfyUI/models" if model_type == "Model" else f"/workspace/ComfyUI/models/{model_type}"
    os.makedirs(dest_dir, exist_ok=True)

    cmd = ["wget", "--header", f"Authorization: Bearer {hf_token}", "-P", dest_dir, url]

    try:
        subprocess.run(cmd, check=True)
        return '', 204
    except subprocess.CalledProcessError as e:
        return jsonify({"detail": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8889)


@app.route("/restart", methods=["POST"])
def restart():
    subprocess.call(["/bin/bash", "/workspace/3dWar_launch/stop_comfy.sh"])
    subprocess.Popen(["/bin/bash", "/workspace/3dWar_launch/start_comfy.sh"])
    return '', 204

@app.route("/models")
def list_models():
    base_dir = "/workspace/ComfyUI/models"
    model_data = {}
    for root, dirs, files in os.walk(base_dir):
        rel_root = os.path.relpath(root, base_dir)
        if rel_root == ".":
            rel_root = "root"
        model_data[rel_root] = sorted([f for f in files if not f.startswith(".")])
    return jsonify(model_data)
