import random

def crear_tablero():
    return [[' ' for _ in range(4)] for _ in range(4)]

def mostrar_tablero(tablero):
    print("  0 1 2 3")
    for idx, fila in enumerate(tablero):
        print(f"{idx} {'|'.join(fila)}")
        if idx < 3:
            print("  -+-+-+-")

def hay_ganador(tablero, marca):
    # Comprobar filas y columnas
    for i in range(4):
        if all([tablero[i][j] == marca for j in range(4)]):
            return True
        if all([tablero[j][i] == marca for j in range(4)]):
            return True
    # Comprobar diagonales
    if all([tablero[i][i] == marca for i in range(4)]):
        return True
    if all([tablero[i][3 - i] == marca for i in range(4)]):
        return True
    return False

def tablero_lleno(tablero):
    return all([tablero[i][j] != ' ' for i in range(4) for j in range(4)])

def movimiento_jugador(tablero):
    while True:
        try:
            fila = int(input("Ingrese la fila (0-3): "))
            columna = int(input("Ingrese la columna (0-3): "))
            if fila in range(4) and columna in range(4):
                if tablero[fila][columna] == ' ':
                    tablero[fila][columna] = 'X'
                    break
                else:
                    print("La posición ya está ocupada. Intente de nuevo.")
            else:
                print("Entrada inválida. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números enteros.")

def movimiento_computadora(tablero):
    posiciones_libres = [(i, j) for i in range(4) for j in range(4) if tablero[i][j] == ' ']
    if posiciones_libres:
        fila, columna = random.choice(posiciones_libres)
        tablero[fila][columna] = 'O'
        print(f"La computadora ha colocado una 'O' en la posición ({fila}, {columna}).")

def juego():
    tablero = crear_tablero()
    mostrar_tablero(tablero)
    turno_jugador = True

    while True:
        if turno_jugador:
            movimiento_jugador(tablero)
            mostrar_tablero(tablero)
            if hay_ganador(tablero, 'X'):
                print("¡Felicidades! ¡Has ganado!")
                break
        else:
            movimiento_computadora(tablero)
            mostrar_tablero(tablero)
            if hay_ganador(tablero, 'O'):
                print("La computadora ha ganado. ¡Mejor suerte la próxima vez!")
                break
        if tablero_lleno(tablero):
            print("El juego ha terminado en empate.")
            break
        turno_jugador = not turno_jugador

if __name__ == "__main__":
    juego()