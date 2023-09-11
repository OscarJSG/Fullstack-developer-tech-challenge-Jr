import random

def get_option():
    while True:
        option = input("\n¿Desea generar una matriz de entrada manualmente o al azar? (m/r): ")
        if option == "m" or option == "r":
            return option
        else:
            print("Por favor, ingrese una de las opciones válidas (m/r).")

def get_array_size():
    while True:
        try:
            array_size = int(input("\nIngrese el tamaño de la matriz de entrada (1-99): "))
            if 1 <= array_size <= 99:
                return array_size
            else:
                print("Por favor, ingrese un número entero positivo válido dentro del rango [1, 99], gracias.")
        except ValueError:
            print("Por favor, ingrese un número entero positivo válido dentro del rango [1, 99], gracias.")

def get_array_value():
    while True:
        try:
            value = int(input("\nIngrese el valor del elemento de la matriz (1-100): "))
            if 1 <= value <= 100:
                return value
            else:
                print("Por favor, ingrese un número entero positivo válido menor o igual a 100, gracias.")
        except ValueError:
            print("Por favor, ingrese un número entero positivo válido menor o igual a 100, gracias.")

def generate_manual_array(array_size):
    return [get_array_value() for _ in range(array_size)]

def generate_random_array(array_size):
    array = [random.randint(1, 100) for _ in range(array_size)]
    print("\nThis is the array generated randomly:", array)
    return array

def calculate_minimum_change_amount(array):
    array.sort()
    return sum(array) + 1

def main():
    print("\nBienvenido al programa Calculadora de Cambio.\n")
    
    option = get_option()
    array_size = get_array_size()

    if option == "m":
        array = generate_manual_array(array_size)
    else:
        array = generate_random_array(array_size)

    minimum_change = calculate_minimum_change_amount(array)

    print(f"\nLa cantidad mínima de cambio que NO SE PUEDE DAR es: {minimum_change}")
    print("\nGracias por usar el programa Calculadora de Cambio.\n")

if __name__ == "__main__":
    main()
