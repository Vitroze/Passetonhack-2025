from Crypto.PublicKey import RSA

# Générer une clé privée RSA de 1024 bits
key = RSA.generate(4096)

# Exporter la clé privée en PEM (format lisible)
private_key = key.export_key()

# Enregistrer la clé privée dans un fichier
with open("private_key.pem", "wb") as f:
    f.write(private_key)

print("Clé privée générée et enregistrée dans 'private_key.pem'")
