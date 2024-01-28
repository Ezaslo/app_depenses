import os
import subprocess
import urllib.request
import json
import shutil

# Nom de la branche GitHub où se trouve main.py
branch_name = 'V2'

# Chemin où le code sera téléchargé
download_path = os.path.expanduser('C:')

# Construisez l'URL de votre fichier main.py dans la branche spécifique
github_main_url = f'https://github.com/Ezaslo/app_depenses.git/{branch_name}/main.py'

# URL de votre dépôt GitHub pour le fichier JSON (si applicable)
github_json_url = f'https://github.com/Ezaslo/app_depenses.git/{branch_name}/donnees.json'

# Téléchargez main.py depuis GitHub
urllib.request.urlretrieve(github_main_url, os.path.join(download_path, 'main.py'))

# Téléchargez le fichier JSON depuis GitHub (si applicable)
if github_json_url:
    urllib.request.urlretrieve(github_json_url, os.path.join(download_path, 'donnees.json'))

# Installez PyInstaller
subprocess.call(['pip', 'install', 'pyinstaller'])

# Exécutez PyInstaller sur main.py pour générer l'exécutable
main_py = os.path.join(download_path, 'main.py')

subprocess.call(['pyinstaller', main_py])

# Copiez l'exécutable sur le bureau de l'utilisateur
output_folder = os.path.join(download_path, 'dist')
executable_path = os.path.join(output_folder, 'main.exe')
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

shutil.copy2(executable_path, desktop_path)

print("Installation terminée et l'exécutable est sur le bureau !")

# Ajoutez cette ligne pour maintenir la console ouverte
input("Appuyez sur Entrée pour quitter...")
