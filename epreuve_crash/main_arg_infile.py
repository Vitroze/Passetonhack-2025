import urllib.parse
import requests
import re

output_file = "args.txt"

# Initialisation des fichiers de sortie
with open(output_file, "w") as f1:
    # Lecture des données d'entrée

    sURL = "https://www.passetonhack.fr/api/storage/challenges/19b86d6b326101548c9f0a70e7411423/intercepted_data.txt"

    response = requests.get(sURL)

    
    for sLine in response.text.split("\n"):
        # Nettoyage des lignes
        sLine = sLine.strip()
        if not sLine:
            continue  # Passer les lignes vides
        
        sLine = urllib.parse.unquote(sLine)
        sLine = sLine.replace('192.112.220.111 - - ', "")
        sLine = sLine.replace(' "GET /payload?', "")
        sLine = re.sub(r"\[\d{2}/[A-Za-z]{3}/\d{4} \d{2}:\d{2}:\d{2}\]", "", sLine).strip()
        sLine = sLine.replace(' HTTP/1.1" 200 -', "")

        f1.write(sLine + "\n")
