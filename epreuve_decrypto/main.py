import sys

def FUN_000111cd(param_1):
    """
    Retourne la longueur d'une chaîne de caractères.
    param_1 : chaîne de caractères (string).
    """
    local_8 = 0

    for char in param_1:
        if char == '\0': 
            break

        local_8 += 1

    return local_8


def FUN_000111fe(param_1, param_2):
    """
    Copie les 16 premiers caractères de param_2 dans param_1, 
    avec un caractère nul '\0' ajouté à la fin.
    
    param_1 : Liste ou buffer de destination (au moins 17 éléments).
    param_2 : Liste ou chaîne source (au moins 16 éléments).
    """

    print(param_1, len(param_2))

    # Si param_1 est une chaîne, le convertir en liste
    param_1 = list(param_1)

    # Copier les 16 premiers caractères de param_2 dans param_1
    param_1[:16] = list(param_2[:17])  # Assurez-vous que param_2 est une liste de caractères

    # Ajouter le caractère nul '\0' à la fin
    param_1[16] = '\0'

    return param_1

def FUN_000112a9(param_1):
    """
    Transforme un tableau d'octets selon une règle donnée.

    param_1 : Liste d'octets (modifiée en place).
    """
    PTR_DAT_00014008 = [0x78, 0x30, 0x34]  # Utilisation des 3 premières valeurs

    # Vérifier si param_1 a bien 17 éléments
    if len(param_1) < 17:
        raise ValueError("param_1 doit contenir au moins 17 éléments.")

    # Parcours des 17 premiers octets
    for local_10 in range(17):
        # Conversion du caractère en code ASCII avec ord()

        print(param_1[local_10])
        char_value = ord(param_1[local_10])
        
        # Applique l'opération XOR et ajuste le résultat
        param_1[local_10] = (
            local_10 + (char_value ^ PTR_DAT_00014008[local_10 % 3]) - 5
        ) & 0xFF  # Assurer que le résultat est un octet (0-255)

    return 0


def reverse_FUN_000112a9(param_1):
    """
    Inverse la transformation d'un tableau d'octets selon la règle donnée.
    
    param_1 : Liste d'octets (modifiée en place).
    """
    PTR_DAT_00014008 = [0x78, 0x30, 0x34]  # Utilisation des 3 premières valeurs

    # Vérifier si param_1 a bien 17 éléments
    if len(param_1) < 17:
        raise ValueError("param_1 doit contenir au moins 17 éléments.")

    # Parcours des 17 premiers octets
    for local_10 in range(17):
        # Récupérer la valeur modifiée avant l'ajout de local_10 et de la soustraction de 5
        modified_value = ord(param_1[local_10])  # Convertir en code ASCII
        
        # Annuler l'ajout de local_10 et la soustraction de 5
        original_value = (modified_value + 5 - local_10) & 0xFF
        
        # Appliquer l'opération inverse du XOR
        param_1[local_10] = chr(original_value ^ PTR_DAT_00014008[local_10 % 3])

    return ''.join(param_1)  # Reconvertir en chaîne de caractères

# Exemple d'utilisation
input_string = "9xr=J}<[nDSqRd^)X"
print("decode : ", reverse_FUN_000112a9(list(input_string)))  # Convertir en liste avant de passer à la fonction


"""

    PTR_DAT_00014008 = [0x78, 0x30, 0x34] 

    for local_10 in range(17):
        param_1[local_10] = (
            local_10 + (param_1[local_10] ^ PTR_DAT_00014008[local_10 % 3]) - 5
        ) & 0xFF  

    return 0
"""


def FUN_00011252(param_1, param_2):
    """
    Compare les 17 premiers octets de deux listes.
    
    param_1 : Liste d'octets (le premier tableau à comparer)
    param_2 : Liste d'octets (le deuxième tableau à comparer)
    
    Retourne :
        - 1 si les 17 premiers octets sont identiques.
        - 0 sinon.
    """

    print(param_1)
    for local_5 in range(17): 
        print(param_1[local_5], param_2[local_5])
        if param_1[local_5] != param_2[local_5]:
            return 0 
    return 1 

def main(param_1, param_2):
    print([0] * 4)
    if param_1 < 2:
        print("Pas assez d'arguments")
        sys.exit(1)

    local_34 = param_2
    local_26 = [0] * 4 
    
    local_2c = FUN_000111cd(local_34)  

    if local_2c == 17: # 0x11 = 17
        local_26 = FUN_000111fe(local_26, local_34)  
        print(local_26)
        local_2d = FUN_000112a9(local_26) 
        
        if local_2d == -1:
            print("C'est un échec sur mon local_2d ...")
            return 1
        
        magic_value = "9xr=J}<[nDSqRd^)X" 
        iVar2 = FUN_00011252(local_26, magic_value)
        
        if iVar2 == 0:
            print("C'est un échec ... Valeur qui ne correspond pas.")
            return 1
        else:
            print("Bravo, le flag est : %s" % local_34[1])
            return 0
    else:
        print("C'est un échec ...")
        return 1

"""

    Le flag doit faire 17 caractères.
    FUN_000111fe copie les 16 premiers caractères de param_2 dans local_26. Et ajoute un caractère nul à la fin. 



    FLAG : ................0
"""

# Simulation d'une exécution si le script est appelé directement.
if __name__ == "__main__":
    # Exemple d'arguments : nombre et liste de paramètres.
    param_1 = len(sys.argv)
    param_2 = sys.argv
    sys.exit(main(2, "9xr=J}<[nDSqRd^)X"))
