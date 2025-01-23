import random

import string


def generate_candidate():

    # Générer une chaîne de 31 caractères aléatoires pour le contenu du flag

    core = ''.join(random.choices(string.ascii_lowercase + string.digits, k=31))

    candidate = f"FLAG{{{core}}}"

    

    # Vérifier si le candidat respecte les conditions

    if check(candidate):

        return candidate

    return None


def check(value):

    if len(value) != 37:

        return False

    if not value.startswith("FLAG{") or not value.endswith("}"):

        return False

    

    # Extraire les parties nécessaires

    inner_value = value[5:-1]  # Contenu entre FLAG{ et }

    

    # Conditions basées sur le code JavaScript

    r = 812

    w = hex(5701445809426169 * r)[2::2]

    

    # Vérifications

    if not inner_value.startswith("561364ff"):

        return False

    if not inner_value.endswith("656bb43"):

        return False

    if inner_value.split("96d")[1] == "":

        return False

    if inner_value.split("a")[1] == "":

        return False

    if inner_value.split("b")[2] != "":

        return False

    if inner_value.split("b6")[0] == "":

        return False

    if not aaa(inner_value.split("ff")[0][:-1]):

        return False

    

    return True


def aaa(k):

    # Implémentation de la fonction aaa

    return int(k, 16) == r * 7912.556411033646


# Lancer la recherche

while True:  # Limiter le nombre de tentatives

    flag = generate_candidate()

    if flag:

        print(f"Flag trouvé : {flag}")

        break
