# r = 16495

# def aaa(k): 
#     return int(k,16)==r*7912.556411033646

# sFlag = ""
# def thecheck(func):
#     def inner(*args, **kwargs):
#         if len(sFlag) != 37:
#             print("Flag invalide : longueur incorrecte")
#         elif func(sFlag):
#             #window.location=sFlag.replace("FLAG{","").replace("}","")+".html"
#             print(sFlag)

#             sEndURL = sFlag.replace("FLAG{","").replace("}","")+".html"
#             print(sEndURL, sFlag)

#             return True

#     return inner

# @thecheck
# def check(value):
#     try:

#         global aa; 
#         r = 812

#         def StartWorldf03(n):
#             w = 5701445809426169 * 812 # On calcule w
#             w = hex(w) # On convertit w en hexadécimal

#             w = w[2::2] # On prend un caractère sur deux à partir du 2ème

#             return n.startswith(w[:-2]) # On retourne si n commence par w sans les 2 derniers caractères


#         def endswithAfterFirstA(n):
#             return n.endswith("656bb43")

#         def startswithAfterb6(m):
#             return m.startswith("561364ff")
        
#         print(value.split("b"))
        
#         print("Test :")
#         if not value.startswith("FLAG{"):
#             print("La chaîne ne commence pas par FLAG{")
        
#         if not StartWorldf03(value.split("{96d")[1]):
#             print("La chaîne ne commence pas par la valeur calculée")
        
#         if not value.endswith("}"):
#             print("La chaîne ne se termine pas par }")

#         if not endswithAfterFirstA(value.split("a")[1][::-1]):
#             print("La chaîne ne se termine pas par 656bb43")

#         if not value.split("b")[2]:
#             pass
#         else:
#             print("La chaîne contient un b")
        
#         if not startswithAfterb6(value.split("b6")[1]):
#             print("La chaîne ne commence pas par 561364ff")
        
#         if not aaa(value.split("f" * 2)[bool(r)][:-1]):
#             print("La chaîne ne commence pas par la valeur calculée pour aaa(k)")


#         return all((value.startswith("FLAG{"),
#                     StartWorldf03(value.split("{96d")[1]),

#                     value.endswith("}"),

#                     endswithAfterFirstA(value.split("a")[1][::-1]),

#                     not value.split("b")[2],

#                     startswithAfterb6(value.split("b6")[1]),

#                     aaa(value.split("f" * 2)[bool(r)][:-1])))
#     except:
#         return False
    
# # sFlag = "FLAG{96d" + "43809b7c" + "561364ff" + "7c78a72" + "}"

# # print(len(sFlag))

# # print(check(sFlag))

# # Étape 1 : calcul de la valeur cible pour aaa(k)
# # Étape 1 : calcul de la valeur cible pour aaa(k)
# r = 16495
# target_value = r * 7912.556411033646

# # Étape 2 : calcul du début pour StartWorldf03
# w = 5701445809426169 * 812
# w = hex(w)[2::2][:-2]  # La partie hexadécimale nécessaire

# # Étape 3 : assembler les autres parties du flag
# part1 = "FLAG{"  # Le flag commence par "FLAG{"
# part2 = "96d"  # On utilise un fragment comme exemple
# part3 = w  # La valeur calculée pour StartWorldf03
# part4 = "34bb656"  # Inverser cette chaîne pour respecter endswithAfterFirstA
# print(part4)
# part5 = "561364ff"  # Une partie du flag
# part6 = "7c78a72"  # La partie à ajouter

# # Construction du flag en respectant les conditions exactes
# sFlag = part1 + part2 + part3 + part6 + part4 + part5 + "}"

# sFlag = "FLAG{96d43809bca34bb6561364ff7c78a72}"

# print(len(sFlag), sFlag)

# # Vérification des conditions
# if check(sFlag):
#     print("Flag reconstruit : ", sFlag)
# else:
#     print("Le flag reconstruit ne passe pas toutes les conditions.")

r = exec('global aaa; aaa = lambda k: int(k,16)==r*7912.556411033646') or 16495

sFlag = "FLAG{96d5942db3a34bb6561364ff7c78a72}"
def thecheck(func):
    def inner(*args, **kwargs):
        if len(sFlag) != 37:
            #window.setInvalidMessage()
            print("Incorrect length")
        elif func(sFlag):
            #window.location=sFlag.replace("FLAG{","").replace("}","")+".html"
            print("Tout est bon : ", sFlag)
        else:
            #window.setInvalidMessage()
            print("Flag invalide")
    return inner

@thecheck
def check(value):
    print(value)
    #try:
    global aa; r = 812

    print(0)
    def aa(n):
        global aa, r; 
        print("r : ", r)
        w = hex(5701445809426169 * r)[2::2]


        def aa(m):
            global aa; r = 388

            print("second aa")
            aa = lambda k: k.startswith("561364ff")

            return m.endswith("656bb43")

        print("first aa", w[:-2])

        return n.startswith(w[:-2])

    print(1, value.split("{96d")[1 == 1])

    aFirst = aa(value.split("{96d")[1 == 1])
    print(2)
    aSecond = aa(value.split("a")[1 or 2][::-(not 0)])

    print("656bb43"[::-1])

    print(3)
    aThree = aa(value.split("b6")[r == 812])

    print("FLAG{ :", value.startswith("FLAG{"))
    print("aFirst :", aFirst)
    print("} : ", value.endswith(chr(125)))
    print("aSecond : ", aSecond)
    print("not b",  not value.split("b")[2])
    print("aThree : ", aThree)
    print("aaa", aaa(value.split("f" * 2)[bool(r)][:-1]))
    
    return all((value.startswith("FLAG{"),
                aFirst,
                value.endswith(chr(125)),
                aSecond,
                not value.split("b")[2],
                aThree,
                aaa(value.split("f" * 2)[bool(r)][:-1])))
    # except Exception as e:
    #     print("Exception : ", e)
    #     print("Traceback : ", e.with_traceback())

       # return False

check(sFlag)