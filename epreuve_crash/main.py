import base58
import requests
import base64
import urllib.parse
import binascii
import re

# URL des journaux
sURL = 'https://www.passetonhack.fr/api/storage/challenges/19b86d6b326101548c9f0a70e7411423/intercepted_data.txt'
response = requests.get(sURL)

def decode_ASCII(sVar):
    """Décodage ASCII"""
    try:
        return sVar.encode('ascii').decode('ascii')
    except UnicodeDecodeError:
        return None

def decode_Base58(sVar):
    """Décodage Base58"""
    try:
        return base58.b58decode(sVar).decode('ascii')
    except Exception:
        return None

def decode_Base64(sVar):
    """Décodage Base64"""
    try:
        return base64.b64decode(sVar).decode('ascii')
    except Exception:
        return None

def decode_Hex(sVar):
    """Décodage Hexadecimal"""
    try:
        return binascii.unhexlify(sVar).decode('ascii')
    except Exception:
        return None

def decode_URL(sVar):
    """Décodage URL (pour les chaînes avec des % comme %2F, %2B...)"""
    try:
        return urllib.parse.unquote(sVar)
    except Exception:
        return None

def try_decode(sVar):
    """Essaye plusieurs méthodes de décodage"""
    decoded = decode_URL(sVar)
    if decoded:
        return decoded
    
    decoded = decode_ASCII(sVar)
    if decoded:
        return decoded
    
    decoded = decode_Base58(sVar)
    if decoded:
        return decoded
    
    decoded = decode_Base64(sVar)
    if decoded:
        return decoded
    
    decoded = decode_Hex(sVar)
    if decoded:
        return decoded
    
    return None

tExtraction = []
for sLine in response.text.split("\n"):
    tMatches = re.findall(r"arg\d=([^&\s]+)", sLine)

    if tMatches: 
        if len(tMatches) > 1:
            sMatch = ""
            for sLineMatch in tMatches:
                sMatch += try_decode(sLineMatch)

            if sMatch:
                tExtraction.append(sMatch)
        else:
            decoded_data = try_decode(tMatches[0])

            if decoded_data:
                tExtraction.append(decoded_data)

if len(tExtraction) > 1:
    print("Les données extraites sont :")

    with open("output.txt", "w") as f:
        for sData in tExtraction:
            f.write(sData + "\n")
