from collections import deque

# Función para convertir una lista bidimensional en una tupla unidimensional
def convertir_a_tupla(tablero):
    return tuple([item for fila in tablero for item in fila])

# Función para encontrar la posición del 0 en el tablero
def encontrar_posicion_cero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 0:
                return i, j

#Función para generar nuevos estados del tablero tras un movimiento válido
def generar_nuevos_estados(tablero, pos_cero):
    fila, columna = pos_cero
    nuevos_estados = []
    
    #Movimientos posibles: arriba, abajo, izquierda, derecha
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for mov_fila, mov_col in movimientos:
        nueva_fila, nueva_columna = fila + mov_fila, columna + mov_col
        
        #Verificar si el nuevo movimiento está dentro de los límites del tablero
        if 0 <= nueva_fila < len(tablero) and 0 <= nueva_columna < len(tablero[0]):
            nuevo_tablero = [list(fila) for fila in tablero]  # Copiar el tablero actual
            #Intercambiar el cero con la nueva posición
            nuevo_tablero[fila][columna], nuevo_tablero[nueva_fila][nueva_columna] = (
                nuevo_tablero[nueva_fila][nueva_columna], nuevo_tablero[fila][columna]
            )
            nuevos_estados.append(nuevo_tablero)
    
    return nuevos_estados

#Función BFS para resolver el 4-Puzzle
def resolver_4_puzzle(estado_inicial, estado_objetivo):
    # Convertir los estados inicial y objetivo a tuplas para que puedan ser almacenados en sets
    estado_inicial = convertir_a_tupla(estado_inicial)
    estado_objetivo = convertir_a_tupla(estado_objetivo)

    #Cola para BFS: cada elemento es (estado_actual, lista_de_movimientos_realizados)
    cola = deque([(estado_inicial, [])])

    #Conjunto de estados visitados
    visitado = set()
    visitado.add(estado_inicial)


    while cola:
        estado_actual, camino = cola.popleft()

        #Si llegamos al estado objetivo, devolvemos el camino
        if estado_actual == estado_objetivo:
            return camino + [estado_actual]

        #Convertir el estado actual a una lista bidimensional para facilitar la manipulación
        tablero_actual = [list(estado_actual[i:i + 2]) for i in range(0, len(estado_actual), 2)]

        #Encontrar la posición del 0
        pos_cero = encontrar_posicion_cero(tablero_actual)

        #Generar los posibles nuevos estados desde el estado actual
        nuevos_estados = generar_nuevos_estados(tablero_actual, pos_cero)

        for nuevo_estado in nuevos_estados:
            nuevo_estado_tupla = convertir_a_tupla(nuevo_estado)

            #Si el nuevo estado no ha sido visitado aun, lo metemos a la cola
            if nuevo_estado_tupla not in visitado:
                visitado.add(nuevo_estado_tupla)
                cola.append((nuevo_estado_tupla, camino + [estado_actual]))

    #Si no encontramos solucion
    return None

#Estado inicial
estado_inicial = [
    [1, 0],
    [3, 2]
]

#Estado objetivo
estado_objetivo = [
    [1, 2],
    [3, 0]
]

#BFS
solucion = resolver_4_puzzle(estado_inicial, estado_objetivo)

#Imprimir la solucion si se encontro
if solucion:
    print("Se encontro una solucion en", len(solucion) - 1, "movimientos:")
    for paso in solucion:
        for i in range(0, len(paso), 2):
            print(paso[i:i+2])
        print("--------")
else:
    print("No hay solucion.")
