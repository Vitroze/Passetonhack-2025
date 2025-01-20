import requests 
from PIL import Image
from io import BytesIO

sURL = 'https://www.passetonhack.fr/api/storage/challenges/19b86d6b326101548c9f0a70e7411423/6052ea0371a46b5c08679a516cf05346-step-1.jpg'

response = requests.get(sURL)
print(response.status_code)
img = Image.open(BytesIO(response.content))

exif_data = img._getexif()

if exif_data:
    for key, value in exif_data.items():
        print(f"Clé : {key}, Valeur : {value}")

else:
    print("Pas de données EXIF")