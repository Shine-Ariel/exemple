import time
import random
print("\t\tPIERRE-FEUILLE-CISEAUX !!")

time.sleep(1)
print("\tVOICI LES REGLES DU JEU:\nVOUS JOUEZ CONTRE L'ORDINATEUR. VOICI LES SITUATIONS\nOU IL Y A UNE VICTOIRE:")
print("FEUILLE => PIERRE: VICTOIRE !\nPIERRE => CISEAUX: VICTOIRE !\nCISEAUX => FEUILLE: VICTOIRE !")
print("EN CAS D'UNE EGALITE, AUCUN JOUEUR NE GAGNE.")
n = 0
time.sleep(3)
choix = {"PIERRE", "PIERRE", "FEUILLE", "FEUILLE", "CISEAUX", "CISEAUX"}
ordinateur = {"p": "PIERRE",
              "f": "FEUILLE",
              "c": "CISEAUX"}
player = input("Entrez votre nom: ").upper()
for x in choix:
    joueur = input("Entrez une p(pour pierre), f(pour feuille) ou c(pour ciseaux): ").lower()
    for i in range(3, 0, -1):
        print(f"\t{i}\n", end="")
        time.sleep(1)
    print(f"ORDINATEUR: {x} !")
    if joueur in ordinateur:
        print(f"{player}: {ordinateur[joueur]} !")
        time.sleep(1)
        if joueur == "p" and x == "CISEAUX":
            print("Vous remportez cette manche !")
            n += 1
        elif joueur == "f" and x == "PIERRE":
            print("Vous remportez cette manche !")
            n += 1
        elif joueur == "c" and x == "FEUILLE":
            print("Vous remportez cette manche !")
            n += 1
        elif ordinateur[joueur] == x:
            print("MATCH NUL !")
        else:
            print("L'ordinarteur remporte cette manche !")
    else:
        print(f"{player}: {joueur.upper()} !")
        print("L'ordinarteur remporte cette manche !")
    time.sleep(1)
if n >= 2:
    print("VOUS AVEZ GAGNE !!")
else:
    print("VOUS AVEZ PERDU !!")