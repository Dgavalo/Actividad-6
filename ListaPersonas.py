diccionario ={} #key:cédula dato:nombre y apellido
def limpiador (linea):
    lineaPartida = linea.split(",")
    lineaCedula = lineaPartida[0]
    lineaNombre = lineaPartida[1]
    lineaApellido = lineaPartida[2]
    return (lineaCedula, lineaNombre, lineaApellido)

try:
    with open("infoPersonas.txt", "r") as archivo:
        for linea in archivo:
            if linea !="":
                lineaLimpia = limpiador(linea)
                diccionario[lineaLimpia[0]] = [lineaLimpia[1],lineaLimpia[2]]
except FileNotFoundError:
    with open("infoPersonas.txt","w") as archivo:
        pass

while True:
    seccion = input("\n Presione la tecla: \n[A] si quiere agregar contacto \n[B] si quiere eliminar contactos \n[C] si quiere modificar contactos \n[D] si quiere ver la lista de personas \n[E] si quiere salir\n")

    if seccion == "e" or seccion == "E":
        with open("infoPersonas.txt","w") as archivo:
            for cedulas in diccionario:
                archivo.write(f"{cedulas},{diccionario[cedulas][0]},{diccionario[cedulas][1]}\n")
        print("¡Adios!")
        break

    elif seccion == "a" or seccion == "A":
        cedula = input("Ingrese número de cédula: \n")
        nombre = input("Ingrese nombre: \n")
        apellido = input("Ingrese apellido: \n")
        diccionario[cedula] = [nombre, apellido]

    elif seccion == "b" or seccion == "B":
        cedula = input("Ingrese la CÉDULA de la persona a Eliminar \n")
        try:
            del diccionario[cedula]
        except KeyError:
            print("Ese número cédula no existe. Intente de nuevo \n")

    elif seccion == "c" or seccion == "C":
        cedula = input("Ingrese la CÉDULA de la persona a modificar \n")
        if cedula not in diccionario:
            print("Ese número de cédula no existe. Intente de nuevo \n")
        diccionario[cedula][0] = input("Inserte Nombre nuevo \n")
        diccionario[cedula][1] = input ("Inserte Apellido nuevo \n")
        print("\nEl contacto ha sido modificado como: \n" + f"Cedula: {cedula} Nombre: {diccionario[cedula][0]} Apellido: {diccionario[cedula][1]} \n")

    elif seccion == "d" or seccion == "D":
        for cedulas in diccionario:
            print(f"\nCedula: {cedulas} - Nombre: {diccionario[cedulas][0]} - Apellido: {diccionario[cedulas][1]} \n")

    else:
        continue