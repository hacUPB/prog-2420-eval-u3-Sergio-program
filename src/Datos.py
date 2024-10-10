import datetime
def crea_entreno_natación():
    entreno_natación = { "Deportista": "________", "Fecha de entreno": datetime.now, "Distancia total recorrida (km)": 0, 
                        "Prueba nadada": "________", "Mejor tiempo (s)": 0, "Sensaciones generales": "________"}

def crea_entreno_ciclismo():
    entreno_ciclismo = {"Deportista": "________", "Fecha de entreno": datetime.now, "Distancia total recorrida (km)": 0, 
                        "Mejor tiempo (h)": 0, "Sensaciones generales": "________"}

def crea_entreno_runner():
    entreno_carrera = {"Deportista": "________", "Fecha de entreno": datetime.now, "Distancia total recorrida (km)": 0, 
                        "Prueba corrida (km)": 0, "Mejor tiempo (s)": 0, "Sensaciones generales": "________"}

def menu_principal():
    print("1: Registrar nuevo entreno\n2: Explorar entrenos\n3: Salir")
    opción = int(input("Que desea hacer: "))
    return opción

def menu_deportes():
    print("1: Natación\n2: Ciclismo\n3: Carrera\n4: Volver")
    deporte = int(input("Selecciona la disciplina que entrenaste: "))
    return deporte

def main():
    #Tu código va aquí. Mantén la indentación
    while True:
        opción = menu_principal()
        if opción == 1:
            deporte = menu_deportes()
            if deporte == 1:
                crea_entreno_natación()
            if deporte == 2:
                crea_entreno_ciclismo()
            if deporte == 3:
                crea_entreno_runner()
            if deporte == 4:
                break
            else:
                print("Opción no válida")
        if opción == 2:
            pass

if __name__ == "__main__":
    main()
