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
def is_base64(s):
    try:
        base64.b64decode(s, validate=True)
        return True
    except Exception:
        return False

# Fonction pour tester si la chaîne est encodée en hexadécimal
def is_hex(s):
    try:
        binascii.unhexlify(s)
        return True
    except Exception:
        return False

# Fonction pour tester si la chaîne est URL encodée
def is_url_encoded(s):
    return s != urllib.parse.unquote(urllib.parse.quote(s))

# Fonction pour tester si la chaîne est encodée en base58
def is_base58(s):
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    return all(c in alphabet for c in s)

# Fonction de décodage
def decode_data(s):
    # Essayer les différents types de décodage
    if is_base64(s):
        try:
            return base64.b64decode(s).decode('utf-8')
        except:
            return None
    elif is_hex(s):
        try:
            return binascii.unhexlify(s).decode('utf-8')
        except:
            return None
    elif is_url_encoded(s):
        return urllib.parse.unquote(s)
    elif is_base58(s):
        return base58.b58decode(s)
    else:
        return None

# Fonction pour tester si la chaîne est en base58
def is_base58(s):
    try:
        base58.b58decode(s)
        return True
    except Exception:
        return False

# Fonction de décodage
def decode_data(s):
    # Essayer les différents types de décodage
    if is_base64(s):
        try:
            return base64.b64decode(s).decode('utf-8')
        except:
            return None
    elif is_hex(s):
        try:
            return binascii.unhexlify(s).decode('utf-8')
        except:
            return None
    elif is_url_encoded(s):
        return urllib.parse.unquote(s)
    elif is_base58(s):
        try:
            return base58.b58decode(s).decode('utf-8')
        except:
            return None
    else:
        return None

# Traitement des lignes dans les journaux
for sLine in response.text.split("\n"):
    sLine = sLine[73:len(sLine) - 15]
    
    tArgs = sLine.split("&")

    if len(tArgs) > 1:
        for sArg in tArgs:
            sArg = re.sub(r'arg\d+=\S+&?', '', sArg)
            decoded = decode_data(sArg)
            if decoded:
                print("Données décodées :", decoded)
                # Ici, analysez les données pour trouver la ville la plus proche ou des coordonnées
    else:
        sLine = re.sub(r'arg\d+=\S+&?', '', sLine)
        decoded = decode_data(sLine)
        if decoded:
            print("Données décodées :", decoded)
            # Ici, analysez les données pour trouver la ville la plus proche ou des coordonnées
