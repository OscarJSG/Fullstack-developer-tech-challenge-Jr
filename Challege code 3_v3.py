import random

def obtener_opcion():
    while True:
        opcion = input("\n¿Desea generar un arreglo de entrada de manera manual o aleatoria? (m/a): ")
        if opcion == "m" or opcion == "a":
            return opcion
        else:
            print("Ingrese por favor alguna de las opciones válidas (m/a).")

def obtener_tamano_arreglo():
    while True:
        try:
            tam_arreglo = int(input("\nIngrese el tamaño del arreglo de entrada (1-99): "))
            if 1 <= tam_arreglo <= 99:
                return tam_arreglo
            else:
                print("Digite por favor un valor entero positivo válido dentro del rango [1, 99], gracias.")
        except ValueError:
            print("Ingrese por favor un valor entero positivo válido dentro del rango [1, 99], gracias.")

def obtener_valor_arreglo():
    while True:
        try:
            valor = int(input("\nIngrese el valor del elemento del arreglo (1-100): "))
            if 1 <= valor <= 100:
                return valor
            else:
                print("Digite por favor un valor entero positivo válido menor o igual a 100, gracias.")
        except ValueError:
            print("Ingrese por favor un valor entero positivo válido menor o igual a 100, gracias.")

def generar_arreglo_manual(tam_arreglo):
    return [obtener_valor_arreglo() for _ in range(tam_arreglo)]

def generar_arreglo_aleatorio(tam_arreglo):
    arreglo = [random.randint(1, 100) for _ in range(tam_arreglo)]
    print("\nEste es el arreglo generado de manera aleatoria:", arreglo)
    return arreglo

def calcular_cantidad_minima(arreglo):
    arreglo.sort()
    return sum(arreglo) + 1

def main():
    print("\nBienvenido al programa de cambio.\n")
    
    opcion = obtener_opcion()
    tam_arreglo = obtener_tamano_arreglo()

    if opcion == "m":
        arreglo = generar_arreglo_manual(tam_arreglo)
    else:
        arreglo = generar_arreglo_aleatorio(tam_arreglo)

    cantidad_minima = calcular_cantidad_minima(arreglo)

    print("\nLa cantidad mínima de cambio que NO puede ser entregada es:", cantidad_minima)
    print("\nGracias por utilizar el programa de cambio.\n")

if __name__ == "__main__":
    main()

