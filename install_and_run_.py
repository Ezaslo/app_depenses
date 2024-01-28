import os
import subprocess
import urllib.request
import json
import shutil
import ctypes
from pathlib import Path

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

subprocess.call(['pyinstaller', main_py])

# Copiez l'exécutable dans le répertoire d'installation
output_folder = os.path.join(download_path, 'dist')
executable_path = os.path.join(output_folder, 'main.exe')
shutil.copy2(executable_path, os.path.join(install_path, 'main.exe'))

# Créez un raccourci sur le bureau de l'utilisateur
user_desktop = Path(os.path.expanduser('~'), 'Desktop')
shortcut_name = "appDepenses.lnk"
shortcut_path = os.path.join(user_desktop, shortcut_name)
target_path = os.path.join(install_path, 'main.exe')

# Utilisez ctypes pour créer le raccourci
shell = ctypes.windll.shell32
shortcut_location = str(Path(install_path).resolve())
shell.ShellExecuteW(None, "create", "explorer.exe", shortcut_location, "", 1)

print("Installation terminée et l'exécutable est sur le bureau !")

# Ajoutez cette ligne pour maintenir la console ouverte
input("Appuyez sur Entrée pour quitter...")
