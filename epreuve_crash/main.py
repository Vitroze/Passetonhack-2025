import base58
import requests
import base64
from urllib.parse import unquote
from itertools import zip_longest
import re

# URL des journaux
sURL = 'https://www.passetonhack.fr/api/storage/challenges/19b86d6b326101548c9f0a70e7411423/intercepted_data.txt'
response = requests.get(sURL)

def cleanData(sLine):
    sLine =  sLine.strip()
    sLine = unquote(sLine)
    sLine = sLine.replace('192.112.220.111 - - ', "")
    sLine = sLine.replace(' "GET /payload?', "")
    sLine = re.sub(r"\[\d{2}/[A-Za-z]{3}/\d{4} \d{2}:\d{2}:\d{2}\]", "", sLine).strip()
    sLine = sLine.replace(' HTTP/1.1" 200 -', "")

    # Delete arg{1,2,3}= from the string

    return sLine

tData = {}
for sLine in response.text.split("\n"):
    sLine = cleanData(sLine)

    # Extract the arguments
    for sArg in sLine.split("&"):
        if sArg.startswith("arg1="):
            tData["arg1"] = sArg[5:]
        elif sArg.startswith("arg2="):
            tData["arg2"] = sArg[5:]
        elif sArg.startswith("arg3="):
            tData["arg3"] = sArg[5:]

# Fichiers locaux (si besoin d'analyser plusieurs fichiers en parallèle)
files = ["file1.txt", "file2.txt", "file3.txt"]

# Liste pour stocker les données combinées
data_lines = []

try:
    with open(files[0], "r") as f1, open(files[1], "r") as f2, open(files[2], "r") as f3:
        for line1, line2, line3 in zip_longest(f1, f2, f3, fillvalue=""):
            combined_line = cleanData((line1 or "").strip() + (line2 or "").strip() + (line3 or "").strip())
            data_lines.append(combined_line)
except FileNotFoundError:
    # Si les fichiers locaux ne sont pas utilisés, charger les données depuis l'URL
    print("Traitement à partir des journaux téléchargés...")
    data_lines = [cleanData(line) for line in response.text.split("\n")]
# Concatenate the arguments
sFullData = tData["arg1"] + tData["arg2"] + tData["arg3"]

# Corriger le padding des données
while len(sFullData) % 4 != 0:
    sFullData += "="

# Vérifications des données avant le décodage
print("Taille des données concaténées :", len(sFullData))
print("Premiers 200 caractères des données concaténées :", sFullData[:200])

# Décoder les données en Base64
try:
    image_data = base64.b64decode(sFullData, validate=True)
    print(f"Taille des données décodées : {len(image_data)} octets")
except Exception as e:
    print("Erreur de décodage des données :", e)
    exit()

# Écrire l'image dans un fichier
with open("image.png", "wb") as img_file:
    img_file.write(image_data)
print(f"Image reconstruite et enregistrée sous : image.png")