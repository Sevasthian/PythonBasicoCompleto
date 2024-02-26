print("Ingrese un numero")
num = int(input())

factorial=1
for i in range(1, num+1):
    factorial*=i
print("El factorial de", num,"es: ", factorial)
 
 