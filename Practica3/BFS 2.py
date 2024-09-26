from collections import deque

#Imprimir el laberinto con el camino marcado
def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print(" ".join(str(celda) for celda in fila))

#Verificar posición válida
def es_posicion_valida(laberinto, x, y, visitado):
    return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] == 0 and not visitado[x][y]

#BFS
def resolver_laberinto_bfs(laberinto, inicio, meta):
    x_inicio, y_inicio = inicio
    x_meta, y_meta = meta

    #Crear una matriz para marcar las celdas visitadas
    visitado = [[False for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]

    #Definir las direcciones de movimiento: arriba, abajo, izquierda, derecha
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    #Cola para que BFS guarde las posiciones y el camino tomado
    cola = deque([(x_inicio, y_inicio, [])])

    #Marcar la celda de inicio
    visitado[x_inicio][y_inicio] = True

    while cola:
        x_actual, y_actual, camino_actual = cola.popleft()

        #Si hemos llegado a la salida, devolver el camino
        if (x_actual, y_actual) == (x_meta, y_meta):
            return camino_actual + [(x_actual, y_actual)]

        #Explorar las cuatro direcciones NESW
        for dx, dy in movimientos:
            nuevo_x, nuevo_y = x_actual + dx, y_actual + dy
            if es_posicion_valida(laberinto, nuevo_x, nuevo_y, visitado):
                visitado[nuevo_x][nuevo_y] = True
                cola.append((nuevo_x, nuevo_y, camino_actual + [(x_actual, y_actual)]))

    return None  

#Laberinto  2D
laberinto = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

#Punto de inicio y salida
inicio = (0, 1)  
meta = (3, 4)  

#Resolver el laberinto utilizando BFS
solucion = resolver_laberinto_bfs(laberinto, inicio, meta)

#Impresion
if solucion:
    print("Camino encontrado:")
    for paso in solucion:
        print(paso)
    #Array del laberinto resuelto
    for x, y in solucion:
        laberinto[x][y] = '_'  #Marca el camino
    imprimir_laberinto(laberinto)
else:
    print("No se encontró solución.")
