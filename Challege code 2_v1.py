import random

def generar_matriz_aleatoria(n):
    matriz = [random.randint(1, 100) for _ in range(n)]
    return matriz

def elevar_al_cuadrado(matriz):
    return [num ** 2 for num in matriz]

def eliminar_numeros_fuera_de_rango(matriz, rango):
    return [num for num in matriz if rango[0] <= num <= rango[1]]

def ingresar_matriz_manualmente():
    n = int(input("\nIngrese el tamaño de la matriz (1-100): "))
    matriz = []

    for i in range(1, n + 1):
        while True:
            try:
                num = int(input("Ingrese el elemento {} de la matriz: ".format(i)))
                if 1 <= num <= 100:
                    matriz.append(num)
                    break
                else:
                    print("El número debe estar dentro del rango (1-100). Intente de nuevo.")
            except ValueError:
                print("La entrada no es un número entero. Intente de nuevo.")

    return matriz

def ordenar_matriz(matriz):
    return sorted(matriz)

def main():
    print("\n¿Desea generar una matriz aleatoria? (s/n): ")
    ans = input().lower()

    while ans not in ("s", "n"):
        print("\nLa respuesta debe ser 's' o 'n'")
        ans = input().lower()

    if ans == "s":
        n = int(input("\n¿De qué tamaño desea su matriz? (1-100): "))
        matriz_entrada = generar_matriz_aleatoria(n)
    else:
        matriz_entrada = ingresar_matriz_manualmente()

    matriz_ordenada = ordenar_matriz(matriz_entrada)

    print("\nMatriz resultante:")
    print(matriz_ordenada)

    matriz_cuadrados = elevar_al_cuadrado(matriz_ordenada)

    print("\nMatriz de cuadrados:")
    print(matriz_cuadrados)

    matriz_resultante = eliminar_numeros_fuera_de_rango(matriz_cuadrados, [0, 77])

    matriz_resultante = ordenar_matriz(matriz_resultante)

    print("\nMatriz resultante:")
    print(matriz_resultante)

if __name__ == "__main__":
    main()
