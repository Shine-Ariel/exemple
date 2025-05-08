import time

print("\tBIENVENU DANS LE COMPTEUR A REBOURS")
temps = int(input("Entrez le temps en secondes: "))

for i in range(temps, 0, -1):
    secondes = i % 60
    minutes = int((i / 60)) % 60
    heure = int((i / 3600)) % 60
    print(f"{heure:02}:{minutes:02}:{secondes:02}")
    time.sleep(1)

print("Il EST L'HEURE")