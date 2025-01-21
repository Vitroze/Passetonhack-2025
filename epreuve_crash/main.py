import base58
import requests
import base64
import urllib.parse
import binascii
import re

# URL des journaux
sURL = 'https://www.passetonhack.fr/api/storage/challenges/19b86d6b326101548c9f0a70e7411423/intercepted_data.txt'
response = requests.get(sURL)


# Fonction pour tester si la chaîne est en base64
def decode_data(data):
    try:
        # Tentative de décodage Base64
        decoded_data = base64.b64decode(data).decode('utf-8')
        return decoded_data
    except (base64.binascii.Error, UnicodeDecodeError):
        return None

# Traitement des lignes dans les journaux

tExtraction = []
for sLine in response.text.split("\n"):
    tMatches = re.findall(r"arg\d=([^&\s]+)", sLine)

    if len(tMatches) > 1:
        sMatch = ""
        for sLineMatch in tMatches:
            sDecodedURL = urllib.parse.unquote(sLineMatch)

           # decoded_data = decode_data(sDecodedURL)

            sMatch += sDecodedURL

        if sMatch:
            tExtraction.append(sMatch)
    else:
        sDecodedURL = urllib.parse.unquote(tMatches[0])
        decoded_data = decode_data(sDecodedURL)

        if decoded_data:
            tExtraction.append(decoded_data)
# 阗 䬙 㳳
# 

if len(tExtraction) > 1:
    print("Les données extraites sont :")
    for sData in tExtraction:
        print(sData)