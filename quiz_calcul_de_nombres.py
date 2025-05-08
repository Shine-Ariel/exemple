import random
import time

print("\tBIENVENU DANS LE QUIZ SUR LES CALCULS")
time.sleep(2)

n = 0
for i in range (1, 6):
    nbre_1 = random.randint(0, 100)
    nbre_2 = random.randint(0, 100)
    calcul = nbre_1 + nbre_2
    try:
        réponse = int(input(f"Question {i}: Combien font {nbre_1} + {nbre_2} ? "))
        if calcul == réponse:
            print("Correct")
            n += 1
        else:
            print("Incorrect")
    except ValueError:
        print("Incorrect")
time.sleep(2)
note = int((n / 5) * 100)
print(f"Votre note finale est {note}/100")
