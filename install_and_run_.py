import os
import subprocess
import urllib.request
from pathlib import Path
import shutil

# Installation de pywin32 pour la gestion des raccourcis
subprocess.call(['pip', 'install', 'pywin32'])

import win32com.client

# URL de votre fichier main.py dans la branche spécifique
github_main_url = 'https://raw.githubusercontent.com/Ezaslo/app_depenses/V2/main.py'

# Chemin où le code sera téléchargé
download_path = os.path.expanduser('~')

# Téléchargez main.py depuis GitHub
urllib.request.urlretrieve(github_main_url, os.path.join(download_path, 'main.py'))

# Répertoire d'installation de l'application
install_path = "C:/programmes/appDepenses"

# Créez le répertoire d'installation s'il n'existe pas
if not os.path.exists(install_path):
    os.makedirs(install_path)

# Installez PyInstaller
subprocess.call(['pip', 'install', 'pyinstaller'])

# Exécutez PyInstaller sur main.py pour générer l'exécutable
main_py = os.path.join(download_path, 'main.py')
subprocess.call(['pyinstaller', '--onefile', main_py])

# Copiez l'exécutable dans le répertoire d'installation
output_folder = os.path.join(download_path, 'dist')
executable_path = os.path.join(output_folder, 'main.exe')
shutil.copy2(executable_path, os.path.join(install_path, 'main.exe'))

# Créez un raccourci sur le bureau de l'utilisateur
desktop = Path(os.path.join(os.path.expanduser('~'), 'Desktop'))
shortcut_path = desktop / 'appDepenses.lnk'
target_path = os.path.join(install_path, 'main.exe')

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(str(shortcut_path))
shortcut.TargetPath = target_path
shortcut.WorkingDirectory = os.path.dirname(target_path)
shortcut.IconLocation = target_path
shortcut.save()

print("Installation terminée et l'exécutable est sur le bureau !")

# Vérification et mise à jour de l'application (Structure de base)
# Note : Ce code est un pseudo-code pour illustrer l'approche.
# Vous devez implémenter la logique de vérification des mises à jour en fonction de votre infrastructure.

# def check_for_updates():
#     # Utilisez l'API GitHub pour vérifier la dernière version disponible
#     # Comparez avec la version actuelle de l'application
#     # Si une nouvelle version est disponible, téléchargez et installez-la

# check_for_updates()

# Maintenez la console ouverte jusqu'à ce que l'utilisateur appuie sur Entrée
input("Appuyez sur Entrée pour quitter...")
