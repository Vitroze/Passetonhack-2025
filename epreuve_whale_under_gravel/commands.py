from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii
import pyperclip

# Clé publique du serveur
PUBKEY = '''\
-----BEGIN PUBLIC KEY-----
MIICIDANBgkqhkiG9w0BAQEFAAOCAg0AMIICCAKCAgEAr1i24dJXtg5bHUOY4Kkv
oSDkjSVJfjsWwQcfGuNpXBg3rUpcIxQhJTfdmXSaXCNhfxUWO2ZJmIUBAh0ACgf+
3hz1HPLt9/Ey+vRGOtMOB8oCTIHfQifDRAaqUga6mGDRsT8Q3pN34yQ+9cHjZsyH
8xoYjBaUj+abOoyfkVetrLzKSAY0xi6aXbP6UHdkuCSt0mW0O54pT/hONBCH1Xf0
qC9naFmPnZgIGdHGuUOpXkgL41eZPSCVt9AT1WSIbS9VyzIscF0J2kvGvXoHUzBr
8PoB80MR/32JCoYYfMyrS3QrjT3/RUr6R9sKZVbjKC+b5DmUJcWn2VKIWIiITyfJ
eq8eSiztUFv7M06iEO6n2glTMpetxHT7dEBIvxh4D0uppUO/23MTHKAm+f56wyLq
Glc/qhUw+xRB1RXbgepm2ojjCu65LP9cg080ixVfSJD+G3kZasWVUrbIxLoeM/Gp
DVJXczgfeIvars7Km4OxKet+qFyBgCAnTLZDeSNy/20My9WLtpfTtvySSYEFbitf
uRQOy2JuPv58A56oesK8c0+3adGy5QFicEmNMbWLfYveRc9wJ3UrWi1FOkfknIf/
FINKg3tMKNNuYfgqPH3cDXW2Q7HGrtw/mxksjTbJfxCRv5bNEFEk3px9RubRnfRd
5hdxo2NKbskEXw5VPDiZyA0CAQM=
-----END PUBLIC KEY-----
'''

# Charger la clé publique
key = RSA.import_key(PUBKEY)

# Message à signer (exemple : challenge du serveur)
message = input("Entrez le challenge reçu du serveur : ")

# Calculer le hachage du message
msg_hash = SHA256.new(message.encode())

fake_signature = (int.from_bytes(msg_hash.digest(), byteorder='big') ** key.e % key.n).to_bytes(key.size_in_bytes(), byteorder='big')

# Convertir la fausse signature en format hexadécimal
fake_signature_hex = binascii.hexlify(fake_signature).decode()

print(f"Fausse signature générée en hexadécimal : {fake_signature_hex}")

# Copier la fausse signature dans le presse-papiers
pyperclip.copy(fake_signature_hex)