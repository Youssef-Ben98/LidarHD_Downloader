#  Téléchargement automatique des dalles LiDAR HD de l’IGN

Ce projet propose un script **Python** permettant de télécharger automatiquement les dalles **LiDAR HD** fournies par l’IGN, à partir d’une liste de liens `.laz`/`.las`.

---

##  Fonctionnalités
- Télécharge en masse les dalles LiDAR HD à partir d’un fichier texte contenant les URLs.
- Stocke les fichiers localement dans un dossier défini.
- Gestion simple des téléchargements via la librairie `requests`.
  
##  Organisation
LidarHD_Download/
│── LidarHD_Down.py # Script principal
│── urls.txt # Liste des liens vers les dalles LiDAR

## Installer les dépendances

pip install requests

## Utilisation
python LidarHD_Down.py

## Sources
https://geoservices.ign.fr/lidarhd#telechargementclassifiees

