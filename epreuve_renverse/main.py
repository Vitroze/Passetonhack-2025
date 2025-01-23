# Chaîne d'entrée
input_string = "9xr=J}<[nDSqRd^)X"

# Valeurs de XOR extraites du code C
xor_values = [ord('9'), ord('x'), ord('r')]  # Valeurs basées sur les caractères

# Liste pour stocker la chaîne transformée
transformed_string = ""

# Appliquer XOR et transformation
for i, char in enumerate(input_string):
    # Obtenir la valeur ASCII du caractère
    char_value = ord(char)
    print(f"Char: {char} | Ord: {char_value}")

    # Appliquer XOR avec les valeurs du tableau
    xor_result = char_value ^ xor_values[i % len(xor_values)]
    print(f"XOR result: {xor_result}")

    # Appliquer un ajustement (-5) comme dans le code C
    transformed_value = xor_result - 5
    print(f"Transformed: {transformed_value}")

    # S'assurer que la transformation produit un caractère valide
    if transformed_value < 32:  # Si la valeur est inférieure à un caractère imprimable
        transformed_value += 95  # Ajuster dans la plage des caractères imprimables

    # Vérifier si la valeur est toujours dans la plage des caractères ASCII imprimables
    if transformed_value < 32:
        transformed_value = 32  # Remettre au minimum de la plage

    # Ajouter le caractère transformé
    transformed_string += chr(transformed_value)

# Afficher le résultat final
print("Flag transformé :", transformed_string)
