nombres = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 0
for i in nombres:
    for a in nombres:
        if i >= a:
            print(f"{i} est supérieur à {a}")
            n+=1
        else:
            print(f"{i} est inférieur à {a}")
            n = 0
if n == len(nombres):
    print(f"Le maximum de cette pile est {i}")