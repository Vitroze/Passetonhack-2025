import random
import datetime
import requests

#aaa = lambda k: int(k,16)==r*7912.556411033646 or 16495

r = exec('global aaa; aaa = lambda k: int(k,16)==r*7912.556411033646') or 16495


test_flag = ""
bFind = False

def thecheck(func):
    global test_flag
    global bFind

    def inner(*args, **kwargs):
        if len(test_flag) != 37: # Un flag fait 37 caractères
            print("Flag invalide : longueur incorrecte")
        elif func(test_flag):
          #  window.location=test_flag.replace("FLAG{","").replace("}","")+".html"

            print(test_flag)
            sEndURL = test_flag.replace("FLAG{","").replace("}","")+".html"

            response = requests.get("https://www.passetonhack.fr/api/storage/challenges/19b86d6b326101548c9f0a70e7411423/tobana_pirates/{sEndURL}")

            if response.status_code == 200:
                print("URL valide")

                print(sEndURL, test_flag)

                bFind = True

                print(response.status_code)
            


            return True
    return inner

def isStartWorldf03(n):
    w = 5701445809426169 * 16495 # On calcule w
    w = hex(w) # On convertit w en hexadécimal

    w = w[2::2] # On prend un caractère sur deux à partir du 2ème

    print(w)

    return n.startswith(w[:-2]) # On retourne si n commence par w sans les 2 derniers caractères

def endswithFlag(n):
    return n.endswith("656bb43")

def startswithFlag(n):
    return n.startswith("561364ff")

# FLAG{96d43809b34bb656

tAttemptsPossible = []
@thecheck
def check(value):

    # FLAG{96d5942db334bb656561364ff7c78a72}

    try:
        global aa; 

        iStart = value.split("{96d")[1] # On prend la partie de value après le premier {96d | Simplification de value.split("{96d")[1 == 1]

        iEnd = value.split("a")[1][::-1] # On prend la partie de value après le premier a et on l'inverse | Simplification de value.split("a")[1 or 2][::-(not 0)]

        iStartWithFlag = value.split("b6")[1] # On prend la partie de value après le premier b6 si r == 812 | Simplification de value.split("b6")[r == 812]

        iAAA = value.split("f" * 2)[1][:-1] # On prend la partie de value après le premier ff si r est vrai | Simplification de value.split("f" * 2)[bool(r)][:-1]

        if not value.startswith("FLAG{"):
            print("Flag invalide : ne commence pas par FLAG{")
        
        if not isStartWorldf03(iStart):
            print("Flag invalide : ne commence pas par la bonne valeur")
        
        if not value.endswith("}"):
            print("Flag invalide : ne se termine pas par }")
        
        if not endswithFlag(iEnd):
            print("Flag invalide : ne se termine pas par l'inverse de 656bb43. C'est à dire : 34bb656")
            sText = f"Impossible function endswithFlag : {value} ; Error : {iEnd}"

            
            if sText not in tAttemptsPossible:
                tAttemptsPossible.append(sText)

        
        if not value.split("b")[2]:
            pass
        else:
            print("Flag invalide : contient un b")

            sText = f"Impossible function value.split('b')[2] > 2 : {value} ; Error : {value.split('b')[2]}"

            if sText not in tAttemptsPossible:
                tAttemptsPossible.append(sText)
        
        if not startswithFlag(iStartWithFlag):
            print("Flag invalide : ne commence pas par 561364ff après b6")

            sText = f"Impossible function startswithFlag : {value} ; Error : {iStartWithFlag}"

            if sText not in tAttemptsPossible:
                tAttemptsPossible.append(sText)
        
        if not aaa(iAAA):
            #print("Flag invalide : valeur incorrecte")

            sText = f"Impossible function aaa : {value} ; Error : {iAAA}"

            if sText not in tAttemptsPossible:
                tAttemptsPossible.append(sText)


        return all((value.startswith("FLAG{"), 
                isStartWorldf03(iStart),
                value.endswith("}"), # chr(125) == "}"
                endswithFlag(iEnd), 
                not value.split("b")[2], 
                startswithFlag(iStartWithFlag), 
                aaa(iAAA)))
    except Exception as e:
        return False

iStart = datetime.datetime.now()
print(f"=== Recherche du flag - Bruteforce ({iStart}) ===")

def find_flag():
    global test_flag

    iAttempt = 0

    # EXAMPLE FLAG 
    """
        FLAG{ --> OK
        96d --> OK
        5942db3d7 --> OK (isStartWorldf03)
        34bb656 --> OK (endswithFlag - Doit terminer par 34bb656)
        561364ff --> OK (startswithFlag, si b6)
        7c78a72
    """

        # Générer un flag avec une approche plus ciblée
    # sFlag = "FLAG{96d43809b"
    test_flag = "FLAG{96d5942db334bb656561364ff7c78a72}"
    print(len(test_flag))


    check(test_flag)




# Lancer la recherche
flag = find_flag()

if flag:
    print(f"Flag trouvé : {flag}")
else:
    
    print("Flag non trouvé.")

    print("Tentatives possibles :")
    # for sAttempt in tAttemptsPossible:
    #     print(sAttempt)

print(f"Durée de l'attaque : {datetime.datetime.now() - iStart}")
print("=== Fin de l'attaque ===")
