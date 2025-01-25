import requests
import io

# 1. Télécharger le fichier binaire
url = "https://www.passetonhack.fr/api/storage/challenges/19b86d6b326101548c9f0a70e7411423/bmp_recover.txt"
response = requests.get(url)

# Vérifier si la requête est réussie
if response.status_code == 200:
    data = response.content
    print("Fichier téléchargé avec succès.")
else:
    print(f"Erreur de téléchargement: {response.status_code}")
    exit()

# 2. Analyser le fichier pour la clé XOR
# Ici, on cherche la récurrence de 45 72
recurrent_bytes = b'\x45\x72'
recurrent_positions = []

# Chercher les positions de la séquence récurrente
for i in range(len(data) - 1):
    if data[i:i+2] == recurrent_bytes:
        recurrent_positions.append(i)

print(f"Positions des bytes 45 72: {recurrent_positions}")

# 3. Appliquer l'opération XOR
# Si la clé est en relation avec cette séquence, il faut extraire la clé
# Exemple : si la clé se trouve à une position spécifique après la séquence '45 72'
xor_key = data[recurrent_positions[0] + 2]  # On suppose que la clé est juste après la séquence 45 72
print(f"Clé XOR trouvée : {hex(xor_key)}")
print(xor_key)

# Appliquer XOR à chaque byte du fichier
decrypted_data = bytearray([byte ^ xor_key for byte in data])

print(decrypted_data)

# 4. Sauvegarder l'image BMP sans décompression
bmp_filename = "recovered_image.bmp"
with open(bmp_filename, "wb") as f:
    f.write(decrypted_data)

print(f"L'image a été sauvegardée sous le nom {bmp_filename}")
