#Creo una funcion que comrpueba si un numero es primo o no
import sys


def primo(n):
    if n<=1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

#Recibo los numeros como inputs
num1 = int(input("Introduce el primer numero: "))

#Checkeo que num1 no sea menor que 0
if num1 < 0:
    print("Error, no se puede introducir un valor menor que 0")
    sys.exit(1)


num2 = int(input("Introduce el segundo numero: "))

#Checkeo que num2 no sea menor que 0
if num2 < 0:
    print("error, no se puede introducir un valor menor que 0")
    sys.exit(1)

#Compruebo que numero es el mayor para hacer el rango correctamente
if num1>num2:
    #De ser asi, los intercambio para que el programa funcione correctamente
    aux = num1
    num1=num2
    num2=aux

#Muestro los numero primos en el rango indicado
print(f"Numeros primos entre {num1} y {num2} (incluidos ambos):")
for num in range(num1, num2+1):
    if primo(num):
        print(num)