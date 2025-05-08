print("\tBIENVENU DANS LA BOUTIQUE DE FRUITS EN LIGNE")

fruits = ["Pomme", "banane", "orange", "ananas", "citron"]
inventaire = {
    "pomme" : {'prix' : 200.00,
               'quantité' : 10},
    "banane" : {'prix' : 250.00,
                'quantité' : 6},
    "orange" : {'prix' : 150.00,
                'quantité' : 50},
    "ananas" : {'prix' : 400.00,
                "quantité" : 20},
    "citron" : {'prix' : 275.00,
                'quantité' : 17}
}
print("Voici les produits que nous avons: ")
for produit in fruits:
    if produit == "citron":
        print(f"{produit}", end=".\n")
    print(f"{produit}", end=", ")
i = 0
while i == 0:
    demande = input("Quel fruit voulez vous ?: ")
    fruit = demande.lower()
    produit_prix = inventaire[f"{fruit}"]['prix']
    produit_quantité = inventaire[f"{fruit}"]['quantité']
    if fruit in inventaire:
        print(f"Le prix de cet article est estimé à {produit_prix} FCFA")
        i = 0
        while i == 0:
            try:
                achat = int(input(
                    f"Entrez le nombre de {fruit} que vous voulez commander(il enreste encore {produit_quantité}): "))
            except ValueError:
                print("La valeur que vous vennez d'entrer n'est pas un nombre entier positif. Réessayez.")
            if achat == 0:
                print("La valeur que vous vennez d'entrer n'est pas un nombre entier positif. Réessayez.")
            elif achat >= produit_quantité:
                print(
                    "La limite de la disponibilité de ce produit est atteinte. Réessayez d'entrer un nombre inférieur à cette limite.")
            else:
                autre_demande = input("Merci pour votre achat. Autre chose ?(O/N): ")
                if autre_demande.lower() == "o":
                    break
                else:
                    break
    if autre_demande.lower() == "n":
        print("D'accord à la prochaine !")
        break