#Pillamos la lista como input del user
entrada = input("Introduce una lista de enteros, separados por espacio: ")

#Convertimos la "lista" recibida (que es un string) a una lista de enteros (ints)
lista = list(map(int, entrada.split(" "))) #map lo que hace es transformar los elementos de un iterable al tipo especificado

#Inicializamos la lista donde vamos a ir añadiendo elementos hasta llegar a un par
lista_final = []

counter = 0 #Contador para no salirme de rango de lista

par_found = False #Boolean para finalizar bucle while al encontrar num par

while counter < len(lista) and not par_found:
    if lista[counter] % 2 == 0: #Numero es par, actualizo boolean
        par_found = True
    else:
        lista_final.append(lista[counter]) #Si el numero no es par, lo añado a la lista resultado
    counter+=1

print(f"Resultado: {lista_final}")