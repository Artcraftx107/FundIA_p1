#Pedir input (mail)
mail = input("Introduce el correo electronico: ")

#Checkeo si es un correo valido (tiene un solo @, obligatoriamente)
if "@" not in mail:
    print("Error: el correo introducido no tiene @")
elif mail.count("@") > 1:
    print("Error: el correo introducido tiene mas de un @")
else:
    #Uso .split para dividir el input tras el checkeo
    user, domain = mail.split("@")

    #Compruebo que el mail introducido tiene user y dominio
    if user and domain:
        print(user)
        print(domain)
    else:
        print("Error: el correo introducido no tiene user o dominio")
