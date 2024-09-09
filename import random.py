import random

# Funcion objetivo f(x,y)
def funcion(x, y):
    return (1.5 - x + x * y) ** 2 + (2.25 - x + x * y) ** 2 + (2.625 - x + x * y) ** 2

# Rango de busqueda
min_rango = -4.5
max_rango = 4.5

# Numero de iteraciones
iteraciones = 10000

# Inicializar las mejores variables
mejor_x = random.uniform(min_rango, max_rango)
mejor_y = random.uniform(min_rango, max_rango)
mejor_f = funcion(mejor_x, mejor_y)

# Realizar la busqueda
for _ in range(iteraciones):
    # Generacion de valores aleatorios para (x) , (y)
    x = random.uniform(min_rango, max_rango)
    y = random.uniform(min_rango, max_rango)
    
    # Evaluar la funcion
    f_xy = funcion(x, y)
    
    # Encontramos el mejor valor, comparamos y lo almacenamos
    if f_xy < mejor_f:
        mejor_x = x
        mejor_y = y
        mejor_f = f_xy
# Valores utilizados
    print(f"Valores: x:{x}, y:{y}")

# Mejor valor encontrado
print(f"El mínimo encontrado es f({mejor_x}, {mejor_y}) = {mejor_f}")