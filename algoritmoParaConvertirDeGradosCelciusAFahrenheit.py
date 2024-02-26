def convertir(c):
    f = (c*9/5) + 32
    return f

c = float(input("ingresa los grados Celsius: "))
print("La conversion de grados fahrenheit es: ",convertir(c) )
