"""
test 9:
Objetivo
 Su objetivo es realizar el algoritmo de un elevador de personas en un edificio de 29 pisos. Este
 debe ser eficiente en cuanto a reducción de tiempo innecesario de desplazamiento respetando
 su dirección de desplazamiento actual (subiendo o bajando).

 Diseñe un simple método que imprima en consola las iteraciones del elevador a medida que
 este se encuentra en funcionamiento, este debe recibir como parámetros: un arreglo de pisos
 a los cuales el elevador será llamado en un orden definido, un piso inicial de ejecución y un
 mapa de pisos ingresados.

 El método debe imprimir el piso actual del elevador, la dirección en la que se desplaza, el
 piso en el que se detiene y el piso ingresado cada vez que alguno de estos cambie

 Prueba realizada por: Santiago Agudelo
"""
#arreglo de pisos
floors= [5, 29, 13, 10]
#piso inicial de ejecución
start_floor= 4

floors_to_enter= {5:2, 29: 10, 13: 1, 10:1}

def elevador_ruta(floors, start_floor):    

    #ordenar el arreglo de pisos
    sorted_floors = sorted(floors)

    #obtener el indice del piso de inicio
    if start_floor in sorted_floors:
        start_index = sorted_floors.index(start_floor)
    else:
        start_index = 0

    #pisos que se van a subir
    up_floor = sorted_floors[start_index:]

    #pisos que se van a bajar
    down_floor = sorted_floors[:start_index]

    #ruta completa
    route = up_floor + down_floor

    #Mueve el elevador hasta llegar al piso deseado
    current_floor = start_floor
    direccion = "Subiendo"
    step = 0
    print(f"{step} elevador en piso: ", current_floor)
    for floor in route:
        while current_floor != floor:
            step += 1
            print(f"{step} elevador", direccion)
            #De acuerdo a la direccion en la que este yendo el alevador aumenta o resta uno al piso actual
            if direccion == "Subiendo":
                current_floor += 1
            else:
                current_floor -= 1
            step += 1
            print(f"{step} elevador en piso: {current_floor}" )
        step += 1
        print(f"{step} elevador se detiene")
        #si el piso actual esta en la lista imprime el piso y lo elimina de la lista
        if floor in floors_to_enter:
            step += 1
            print(f"{step} piso ingresado: ", floors_to_enter[floor])
            del floors_to_enter[floor]

elevador_ruta(floors, start_floor)

"""
El proyecto esta sin bonus solo el problema principal
use como ejemplo una practica que estaba haciendo sobre el uso de dos elevadores
me surgui un problema de que no estaba guardando las paradas que se agregaban en la lista 
"""