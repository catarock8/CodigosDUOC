#ejemplo Menu
#Puede copiar esto si estima conveniente
#Hay que usar el repositorio Prueba3Autos

from autoHerramientas import *

#Con esto puede llamar a cualquier funcion creada en prueba.py
from prueba import *

#lista de autos
lista_autos = obtenerAutos("Autos2")

opciones_menu = [
    "Opcion 1",
    "Opcion 2",
    "Opcion 3",
    "Opcion 4",
    "Opcion 5",
    "Opcion 6",
    "Opcion 7",
#agregar más opciones de forma similar
]
opciones_menu.append("Salir")

nombre_usuario=input("Ingrese nombre de usuario: ")
fecha_actual=input("Ingrese la fecha de hoy: ")
color_favorito=input("Ingrese color favorito: ")

def opcion1():
    marca=input("Ingrese la marca del vehiculo: ")
    modelo= input("Ingrese el modelo del auto: ")
    for i in range(len(lista_autos)):
        x=lista_autos[i]
        x=x["marca"]
        y=lista_autos[i]
        y=y["modelo"]
        if marca==x and modelo==y:
            print(lista_autos[i])
    return



def opcion4():
    patente=input("Ingrese la patente: ")
    for i in range(len(lista_autos)):
        x=lista_autos[i]
        x=x["patente"]
        if patente==x:
            print(lista_autos[i])
    return



def opcion3():
    modelo= input("Ingrese el modelo del auto: ")
    marca=input("Ingrese la marca del vehiculo: ")
    for i in range(len(lista_autos)):
        x=lista_autos[i]
        x=x["marca"]
        y=lista_autos[i]
        y=y["modelo"]
        z=lista_autos[i]
        z=z["patente"]
        c=lista_autos[i]
        c=c["color"]
        if marca==x and modelo==y:
            print(lista_autos[i])
            print(nombre_usuario,"emite certificado que:")
            print(" ")
            print("El vehiculo",x," ",y,"con patente",z,"de color",c)
            print("Queda registrado oficialmente a la fecha:",fecha_actual)
        
    
    return

def opcion2():
    llave = input("Ingresa la llave para filtrar los vehículos: ")
    parametro = input("Ingresa el parámetro para filtrar los vehículos: ")

    for i in lista_autos:
        if llave in i and i[llave] == parametro:
            print(i)
    return


def opcion5():
    rango1=int(input("Ingrese el primer rango de años: "))
    rango2=int(input("Ingrese el segundo rango de años: "))
    for i in range(len(lista_autos)):
        aux=lista_autos[i]
        aux=aux["año"]
        if aux>=rango1 and aux<=rango2:
            print(lista_autos[i])
    return


def opcion6():
    patente=input("Ingrese su patente: ")
    nuevo_propietario=input("Ingrese su nombre: ")
    propietario="Propietario"
    for i in range(len(lista_autos)):
        aux=lista_autos[i]
        aux=aux["patente"]
        if aux==patente:
            aux2=lista_autos[i]
            aux2[propietario]=nuevo_propietario
            print(lista_autos[i])
    return


def opcion7():
    color=color_favorito.capitalize()
    print("Su color favorito es el: ",color)
    print("Aqui le mostramos todos los autos con este color")
    for i in range(len(lista_autos)):
        x=lista_autos[i]
        x=x["color"]
        if color==x:
            print(lista_autos[i])
    return



while (True):
    #Mostrar Menu
    for i, opcion in enumerate(opciones_menu):
        print(i+1,". ",opcion, sep="")

    #Seleccionar
    while (True):
        seleccion = input(">> ")
        if (validar_seleccion(seleccion,opciones_menu)):
            seleccion = int(seleccion)-1
            break
    
    #MOSTRAR OPCION --------------------
    print(opciones_menu[seleccion])

    #HACER ACCIONES ---------------------
    if (seleccion == 0):
        #opcion 1
        opcion1()
        pass

    if (seleccion == 1):
        #opcion 2
        opcion2()
        pass

    if (seleccion == 2):
        #opcion 3
        opcion3()
        pass

    if (seleccion == 3):
        #opcion 4
        opcion4()
        pass

    if (seleccion == 4):
        #opcion 5
        opcion5()
        pass

    if (seleccion == 5):
        #opcion 6
        opcion6()
        pass

    if (seleccion == 6):
        #opcion 7
        opcion7()
        pass



    if (seleccion == len(opciones_menu)-1):
        #SALIR
        print("chao csm")
        break
        pass
