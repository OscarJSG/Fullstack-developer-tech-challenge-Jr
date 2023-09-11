import random

def generar_matriz_aleatoria(n):
    matriz = []
    for i in range(n):
        matriz.append(random.randint(1, 100))
    return matriz

def ordenar_matriz(matriz):
    matriz.sort()
    return matriz

def calcular_cuadrados(matriz):
    nueva_matriz = []
    for num in matriz:
        nueva_matriz.append(num ** 2)
    return nueva_matriz

def eliminar_numeros_fuera_de_rango(matriz, rango):
    nueva_matriz = []
    for num in matriz:
        if num >= rango[0] and num <= rango[1]:
            nueva_matriz.append(num)
    return nueva_matriz

def main():
    # Preguntar al usuario si desea generar una matriz aleatoria
    print("\n¿Desea generar una matriz aleatoria? (s/n): ")
    ans = input().lower()

    # Validar la respuesta del usuario
    while ans not in ("s", "n"):
        print("\nLa respuesta debe ser 's' o 'n'")
        ans = input().lower()

    # Generar una matriz aleatoria
    if ans == "s":
        n = int(input("\n¿De qué tamaño desea su matriz? (1-100): "))
        matriz_entrada = generar_matriz_aleatoria(n)
    else:
        # Pedir al usuario una matriz de entrada
        matriz_entrada = []
        print("\nIngrese el tamaño de la matriz: ")
        n = int(input())
        for i in range(1, n + 1):
            num = input("Ingrese el elemento {} de la matriz: ".format(i))
            valido = False
            while not valido:
                try:
                    num = int(num)
                    valido = True
                except ValueError:
                    print("La entrada no es un número entero. Intente de nuevo.")
                    num = input("Ingrese el elemento {} de la matriz: ".format(i))
            matriz_entrada.append(num)

    # Ordenar la matriz
    matriz_ordenada = ordenar_matriz(matriz_entrada)

    # Imprimir la matriz resultante
    print("\nMatriz resultante:")
    print(matriz_ordenada)

    # Calcular los cuadrados de la matriz ordenada
    matriz_cuadrados = calcular_cuadrados(matriz_ordenada)

    # Imprimir la matriz de cuadrados
    print("\nMatriz de cuadrados:")
    print(matriz_cuadrados)

    # Eliminar los números fuera de rango
    matriz_resultante = eliminar_numeros_fuera_de_rango(matriz_cuadrados, [0, 77])

    # Ordenar la matriz resultante
    matriz_resultante = ordenar_matriz(matriz_resultante)

    # Imprimir la matriz resultante
    print("\nMatriz resultante:")
    print(matriz_resultante)

if __name__ == "__main__":
    main()
