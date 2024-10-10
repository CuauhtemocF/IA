import random
import math

#Himmelblau
def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

#Derivadas
def derivada_x(x, y):
    return 4 * (x**2 + y - 11) * x + 2 * (x + y**2 - 7)

def derivada_y(x, y):
    return 2 * (x**2 + y - 11) + 4 * (x + y**2 - 7) * y

#Descenso de gradiente
def gradiente_descendente(x_inicial, y_inicial, tasa_aprendizaje, iteraciones, limite):
    x = x_inicial
    y = y_inicial

    for i in range(iteraciones):
        #Calcular las derivadas en el punto actual
        grad_x = derivada_x(x, y)
        grad_y = derivada_y(x, y)

        #Actualizar x e y utilizando la tasa de aprendizaje
        x = x - tasa_aprendizaje * grad_x
        y = y - tasa_aprendizaje * grad_y

        #Rango [-5, 5]
        x = max(min(x, limite), -limite)
        y = max(min(y, limite), -limite)

        #Iteracion
        print(f"Iteracion {i + 1}: x = {x:.3f}, y = {y:.3f}, f(x, y) = {himmelblau(x, y):.3f}")

    return x, y

if __name__ == "__main__":
    x_inicial = random.uniform(-5, 5)
    y_inicial = random.uniform(-5, 5)
    tasa_aprendizaje = 0.01
    iteraciones = 10  
    limite = 5  
    #Minimo de la funcion de Himmelblau
    x_min, y_min = gradiente_descendente(x_inicial, y_inicial, tasa_aprendizaje, iteraciones, limite)
    #Resultado final
    print(f"\nMinimo en: x = {x_min:.3f}, y = {y_min:.3f}, f(x, y) = {himmelblau(x_min, y_min):.3f}")
