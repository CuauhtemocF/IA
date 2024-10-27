#Ruta Absoluta
ruta_archivo = r'C:\Users\bleak\OneDrive\Imágenes\Escom 9\IA\bezdekIris.data'

#Matriz
datos = []

#Leectura del archivo linea por linea
with open(ruta_archivo, 'r') as archivo:
    for linea in archivo:
        #Separacion por coma y eliminacion de espacios en blanco
        valores = linea.strip().split(',')
        #Evitar lineas vacias
        if len(valores) == 5:
            datos.append(valores)

#Imprimir Filas
for fila in datos[:150]:
    print(fila)

