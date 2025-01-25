import base64
import requests
import urllib.parse
import re
from itertools import zip_longest

# URL des journaux
sURL = 'https://www.passetonhack.fr/api/storage/challenges/19b86d6b326101548c9f0a70e7411423/intercepted_data.txt'
response = requests.get(sURL)

if response.status_code != 200:
    print("Erreur lors de la récupération des données depuis l'URL.")
    exit()

# Nettoyage des données
def clean_data(data):
    """Nettoyer les données pour les rendre compatibles avec Base64."""

    decoded_data = urllib.parse.unquote(data)  # Décoder les caractères URL

    """
        cleaned_data ; Caractères valides : A-Z, a-z, 0-9, +, /, =
    
    """

    cleaned_data = re.sub(r"[^A-Za-z0-9+/=]", "", decoded_data)  # Supprimer les caractères non valides

    return cleaned_data

def fix_padding(data):
    """Corriger le padding des données Base64 pour qu'elles soient multiples de 4."""
    while len(data) % 4 != 0:
        data += "="
    return data

tDataArg1, tDataArg2, tDataArg3 = [], [], []

def beautifulLine(sLine):
    sLine = sLine.replace('192.112.220.111 - - ', "")
    sLine = sLine.replace(' "GET /payload?', "")
    sLine = re.sub(r"\[\d{2}/[A-Za-z]{3}/\d{4} \d{2}:\d{2}:\d{2}\]", "", sLine).strip()
    sLine = sLine.replace(' HTTP/1.1" 200 -', "")

    return sLine

# Create file Args
with open("args.txt", "w") as f1:
    for line in response.text.split("\n"):
        line = line.strip()
        line = beautifulLine(line)
        f1.write(line + "\n")

with open("args.txt", "r") as f1:
    for line in f1:
        line = line.strip()
        if not line:
            continue  # Passer les lignes vides

        sArg1, sArg2, sArg3 = "", "", ""
        for part in line.split("&"):
            if part.startswith("arg1="):
                sArg1 = part[5:]  # Supprimer 'arg1='
            elif part.startswith("arg2="):
                sArg2 = part[5:]  # Supprimer 'arg2='
            elif part.startswith("arg3="):
                sArg3 = part[5:]  # Supprimer 'arg3='

        tDataArg1.append(sArg1)
        tDataArg2.append(sArg2)
        tDataArg3.append(sArg3)

# Combiner les données des arguments
tDataFile = []
for sArg1, sArg2, sArg3 in zip_longest(tDataArg1, tDataArg2, tDataArg3, fillvalue=""):

    sFullDataLine = clean_data((sArg1 or "").strip() + (sArg2 or "").strip() + (sArg3 or "").strip())
    tDataFile.append(sFullDataLine)

print("Taille des données concaténées :", len(tDataFile))
print("Premiers 200 caractères des données concaténées :", "".join(tDataFile)[:200])
sFullData = "".join(tDataFile)
sFullData = fix_padding(sFullData)

# Décoder les données en Base64
try:
    fImageData = base64.b64decode(sFullData, validate=True) # validate=True : Vérifie si les données sont valides
    print(f"Taille des données décodées : {len(fImageData)} octets")
except Exception as e:
    print("Erreur de décodage des données :", e)
    exit()


output_image = "image.png"
try:
    with open(output_image, "wb") as img_file:
        img_file.write(fImageData)
    print(f"Image reconstruite et enregistrée sous : {output_image}")
except Exception as e:
    print("Erreur lors de l'écriture du fichier :", e)
