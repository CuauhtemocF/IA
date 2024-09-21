# Encontrar la posicion de la casilla vacia (0)
def encontrar_cero(tablero):
    for i in range(2):
        for j in range(2):
            if tablero[i][j] == 0:
                return i, j

# Verificacion
def es_meta(tablero, meta):
    return tablero == meta

# Generador de movimientos
def generar_movimientos(tablero):
    x, y = encontrar_cero(tablero)
    movimientos = []
    direcciones = {'arriba': (-1, 0), 'abajo': (1, 0), 'izquierda': (0, -1), 'derecha': (0, 1)}
    
    for direccion, (dx, dy) in direcciones.items():
        nuevo_x, nuevo_y = x + dx, y + dy
        if 0 <= nuevo_x < 2 and 0 <= nuevo_y < 2:
            nuevo_tablero = [fila[:] for fila in tablero]  # Copia del tablero
            nuevo_tablero[x][y], nuevo_tablero[nuevo_x][nuevo_y] = nuevo_tablero[nuevo_x][nuevo_y], nuevo_tablero[x][y]
            movimientos.append((nuevo_tablero, direccion))
    
    return movimientos

# Inicio
def dfs_4_puzzle(inicio, meta):
    pila = [(inicio, [])]  # La pila, tuplas (tablero_actual, camino)
    visitados = set()

    while pila:
        tablero_actual, camino = pila.pop()

        # Convertir tablero actual en tupla inmutable para el conjunto de visitados
        tablero_tupla = tuple(tuple(fila) for fila in tablero_actual)

        if tablero_tupla in visitados:
            continue

        visitados.add(tablero_tupla)

        # Verificar si el tablero actual es la meta que pusimos
        if es_meta(tablero_actual, meta):
            return camino

        # Generar movimientos y seguir con DFS
        for nuevo_tablero, movimiento in generar_movimientos(tablero_actual):
            pila.append((nuevo_tablero, camino + [movimiento]))

    return None  # No se encontro solución

# Tablero inicial (posiciones)
tablero_inicial = [[2, 3], [0, 1]]

# Tablero final
tablero_meta = [[1, 2], [3, 0]]

# Resolver puzzle
solucion = dfs_4_puzzle(tablero_inicial, tablero_meta)

if solucion:
    print(f"Solucion encontrada: {solucion}")
else:
    print("Error")