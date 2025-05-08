print ("\tBIENVENU DANS LE GENERATEUR DE TRIANGLE")

try:
    etage = int(input("Entrez le nombre d'étage de votre triangle: "))
except ValueError:
    print("Vous avez entré une mauvaise valeur. Entrez un nombre à virgule")
else:
    symbole = input("Entrez un symbole pour réaliser la pyramide: ")
    x = 0
    while x >= 0:
        x = x + 1
        for i in range(x):
            print(f"{symbole}", end=" ")
        print()
        if x == (etage + 1):
            break
