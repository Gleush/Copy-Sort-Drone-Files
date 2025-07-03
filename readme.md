# Copy & Sort Done Files

Ce script Python copie automatiquement TOUS vos fichiers vidéo et photo depuis le dossier DCIM d’Android (carte SD de votre drone) vers le dossier où se trouve le script, en les organisant dans des dossier par date.  
Utile pour vider rapidement un drone tout en gardant tout les fichiers média en une simple commande.

Ce script à été conçu pour le DJI Mini Pro 4. Mais peux convenir pour d'autres modèles.  
Pour d'autres marques je conseille de modifier le code. Feel free to contribute :)

## Fonctionnalités

- Ignore les fichiers `.SRT` et `.LRF`  
- Ne conserve que les fichiers nommés `DJI_YYYYMMDDhhmmss_*.*`  
- Crée un sous-dossier `YYYY-MM-DD` pour chaque date extraite du nom de fichier  
- Affiche un résumé interactif (source & destination) avant la copie  
- Barre de progression en console via [`tqdm`](https://github.com/tqdm/tqdm)

## Prérequis

- Python 3.6+  
- [tqdm](https://pypi.org/project/tqdm/)  
```bash
  pip install tqdm
````

## Installation

1. Clonez ce dépôt ou téléchargez simplement le fichier [`drone_copy.py`](./drone_copy.py).
2. Placez-le dans le dossier que vous souhaitez utiliser comme **destination** pour vos fichiers DJI.

## Usage

Ouvrez un terminal dans le dossier contenant `dji_copy.py`, puis lancez :

```bash
# avec dossier source explicite
python dji_copy.py /Volumes/Android/DCIM

# ou sans argument
python dji_copy.py
```

Si vous avez un message avec tqdm c'est que vous avez oublié les prérequis.

* **Dossier d’origine** :

  * Si vous passez un argument, il est utilisé comme chemin vers `DCIM/Android`.
  * Sinon, le script propose `/Volumes/Android/DCIM` par défaut.
* **Dossier de destination** :

  * C’est toujours le dossier où se trouve le script.

Le script vous affichera un résumé :

```
Résumé de l'action :
  - Dossier d'origine : /Volumes/Android/DCIM
  - Dossier de destination : /Users/votre_user/Script
  - Tous les fichiers vidéo et photo nommés DJI_YYYYMMDDhhmmss_... seront copiés (hors .SRT, .LRF), organisés par date du nom.
Confirmez-vous cette opération ? [o/n]
```

Répondez `o` pour lancer la copie.

---

**Licence MIT**  
© 2025 Samuel Carpentier.
