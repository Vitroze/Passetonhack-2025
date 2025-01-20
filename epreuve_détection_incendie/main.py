input_s = "Impacts: [-6, 0, -6, 9, -9, 1, 1, 3, -10, 9, -4, -3, -4, -5, -3, 5, 7, 8, -4, -10, 5, -2, 10, 4, -8, -4, -7, -6, 8, -4, 8, -2, 3, -2, -2, 7, 6, 7, 7, -2, 1, -6, -1, 7, 2, -1, 5, -2, -2, 8, 5, 7, -2, 1, -6, 3, 1, -5, 3, 7, 7, 0, 3, 3, 8, -1, 7, -1, -2, 5, -8, -5, -8, 6, 9, -6, -5, 3, 8, -3, 6, -2, 9, 9, 1, 1, -10, 6, -7, -2, 1, -9, -4, 6, 10, -6, -8, -4, -5, 7, -6, -7, 5, -6, 1, -9, 1, 2, 6, -5, -5, 6, -2, -1, 3, -10, -5, -7, 1, -6, 2, -1, -1, 4, 7, 1, -10, -6, 5, -8, -2, 8, 10, -7, -5, 0, 2, -9, 7, 4, -2, -3, 6, 5, -9, -7, -6, -8, -5, 8, 1, 8, -4, -5, -6, 10, 3, -2, -4, 6, 9, 7, -7, 3, 1, 0, 8, 10, 4, 10, -9, 7, -6, 1, 10], K: 19"
iK = int(input_s.split("K:")[1].strip())

# Extraction de la liste d'impacts
tImpacts = input_s[10:len(input_s)-8]
tImpacts = [int(iNumber) for iNumber in tImpacts.split(",")]

# Initialisation des variables
iCount = 0
iSommeCumulative = 0
tTableHachage = {0: 1}  # Table pour suivre les sommes cumulatives

# Parcours des impacts
for i in tImpacts:
    iSommeCumulative += i  # Mise à jour de la somme cumulative
    
    # Vérification si un sous-tableau valide est trouvé
    if iSommeCumulative - iK in tTableHachage:
        iCount += tTableHachage[iSommeCumulative - iK]
    
    # Mise à jour de la table de hachage
    tTableHachage[iSommeCumulative] = tTableHachage.get(iSommeCumulative, 0) + 1

print(iCount)