import time

print("BIENVENU DANS LE VERIFICATEUR DE MOT DE PASSE")
time.sleep(2)
code_de_base = "les_etres_humains_sont_des_chiens_à_",100%"
while len(code_de_base) >= 40:
    code_a_entrer = input("Entrez votre mot de passe: ")
    if len(code_a_entrer) > 40:
        print("Le ccode de vous avez entré est trop long")
    elif len(code_a_entrer) < 40:
        print("Le ccode de vous avez entré est trop court")
    elif code_de_base == code_a_entrer:
        print("Correct")
        break
