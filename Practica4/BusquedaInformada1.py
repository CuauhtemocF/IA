import heapq
import time
#Definicion heuristica Distancia de Manhattan
def heuristica_manhattan(nodo_actual, nodo_objetivo):
    return abs(nodo_actual[0] - nodo_objetivo[0]) + abs(nodo_actual[1] - nodo_objetivo[1])

#Explorar cuatro direcciones NESW
def obtener_vecinos(laberinto, nodo):
    vecinos = []
    filas, columnas = len(laberinto), len(laberinto[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  #arriba, abajo, izquierda, derecha
    
    for mov_fila, mov_columna in movimientos:
        nueva_fila, nueva_columna = nodo[0] + mov_fila, nodo[1] + mov_columna
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and laberinto[nueva_fila][nueva_columna] == 0:
            vecinos.append((nueva_fila, nueva_columna))
    
    return vecinos

#Funcion para reconstruir el camino desde el nodo inicial al nodo objetivo
def reconstruir_camino(padre, nodo_actual):
    camino = []
    while nodo_actual:
        camino.append(nodo_actual)
        nodo_actual = padre[nodo_actual]
    return camino[::-1]  #Devuelve el camino en el orden correcto

#Algoritmo A*
def a_estrella(laberinto, inicio, objetivo):
    #Inicializar la cola de prioridad
    prioridad = []
    heapq.heappush(prioridad, (0, inicio))
    
    #Estructuras para almacenar el costo de llegar a cada nodo y el nodo padre
    costo_acumulado = {inicio: 0}
    padre = {inicio: None}
    
    while prioridad:
        _, nodo_actual = heapq.heappop(prioridad)
        
        #Si llegamos, reconstruimos y devolver camino
        if nodo_actual == objetivo:
            return reconstruir_camino(padre, nodo_actual)
        
        #Obtener direcciones validas
        for vecino in obtener_vecinos(laberinto, nodo_actual):
            nuevo_costo = costo_acumulado[nodo_actual] + 1  #Costo
            if vecino not in costo_acumulado or nuevo_costo < costo_acumulado[vecino]:
                costo_acumulado[vecino] = nuevo_costo
                prioridad_heuristica = nuevo_costo + heuristica_manhattan(vecino, objetivo)
                heapq.heappush(prioridad, (prioridad_heuristica, vecino))
                padre[vecino] = nodo_actual
    
    return None 

#Laberinto 2D
laberinto = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

#Punto de inicio y salida
inicio = (0, 1) 
objetivo = (3, 4) 

#Empezar el temporizador
start_time = time.time()

#Resolver el laberinto (A*)
camino = a_estrella(laberinto, inicio, objetivo)

#Fin del temporizador
end_time = time.time()

#Impresion
if camino:
    print("Se ha encontrado un camino:")
    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {end_time - start_time:.9f} segundos")
    for paso in camino:
        print(paso)
else:
    print("No se ha encontrado un camino.")

