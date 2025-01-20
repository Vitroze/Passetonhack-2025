import requests

def get_brookies():
    response = requests.get('https://www.passetonhack.fr/api/storage/challenges/19b86d6b326101548c9f0a70e7411423/brookie/brookie.html')
    print(response.text)

print(get_brookies())