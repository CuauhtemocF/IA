import math
import random

#Himmelblau
def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

#Funcion para generar un nuevo punto aleatorio cercano
def generar_vecino(x, y, limite):
    delta_x = random.uniform(-0.5, 0.5)
    delta_y = random.uniform(-0.5, 0.5)
    
    #Nuevo punto, manteniendo dentro del limite [-5, 5]
    nuevo_x = max(min(x + delta_x, limite), -limite)
    nuevo_y = max(min(y + delta_y, limite), -limite)
    
    return nuevo_x, nuevo_y

#Funcion de probabilidad para aceptar un peor estado
def probabilidad_aceptacion(delta, temperatura):
    if delta < 0:
        return 1.0
    else:
        return math.exp(-delta / temperatura)

#Algoritmo de recocido simulado
def recocido_simulado(x_inicial, y_inicial, temperatura_inicial, enfriamiento, limite, iteraciones):
    x_actual = x_inicial
    y_actual = y_inicial
    valor_actual = himmelblau(x_actual, y_actual)
    
    temperatura = temperatura_inicial
    
    for i in range(iteraciones):
        #Generar un vecino aleatorio
        x_vecino, y_vecino = generar_vecino(x_actual, y_actual, limite)
        valor_vecino = himmelblau(x_vecino, y_vecino)
        
        #Diferencia en funcion de Himmelblau
        delta = valor_vecino - valor_actual
        

        if probabilidad_aceptacion(delta, temperatura) > random.random():
            x_actual = x_vecino
            y_actual = y_vecino
            valor_actual = valor_vecino

        temperatura *= enfriamiento

        if i % 500 == 0:
            print(f"Iteración {i + 1}: x = {x_actual:.5f}, y = {y_actual:.5f}, f(x, y) = {valor_actual:.5f}")
    
    return x_actual, y_actual, valor_actual


if __name__ == "__main__":
    x_inicial = random.uniform(-5, 5)  
    y_inicial = random.uniform(-5, 5)  
    temperatura_inicial = 10000  
    enfriamiento = 0.99  
    iteraciones = 10000  
    limite = 5  
    print(f"Punto inicial: x = {x_inicial:.5f}, y = {y_inicial:.5f}")
    x_min, y_min, valor_min = recocido_simulado(x_inicial, y_inicial, temperatura_inicial, enfriamiento, limite, iteraciones)

    #Final
    print(f"\nMínimo encontrado en: x = {x_min:.5f}, y = {y_min:.5f}, f(x, y) = {valor_min:.5f}")
