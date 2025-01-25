import base64
import urllib.parse
import re
from itertools import zip_longest

# Fichiers source
files = ["arg1.txt", "arg2.txt", "arg3.txt"]
output_image = "reconstructed_image.png"

def clean_data(data):
    """Nettoyer les données pour les rendre compatibles avec Base64."""
    decoded_data = urllib.parse.unquote(data)  # Décoder les caractères URL (%2B → +)
    cleaned_data = re.sub(r"[^A-Za-z0-9+/=]", "", decoded_data)  # Supprimer les caractères non valides
    return cleaned_data

def fix_padding(data):
    """Corriger le padding des données Base64 pour qu'elles soient multiples de 4."""
    while len(data) % 4 != 0:
        data += "="
    return data

# Lire et combiner les données des fichiers
data_lines = []
with open(files[0], "r") as f1, open(files[1], "r") as f2, open(files[2], "r") as f3: # Ouvrir les fichiers
    for line1, line2, line3 in zip_longest(f1, f2, f3, fillvalue=""):  # Gérer les lignes manquantes
        combined_line = clean_data((line1 or "").strip() + (line2 or "").strip() + (line3 or "").strip())
        data_lines.append(combined_line)

# Concaténer toutes les lignes en une seule chaîne
full_data = "".join(data_lines)

# Corriger le padding des données
full_data = fix_padding(full_data)

# Vérifications des données avant le décodage
print("Taille des données concaténées :", len(full_data))
print("Premiers 200 caractères des données concaténées :", full_data[:200])

# Décoder les données en Base64
try:
    image_data = base64.b64decode(full_data, validate=True)
    print(f"Taille des données décodées : {len(image_data)} octets")
except Exception as e:
    print("Erreur de décodage des données :", e)
    exit()

# Écrire l'image dans un fichier
try:
    with open(output_image, "wb") as img_file:
        img_file.write(image_data)
    print(f"Image reconstruite et enregistrée sous : {output_image}")
except Exception as e:
    print("Erreur lors de l'écriture du fichier :", e)
