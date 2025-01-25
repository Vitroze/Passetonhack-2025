import base64
import urllib.parse
import string


def decode_arg1(data):
    """Décode l'argument 1 en base64."""
    try:
        decoded_data = base64.b64decode(data).decode('utf-8')
        return decoded_data
    except Exception:
        return None


def decode_arg2(data):
    """Décode l'argument 2 en interprétant les encodages URL."""
    try:
        decoded_data = urllib.parse.unquote(data)
        return decoded_data
    except Exception:
        return None


def decode_arg3(data):
    """Inverser la chaîne comme exemple de traitement personnalisé."""
    try:
        return data[::-1]
    except Exception:
        return None


def is_valid_string(value):
    """
    Vérifie si une chaîne est valide :
    - Contient uniquement des lettres (sans chiffres ni ponctuation).
    """
    if value is None:
        return False
    return all(char.isalpha() or char.isspace() for char in value)


def process_log_line(line):
    """Traite une ligne du fichier de logs pour extraire les arguments et vérifier s'ils sont valides."""
    try:
        # Extraire la partie des arguments (après "?")
        if "GET /payload?" in line:
            args_part = line.split("GET /payload?")[1].split(" HTTP/1.1")[0]
            args = args_part.split("&")

            # Stocker les arguments sous forme de dictionnaire
            decoded_args = {}
            for arg in args:
                key, value = arg.split("=")
                decoded_value = None

                # Décoder selon l'argument
                if key == "arg1":
                    decoded_value = decode_arg1(value)
                elif key == "arg2":
                    decoded_value = decode_arg2(value)
                elif key == "arg3":
                    decoded_value = decode_arg3(value)

                # Vérifier la validité de la chaîne
                if decoded_value and is_valid_string(decoded_value):
                    decoded_args[key] = decoded_value

            return decoded_args
    except Exception:
        return None


def process_log_file(filepath):
    """Traite un fichier contenant des logs HTTP."""
    results = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                if "GET /payload?" in line:
                    decoded_data = process_log_line(line)
                    if decoded_data:  # Ajouter uniquement les données valides
                        results.append(decoded_data)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filepath}' est introuvable.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

    return results


if __name__ == "__main__":
    # Spécifie le chemin du fichier contenant les logs
    log_file = "intercepted_data.txt"  # Remplace par le chemin de ton fichier
    decoded_results = process_log_file(log_file)

    # Afficher les résultats valides
    with open("data_recorded.txt", "w", encoding="utf-8") as f:  # Ajout de encoding="utf-8"
        for i, result in enumerate(decoded_results, 1):
            print(f"=== Ligne {i} ===")
            for key, value in result.items():
                print(f"{key}: {value}")
                
                f.write(f"L.{i} {key}: {value}\n")
            print()
