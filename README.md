[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MuElT52l)
# Unidad 3
---
## Documentación del proyecto
Nombre:  Sergio González Losada
ID:  000548401
---
# Título: Thundersports

#### Descripción:
La actividad física es beneficiosa para todos. Hacer deporte es crucial, pero tanto como hacerlo, es llevar registro del progreso, los objetivos establecidos, y el avance que se tiene en ellos, "Lo que se mide se mejora". Para algunas personas, llevar un historial de sus entrenos y progreso físico es complicado, creen que es suficiente con memorizarlo, lo llevan en hojas o material físico que tiende a perderse, ó en el caso de usar herramientas digitales, son muy complejas para continuar usándolas a largo plazo.
Con este programa se busca crear una herramienta fácil e intuitiva, que ayude a llevar control de los entrenos y del progreso que se va realizando en distintos deportes.

#### Alcance:
El programa debe ayudar al usuario a llevar control de sus entrenos y prácticas deportivas. Inicialmente llevando un registro general de la persona, con su peso, talla, tiempos correspondientes a ciertas pruebas, cantidad de entrenos que tendrá a la semana y metas. Posteriormente, dejará llevar registro de cada uno de esos entrenos, con la distancia total recorrida, el tipo de prueba en el que se hizo, los tiempos por cierta distancia y la duración de los entrenos (Datos añadidos por el usuario), el programa recopilará estos datos y los mostrará.
Con la idea inicial del programa, se apunta a ayudar a deportistas en alguna disciplina de triatlón, bien sea natación, ciclismo, carrera (running), o en las tres.

#### Estructuras de datos:
Par el desarrollo de programas se emplearán principalmente listas y diccionarios, que serán acompañadas de funciones y métodos para cumplir todas las tareas del programa. De ser necesario, se emplearán otros métodos de control de datos, aunque en menor medida.

#### Pseudocódigo:

```
Inicio
    mientras true
        imprimir("1: Nuevo entreno\n2: Explorar entrenos")
        opción = input(int("Seleccione una opción"))
            if opción == 1:
                funcion para añadir un entreno
            elif
                while true
                    imprimir("1: Mayor distancia recorrida\n2: Menor tiempo por prueba")
                    if opción == 1:
                        mostrar biblioteca del entreno con mayor distancia total
                    if opción == 2:
                        while true:
                            imprimir("Ingrese la prueba para ver su menor tiempo")
                            mostrar el menor tiempo de la prueba elegida
        else: imprimir("Opción no válida") 
```