# ComfyUI Manager sur RunPod

Ce dossier contient une interface web simple pour contrôler ComfyUI depuis RunPod, avec en bonus :

- ✅ Démarrage / arrêt de ComfyUI
- ✅ Affichage des logs (20 dernières lignes)
- ✅ Lien direct vers l’interface ComfyUI
- ✅ Téléchargement de modèles depuis HuggingFace

---

## 🚀 Installation

```bash
git clone https://github.com/<TON-USER>/runpod-comfy-manager.git
cd runpod-comfy-manager
bash setup.sh
```

---

## 🔧 Utilisation

```bash
bash start.sh
```

Puis ouvre ton navigateur à l’adresse :  
**http://localhost:8889** *(ou selon ton pod RunPod)*

---

## 🌐 Variables d’environnement

Avant d’utiliser le téléchargement HuggingFace, définis ton token :

```bash
export HF_TOKEN=hf_XXXXXXXXXXXXXXXXXXXXX
```

---

## 📂 Dossiers utilisés

- `models/<type>` : les fichiers HuggingFace sont téléchargés ici
- `user/comfyui_3001.log` : fichier log de ComfyUI
- `comfy.pid` : fichier PID pour contrôle du process
