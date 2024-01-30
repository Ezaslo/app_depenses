import os
import subprocess
import urllib.request
from pathlib import Path
import shutil
import win32com.client

# Assurez-vous que pywin32 est installé pour la gestion des raccourcis
subprocess.call(['pip', 'install', 'pywin32'])

# URL de votre fichier main.py dans la branche spécifique
github_main_url = 'https://raw.githubusercontent.com/Ezaslo/app_depenses/V2/main.py'

# Chemin où le code sera téléchargé
download_path = os.path.expanduser('~')

# Répertoire d'installation de l'application
install_path = "C:/programmes/Anselmo Studio"

# Vérifiez si le répertoire d'installation existe, et s'il existe, supprimez-le
if os.path.exists(install_path):
    shutil.rmtree(install_path)

# Téléchargez main.py depuis GitHub
urllib.request.urlretrieve(github_main_url, os.path.join(download_path, 'main.py'))

# Créez le répertoire d'installation s'il n'existe pas
if not os.path.exists(install_path):
    os.makedirs(install_path)

# Installez PyInstaller
subprocess.call(['pip', 'install', 'pyinstaller'])

# Exécutez PyInstaller sur main.py pour générer l'exécutable directement dans le répertoire d'installation
main_py = os.path.join(download_path, 'main.py')
subprocess.call(['pyinstaller', '--onefile', '--distpath', install_path, main_py])

# Vérifiez si le raccourci existe déjà sur le bureau, et s'il existe, supprimez-le
desktop = Path(os.path.join(os.path.expanduser('~'), 'Desktop'))
shortcut_path = desktop / 'Gestion_Budget.lnk'

if os.path.exists(shortcut_path):
    os.remove(shortcut_path)

# Créez un raccourci sur le bureau de l'utilisateur
target_path = os.path.join(install_path, 'main.exe')

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(str(shortcut_path))
shortcut.TargetPath = target_path
shortcut.WorkingDirectory = install_path
shortcut.IconLocation = target_path
shortcut.save()

print("Installation terminée et l'exécutable est sur le bureau !")

# Maintenez la console ouverte jusqu'à ce que l'utilisateur appuie sur Entrée
input("Appuyez sur Entrée pour quitter...")
