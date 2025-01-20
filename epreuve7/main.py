import requests 
from bs4 import BeautifulSoup

sURL = 'https://www.passetonhack.fr/10614a982be7b8607b7ab3e9d5cc370d/'


response = requests.get(sURL)
soup = BeautifulSoup(response.text, "html.parser")

# Trouver tous les chemins des images et liens
print("Images trouvées :")
for img in soup.find_all("img", src=True):
    print(img["src"])

print("\nLiens trouvés :")
for link in soup.find_all("a", href=True):
    print(link["href"])
