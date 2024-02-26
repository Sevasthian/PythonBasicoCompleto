lista = [6,5,7,9,9,9,9,4,6,2]
valores = len(lista)
suma = 0

for numero in lista:
    suma += numero

promedio = suma / valores
print(f'El promedio es: {promedio}')