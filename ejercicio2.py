#Recibo como inputs el nombre, precio por unidad y numero de unidades de un prodcuto
import sys

nombre = input("Introduce el nombre del producto: ")

#Si el nombre del producto esta vacio, termina el programa
if not nombre:
    print("Error, el nombre esta vacio")
    sys.exit(1)

precioxunit = float(input("Introduce el precio por unidad: "))

#Si el precio por unidad esta vacio o es menor que 0, termina el programa
if precioxunit <0:
    print("Error, el precio por unidad no puede ser menor a 0")
    sys.exit(1)

units = int(input("Introduce el numero de unidades: "))

#Si el numero de unidades esta vacio o es menor que 0, termina el programa
if units <0:
    print("Error, el numero de unidades no puede ser menor a 0")
    sys.exit(1)

#Tras recibir toda la info y checkearla, calculamos el total
total = precioxunit*units

#Lo de 8.2f es para que se cumpla lo que especifica el enunciado (el precio por unidad con 6 dígitos enteros y 2 decimales), la forma en la que funciona es la siguiente:
# Al ser 6 enteros y 2 decimales, necesitamos 8 espacios (de ahi el 8) y el numero despues del . especifica cuantos de los espacios cogidos son decimales
# por ejemplo, para coger 4 enteros y 4 decimales, escribiria 8.4f (4+4.numDecimales)
print(f"{nombre}: {units} unidades x {precioxunit:8.2f}€ = {total:10.2f}€")