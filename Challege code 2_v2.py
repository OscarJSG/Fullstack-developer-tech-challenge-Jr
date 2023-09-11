import random

MIN_VALUE = -100
MAX_VALUE = 100
MAX_SIZE = 100

def validate_input(message, valid_range, expected_type):
    while True:
        try:
            user_input = expected_type(input(message))
            if valid_range[0] <= user_input <= valid_range[1]:
                return user_input
            else:
                print(f"\nPor favor, ingrese un valor entre {valid_range[0]} y {valid_range[1]}.")
        except ValueError:
            print(f"Por favor, ingrese un valor de tipo {expected_type.__name__} válido.")

def generate_manual_array():
    n = validate_input("\nIngrese el tamaño de la matriz: ", (1, MAX_SIZE), int)
    array = []
    for i in range(n):
        element = validate_input(f"\nIngrese el elemento {i + 1} de la matriz: ", (MIN_VALUE, MAX_VALUE), int)
        array.append(element)
    return array

def generate_random_array():
    n = validate_input("\nIngrese el tamaño de la matriz: ", (1, MAX_SIZE), int)
    array = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(n)]
    return array

def swap_elements(array, i, j):
    array[i], array[j] = array[j], array[i]

def bubble_sort(array):
    sorted_array = array.copy()
    n = len(sorted_array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if sorted_array[j] > sorted_array[j + 1]:
                swap_elements(sorted_array, j, j + 1)
    return sorted_array

def square_matrix(array):
    return [x ** 2 for x in array]

def filter_matrix(array, ss):
    return [x for x in array if 0 <= x <= ss]

def main():
    print("\nBienvenido al programa.")

    ss = validate_input("\nIngrese el valor de SS (entero positivo): ", (0, MAX_VALUE), int)
    
    option = input("\n¿Desea generar una matriz de forma manual o aleatoria? (M/A): ")
    while option not in ["M", "A"]:
        print("\nPor favor, escoja entre las opciones válidas.")
        option = input("\n¿Desea generar una matriz de forma manual o aleatoria? (M/A): ")
    if option == "M":
        input_array = generate_manual_array()
    else:
        input_array = generate_random_array()

    try:
        print("\nEsta es su matriz de entrada:")
        print(input_array)

        sorted_array = bubble_sort(input_array)
        print("\nEsta es su matriz ordenada de manera ascendente:")
        print(sorted_array)

        squared_matrix = square_matrix(sorted_array)
        print("\nEsta es su matriz cuadrada de números enteros ordenada:")
        print(squared_matrix)

        filtered_matrix = filter_matrix(squared_matrix, ss)
        print("\nEsta es la matriz resultante después de la eliminación de números fuera del rango [0, SS]:")
        print(filtered_matrix)

    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"\nSe produjo un error inesperado: {str(e)}")

    print("\nGracias por usar el programa.")

if __name__ == "__main__":
    main()
