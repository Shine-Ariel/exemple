L1 = []
L2 = []
n = 0
i = 0

try:
    limite = int(input("Combien d'éléments voulez-vous dans votre liste ?"))
except limite < 0:
    print("Entrez un entier")

while i < limite:
    try:
        nbre = int(input("Entrez un nombre: "))
        L1.append(nbre)
    except ValueError:
        print("Entrez un entier")
    i += 1

for element in L1:
    n += element
moyenne = n / i
print(f"La somme de cette liste est: {n}")
print(f"La moyenne de cette liste est: {moyenne}")
print(f"Le nombre le plus grand de cette liste est: {max(L1)}")
print(f"Le nombre le plus petit de cette liste est: {min(L1)}")
for pair in L1:
    if pair % 2 == 0:
        L2.append(pair)
print(f"Les nombres pairs de la liste initiale sont : {L2}")

