import os
import sys
import shutil
import argparse
import re
from datetime import datetime
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser(
        description="Copie organisée des fichiers DJI depuis le dossier DCIM Android vers le dossier actuel (destination)."
    )
    parser.add_argument(
        "source",
        nargs="?",
        help="Chemin du dossier d'origine (DCIM/Android où se trouve le drone)."
    )
    return parser.parse_args()

def confirm_action(src, dst):
    print("\nRésumé de l'action :")
    print(f"  - Dossier d'origine : {src}")
    print(f"  - Dossier de destination : {dst}")
    print("  - Tous les fichiers vidéo et photo nommés DJI_YYYYMMDDhhmmss_... seront copiés (hors .SRT, .LRF), organisés par date du nom.")
    choice = input("Confirmez-vous cette opération ? [o/N] ").strip().lower()
    return choice == 'o'

def find_files(src):
    pattern = re.compile(r"^DJI_(\d{14})_.*\.[A-Za-z0-9]+$")
    for root, _, files in os.walk(src):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in ('.srt', '.lrf'):
                continue
            if pattern.match(f):
                yield os.path.join(root, f), f

if __name__ == '__main__':
    args = parse_args()
    dest = os.path.dirname(os.path.abspath(__file__))

    default_src = "/Volumes/android/DCIM/DJI_001"
    src = args.source or input(f"Dossier d'origine (DCIM Android) [par défaut: {default_src}]: ") or default_src

    if not os.path.isdir(src):
        print(f"Erreur : le dossier d'origine '{{src}}' n'existe pas.")
        sys.exit(1)

    if not confirm_action(src, dest):
        print("Opération annulée.")
        sys.exit(0)

    files = list(find_files(src))
    if not files:
        print("Aucun fichier compatible trouvé dans '{{src}}'.")
        sys.exit(0)

    print(f"\nDémarrage de la copie de {len(files)} fichiers...")
    for fullpath, filename in tqdm(files, desc="Copie en cours", unit="fichier"):
        date_str = re.match(r"^DJI_(\d{14})", filename).group(1)
        try:
            dt = datetime.strptime(date_str, "%Y%m%d%H%M%S")
            subfolder = dt.strftime("%Y-%m-%d")
        except Exception:
            subfolder = "inconnu"
        target_dir = os.path.join(dest, subfolder)
        os.makedirs(target_dir, exist_ok=True)
        shutil.copy2(fullpath, os.path.join(target_dir, filename))

    print("\nCopie terminée !")
