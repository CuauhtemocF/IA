import math
#Constantes
VACIO = 0
HUMANO = 1
IA = -1
INFINITO = float('inf')
TAMANIO = 4

#Inicialisar el tablero
def crear_tablero():
    return [[VACIO for _ in range(TAMANIO)] for _ in range(TAMANIO)]

#Imprimir tablero
def imprimir_tablero(tablero):
    simbolos = {VACIO: ".", HUMANO: "X", IA: "O"}
    for fila in tablero:
        print(" ".join([simbolos[celda] for celda in fila]))
    print()

#Comprobar si hay un ganador
def comprobar_ganador(tablero):
    #Comprobar filas, columnas y diagonales
    for i in range(TAMANIO):
        #Fila
        if abs(sum(tablero[i])) == TAMANIO:
            return tablero[i][0]
        #Columna
        if abs(sum([tablero[j][i] for j in range(TAMANIO)])) == TAMANIO:
            return tablero[0][i]
    
    #Diagonales
    if abs(sum([tablero[i][i] for i in range(TAMANIO)])) == TAMANIO:
        return tablero[0][0]
    if abs(sum([tablero[i][TAMANIO-i-1] for i in range(TAMANIO)])) == TAMANIO:
        return tablero[0][TAMANIO-1]
    
    return None

#Comprobar si el tablero esta lleno
def tablero_lleno(tablero):
    for fila in tablero:
        if VACIO in fila:
            return False
    return True

#Funcion de evaluacion heuristica
def evaluar(tablero):
    ganador = comprobar_ganador(tablero)
    if ganador == HUMANO:
        return -100
    elif ganador == IA:
        return 100
    else:
        return 0

#Minimax con pod alfa beta
def minimax(tablero, profundidad, es_maximizador, alfa, beta):
    puntaje = evaluar(tablero)
    if abs(puntaje) == 100 or profundidad == 0 or tablero_lleno(tablero):
        return puntaje
    
    if es_maximizador:
        mejor_valor = -INFINITO
        for i in range(TAMANIO):
            for j in range(TAMANIO):
                if tablero[i][j] == VACIO:
                    tablero[i][j] = IA
                    valor = minimax(tablero, profundidad - 1, False, alfa, beta)
                    tablero[i][j] = VACIO
                    mejor_valor = max(mejor_valor, valor)
                    alfa = max(alfa, mejor_valor)
                    if beta <= alfa:
                        break
        return mejor_valor
    else:
        mejor_valor = INFINITO
        for i in range(TAMANIO):
            for j in range(TAMANIO):
                if tablero[i][j] == VACIO:
                    tablero[i][j] = HUMANO
                    valor = minimax(tablero, profundidad - 1, True, alfa, beta)
                    tablero[i][j] = VACIO
                    mejor_valor = min(mejor_valor, valor)
                    beta = min(beta, mejor_valor)
                    if beta <= alfa:
                        break
        return mejor_valor

#Funcion de IA que toma decisiones basadas en Minimax
def mejor_movimiento(tablero):
    mejor_valor = -INFINITO
    mejor_jugada = (-1, -1)
    for i in range(TAMANIO):
        for j in range(TAMANIO):
            if tablero[i][j] == VACIO:
                tablero[i][j] = IA
                valor = minimax(tablero, 5, False, -INFINITO, INFINITO)
                tablero[i][j] = VACIO
                if valor > mejor_valor:
                    mejor_valor = valor
                    mejor_jugada = (i, j)
    return mejor_jugada

#Modo Humano vs Humano
def humano_vs_humano():
    tablero = crear_tablero()
    jugador_actual = HUMANO
    while True:
        imprimir_tablero(tablero)
        if jugador_actual == HUMANO:
            print("Turno del Humano (X)")
        else:
            print("Turno del Humano 2 (O)")
        
        fila = int(input("Ingresa la fila (0-3): "))
        columna = int(input("Ingresa la columna (0-3): "))
        if tablero[fila][columna] == VACIO:
            tablero[fila][columna] = jugador_actual
            ganador = comprobar_ganador(tablero)
            if ganador or tablero_lleno(tablero):
                imprimir_tablero(tablero)
                if ganador == HUMANO:
                    print("Humano 1 (X) a ganado!")
                elif ganador == IA:
                    print("Humano 2 (O) a ganado!")
                else:
                    print("¡Empate!")
                break
            jugador_actual *= -1
        else:
            print("Movimiento invalido!!!! Prueba otro")

#Modo de juego Humano vs IA
def humano_vs_ia():
    tablero = crear_tablero()
    while True:
        imprimir_tablero(tablero)
        print("Turno del Humano (X)")
        fila = int(input("Ingresa la fila (0-3): "))
        columna = int(input("Ingresa la columna (0-3): "))
        if tablero[fila][columna] == VACIO:
            tablero[fila][columna] = HUMANO
            if comprobar_ganador(tablero):
                imprimir_tablero(tablero)
                print("El Humano a ganado!!!!")
                break
            if tablero_lleno(tablero):
                imprimir_tablero(tablero)
                print("Empate!")
                break
            #Turno de la IA
            fila_ia, columna_ia = mejor_movimiento(tablero)
            tablero[fila_ia][columna_ia] = IA
            if comprobar_ganador(tablero):
                imprimir_tablero(tablero)
                print("La IA a ganado!")
                break
            if tablero_lleno(tablero):
                imprimir_tablero(tablero)
                print("Empate!")
                break
        else:
            print("Movimiento invalido!!!! Prueba otro")

#Modo IA vs IA
def ia_vs_ia():
    tablero = crear_tablero()
    turno = HUMANO
    while True:
        imprimir_tablero(tablero)
        if turno == HUMANO:
            print("Turno de la IA 1 (X)")
        else:
            print("Turno de la IA 2 (O)")
        fila_ia, columna_ia = mejor_movimiento(tablero)
        tablero[fila_ia][columna_ia] = turno
        if comprobar_ganador(tablero):
            imprimir_tablero(tablero)
            if turno == HUMANO:
                print("La IA 1 a ganado!!!!")
            else:
                print("La IA 2 a ganado!!!!")
            break
        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("Empate!")
            break
        turno *= -1

#Menu
def menu():
    print("Bienvenido al Juego del Gato 4x4")
    print("1. Humano vs Humano")
    print("2. Humano vs IA")
    print("3. IA vs IA")
    opcion = int(input("Selecciona una opcion (1-3): "))
    if opcion == 1:
        humano_vs_humano()
    elif opcion == 2:
        humano_vs_ia()
    elif opcion == 3:
        ia_vs_ia()
    else:
        print("Movimiento invalido!!!! Prueba otro")

if __name__ == "__main__":
    menu()
