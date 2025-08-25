import os
import requests

# Chosir un  dossier pour stocker les fichiers téléchargés
download_dir = "LIdarHD_PARIS"
os.makedirs(download_dir, exist_ok=True)

#  Fichier contenant la liste des liens (un par ligne), vous telecharger ce fichier dans le site de geoserivce de l'IGN
url_file = "liste_dalle.txt"

#  Lire tous les liens depuis le fichier
with open(url_file, "r") as f:
    urls = [line.strip() for line in f if line.strip()]

#  Téléchargement
for url in urls:
    filename = os.path.basename(url)
    filepath = os.path.join(download_dir, filename)

    if not os.path.exists(filepath):
        print(f"Téléchargement de {filename}...")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(filepath, "wb") as f_out:
                for chunk in response.iter_content(1024):
                    f_out.write(chunk)
            print(f"{filename} téléchargé dans {download_dir}")
        else:
            print(f"Erreur {response.status_code} pour {url}")
    else:
        print(f"⚡ {filename} déjà présent, on passe.")
