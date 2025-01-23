import socket
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes

# Adresse et port du serveur cible
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

# Clé publique extraite du serveur
PUBKEY = """\
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
"""

# Charger la clé publique
key = RSA.import_key(PUBKEY)


def forge_signature(challenge):
    """
    Forge une signature ASN.1 pour contourner la validation.
    """
    # Construire une structure ASN.1 invalide mais acceptable
    hash_len = 32  # Taille de SHA256
    fake_asn1 = b'\x30' + bytes([0x2e + hash_len]) + b'\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00' + \
                b'\x04' + bytes([hash_len]) + b'\x00' * hash_len

    # Représenter la structure comme un entier pour simuler une signature
    fake_sig_int = int.from_bytes(fake_asn1, 'big')
    forged_sig_int = pow(fake_sig_int, key.e, key.n)

    # Retourner la signature sous forme d'octets
    return long_to_bytes(forged_sig_int, key.size_in_bytes())

challenge = input("Entrez le challenge : ")
forged_signature = forge_signature(challenge)
hex_signature = forged_signature.hex()
print(f"Signature forgée : {hex_signature}")

# Copier la signature forgée dans le presse-papiers
import pyperclip
pyperclip.copy(hex_signature)
print("Signature copiée dans le presse-papiers.")