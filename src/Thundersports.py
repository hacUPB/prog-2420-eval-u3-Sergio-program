#Importe de funciones ya existentes que nos ayudarán a la estética y funcionalidad de nuestro código.
import datetime
from os import system

#Listas que se van a llenar con los entrenos de la respectiva disciplina.
lista_entrenos_natación = []
lista_entrenos_ciclismo = []
lista_entrenos_runner = []
lista_deportistas = []

#Esta función crea un diccionario con las claves predeterminadas de un deportista.
def crear_deportista():
    deportista = {
        "Deportista": input("Nombre del desportista: "),
        "Peso": int(input("Ingrese el peso del deportista (Kg): ")),
        "Altura": int(input("Ingrese la estatura del deportista (cm): ")),           
        "Disciplina_principal": input("Ingrese la discilina principal del deportista: "),
        "Entrenos_semana": int(input("Número de entrenos a la semana: ")),
        "Prueba_objetivo": input("¿Qué prueba desea preparar?: ")
    }
    return  deportista

#Esta función crea un diccionario con las claves predeterminadas para la natación y los datos los llena el usuario.
def crea_entreno_natación():
    entreno_natación = { 
        "Deportista": input("Nombre del deportista: "),
        "Fecha de entreno": datetime.date.today(), 
        "Distancia total recorrida (km)": float(input("Distancia total recorrida (km): ")), 
        "Prueba nadada": input("Prueba nadada: "),
        "Mejor tiempo (s)": float(input("Mejor tiempo (s): ")), 
        "Sensaciones generales": input("Sensaciones generales: ")
    }
    return entreno_natación

#Esta función creea un diccionario con las claves predeterminadas para el ciclismo y los datos los llena el usuario.
def crea_entreno_ciclismo():
    entreno_ciclismo = {
        "Deportista": input("Nombre del deportista: "),
        "Fecha de entreno": datetime.date.today(), 
        "Distancia total recorrida (km)": float(input("Distancia total recorrida (km): ")), 
        "Mejor tiempo (h)": float(input("Mejor tiempo (h): ")), 
        "Sensaciones generales": input("Sensaciones generales: ")
    }
    return entreno_ciclismo

#Esta función creea un diccionario con las claves predeterminadas para la carrera y los datos los llena el usuario.
def crea_entreno_runner():
    entreno_carrera = { 
        "Deportista": input("Nombre del deportista: "),
        "Fecha de entreno": datetime.date.today(), 
        "Distancia total recorrida (km)": float(input("Distancia total recorrida (km): ")), 
        "Prueba corrida (km)": float(input("Prueba corrida (km): ")), 
        "Mejor tiempo (min)": float(input("Mejor tiempo (min): ")), 
        "Sensaciones generales": input("Sensaciones generales: ")
    }
    return entreno_carrera

#Esta función alberga el menú principal del programa, que permite elegir entre explorar o crear entrenos y salir.
def menu_principal():
    print("1: Registrar nuevo entreno\n2: Explorar\n3: Registar deportistas\n4: Salir")
    opción = int(input("¿Qué desea hacer?: "))
    return opción

#Esta función alberga el menú para crear un entreno nuevo, dejando elegir la disciplina.
def menu_deportes():
    print("1: Natación\n2: Ciclismo\n3: Carrera\n4: Volver")
    deporte = int(input("Selecciona la disciplina que entrenaste: "))
    return deporte

#Esta fuhnción alberga el menú para explorar entrenos ya existentes, dejando elegir la disciplina.
def menu_explorar():
    print("1: Explorar entrenos de natación\n2: Explorar entrenos de ciclismo\n3: Explorar entrenos de carrera\n4: Explorar deportistas\n5: Volver")
    explora = int(input("Seleccione la disciplina a explorar: "))
    return explora

#Esta función cambia el nombre del diccionario según su posición en la lista, para facilitar el reconocimiento.
def cambia_nombre_crea_lista(lista, diccionario, nombre):
    posicion = len(lista)
    nuevo_nombre = f"{nombre}_{posicion}"
    lista.append((nuevo_nombre, diccionario))
    return nuevo_nombre, diccionario

#Esta función imprime todos los entrenos que se han registrado por la disciplina seleccionada.
def explorar_entrenos(lista_entrenos):
    if len(lista_entrenos) == 0:
        print("No hay entrenos registrados para esta disciplina.")
    else:
        for nombre_entreno, entreno in lista_entrenos:
            print(f"Entreno: {nombre_entreno}")
            for clave, valor in entreno.items():
                print(f"  {clave}: {valor}")
            print()

def mayor_distancia(lista_entrenos):
    lista = []
    for nombre_entrenos, entreno in lista_entrenos:
        lista.append(entreno["Distancia total recorrida (km)"])
    mayor = max(lista)
    return mayor
    
#Código principal del programa, que fusiona las funciones creadas previamente.          
def main():
    #Bucle while que mantiene al menú principal corriéndose indefinidamente.
    
    while True:
        opción = menu_principal()
        
        #Creación de entrenos y listas.
        if opción == 1:
            system ('cls')
            deporte = menu_deportes()
            if deporte == 1:
                system ('cls')
                entreno_natación = crea_entreno_natación()
                cambia_nombre_crea_lista(lista_entrenos_natación, entreno_natación, "entreno_natación")
            elif deporte == 2:
                system ('cls')
                entreno_ciclismo = crea_entreno_ciclismo()
                cambia_nombre_crea_lista(lista_entrenos_ciclismo, entreno_ciclismo, "entreno_ciclismo")
            elif deporte == 3:
                system ('cls')
                entreno_runner = crea_entreno_runner()
                cambia_nombre_crea_lista(lista_entrenos_runner, entreno_runner, "entreno_runner")
            elif deporte == 4:
                break
            else:
                print("Opción no válida")
        
        #Exploración de entrenos y listas.
        elif opción == 2:
            system ('cls')
            explora = menu_explorar()
            if explora == 1:
                system ('cls')
                explorar_entrenos(lista_entrenos_natación)
                m = mayor_distancia(lista_entrenos_natación)
                print(m)
            elif explora == 2:
                system ('cls')
                explorar_entrenos(lista_entrenos_ciclismo)
            elif explora == 3:
                system ('cls')
                explorar_entrenos(lista_entrenos_runner)
            elif explora == 4:
                system('cls')
                explorar_entrenos(lista_deportistas)
            elif explora == 5:
                break
            else:
                print("Opción no válida")
        
        elif opción == 3:
            deportista = crear_deportista()
            cambia_nombre_crea_lista(lista_deportistas, deportista, "Deportista")

        #Cierre del bucle while
        elif opción == 4:
            system ('cls')
            print("Cerrando programa")
            break
        else:
            print("Opción no válida")
            
if __name__ == "__main__":
    main()