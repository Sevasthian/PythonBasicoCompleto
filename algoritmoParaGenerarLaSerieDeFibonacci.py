numero1 = float(input("Que cantidad de numeros necesita para serie de Fibonacci: "))
A = 0
B = 1
C = 1
while C <= numero1:
    if C % 2 == 1:
        print(A, end=",")
        A += B
    else:
        print(B, end=",")
        B += A
    C += 1

