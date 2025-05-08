import time
print("\tBIENVENU DANS LE DETECTEUR D'ETAT DE L'EAU")
time.sleep(2)

while True:
    try:
        celcius = float(input("Entrez la température de l'eau en celcius: "))
        time.sleep(2)
        if celcius < 0:
            print(f"A {celcius}°C, l'eau est à l'état solide")
        elif celcius >= 0 and celcius < 100:
            print(f"A {celcius}°C, l'eau est à l'état liquide")
        else:
            print(f"A {celcius}°C, l'eau est à l'état gazeux")
    except ValueError:
        print("Entrez une température")
