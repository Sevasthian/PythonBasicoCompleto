number1 = int(input("Ingrese el numero: "))
number2 = int(input("Ingrese el numero: "))
number3 = int(input("Ingrese el numero: "))

if number2 < number1 > number3:
    print("El numero mayor es el primer numero:",number1)
elif number1 < number2 > number3:
    print( "El numero mayor es el segundo numero: ",number2)
elif number1 < number3 > number2:
    print( "El numero mayor es el trecer numero: ",number3)

elif number1 == number2  > number3 :
    print("El numero mayor es el primer numero:",number2) 

elif number1 == number3  > number2 :
    print("El numero mayor es el primer numero:",number1)
elif number2 == number3  > number1 :
    print("El numero mayor es el primer numero:",number3)
elif number1 == number2  == number3 :
    print("El numero mayor es el primer numero:",number2)
    