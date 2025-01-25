# Chemin d'accès au fichier source
input_file = "args.txt"
# Chemins des fichiers de sortie
output_files = ["arg1.txt", "arg2.txt", "arg3.txt"]

# Initialisation des fichiers de sortie
with open(output_files[0], "w") as f1, open(output_files[1], "w") as f2, open(output_files[2], "w") as f3:
    # Lecture des données d'entrée
    with open(input_file, "r") as infile:
        for line in infile:
            # Nettoyage des lignes
            line = line.strip()
            if not line:
                continue  # Passer les lignes vides
            
            # Extraction des arguments
            arg1, arg2, arg3 = "", "", ""
            for part in line.split("&"):
                if part.startswith("arg1="):
                    arg1 = part[5:]  # Supprimer 'arg1='
                elif part.startswith("arg2="):
                    arg2 = part[5:]  # Supprimer 'arg2='
                elif part.startswith("arg3="):
                    arg3 = part[5:]  # Supprimer 'arg3='
            
            # Écriture des arguments dans les fichiers correspondants
            f1.write(arg1 + "\n")
            f2.write(arg2 + "\n")
            f3.write(arg3 + "\n")