numero = int(input("Registre algún número: "))
S = 1
V = 0

while S <= numero:
    if numero % S == 0:
        V = V + 1
    S = S + 1
if V == 2:
    print("El numero ",numero, " es primo")
else:
    print("El numero ",numero, " no es primo")
