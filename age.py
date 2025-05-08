def determinr_categorie(age):
    if age < 12 and age > 0:
        print(f"Vous avez {age} ans, donc vous etes dans la catégorie Enfant")
    elif age >= 12 and age < 18:
        print(f"Vous avez {age} ans, donc vous etes dans la catégorie Adolescent")
    elif age >= 18 and age < 65:
        print(f"Vous avez {age} ans, donc vous etes dans la catégorie Adulte")
    elif age > 65:
        print(f"Vous avez {age} ans, donc vous etes dans la catégorie Senior")
    else:
        print("Entrez votre vrai age")

while True:
    try:
        age = int(input("Entrez votre age: "))
        determinr_categorie(age)
    except ValueError:
        print("Entrez votre vrai age")