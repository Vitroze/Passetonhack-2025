# Fonction pour lire le fichier texte brut
def read_text_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    return data

# Fonction pour appliquer l'opération XOR
def xor_decrypt(data, key):
    decrypted_data = bytearray(data)
    key_len = len(key)
    for i in range(len(data)):
        decrypted_data[i] ^= key[i % key_len]
    return bytes(decrypted_data)

# Fonction pour corriger l'en-tête BMP
def fix_bmp_header(data):
    # Remplacer les 2 premiers bytes par 'BM' (42 4D en hex)
    return b'BM' + data[2:]

# Chemin vers le fichier texte téléchargé
file_path = "bmp_recover.txt"

# Lire les données du fichier texte
file_data = read_text_file(file_path)

# Clé de chiffrement (recherche du motif 45 72 dans les données)
key = b'\x45\x72'

# Déchiffrer les données avec XOR
decrypted_data = xor_decrypt(file_data, key)

# Corriger l'en-tête BMP
bmp_data = fix_bmp_header(decrypted_data)

# Sauvegarder le fichier BMP
with open("recovered_image.bmp", "wb") as bmp_file:
    bmp_file.write(bmp_data)

print("Image BMP récupérée et corrigée sous le nom 'recovered_image.bmp'")
