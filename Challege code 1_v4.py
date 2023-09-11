import random

def welcome_message():
    print("\nBienvenido al programa de eliminación de dígitos\n")

def get_input_mode():
    while True:
        mode = input("\nElija el modo de generación del arreglo: (1) manual (2) aleatorio: ")
        if mode in ("1", "2"):
            return mode
        print("\nOpción incorrecta. Por favor, elija entre las opciones válidas.\n")

def get_array():
    n = int(input("\nIngrese el tamaño del arreglo: "))
    while n < 1 or n > 100:
        n = int(input("\nIngrese un tamaño válido del arreglo (entre 1 y 100): "))

    if input_mode == "1":
        return get_manual_array(n)
    else:
        return generate_random_array(n)

def get_manual_array(n):
    array = []
    for i in range(n):
        while True:
            number = input(f"Ingrese el elemento {i + 1}: ")
            if is_valid_manual_input(number):
                array.append(int(number))
                break
    return array

def is_valid_manual_input(number):
    if not number.isdigit():
        print("\nIngrese un número válido.\n")
        return False

    number = int(number)
    if number < 1 or number > 100:
        print("\nEl número debe estar en el rango de 1 a 100.\n")
        return False

    for digit in str(number):
        if int(digit) > S:
            print(f"\nEl dígito {digit} no debe ser mayor que {S}.\n")
            return False

    return True

def generate_random_array(n):
    random_array = [random.randint(1, 100) for _ in range(n)]
    print("\nEste es su arreglo de entrada generado de manera aleatoria:", random_array)
    return random_array


def remove_digits(array, S):
    
    new_array = []

    for number in array:
        new_number = 0
        has_valid_digit = False  # Verifica si al menos un dígito es válido
        for digit in str(number):
            if int(digit) < S:
                new_number = new_number * 10 + int(digit)
                has_valid_digit = True
        if has_valid_digit:  # Agregar solo si al menos un dígito es válido
            new_array.append(new_number)

    return new_array

def reorder_array(array):
    return array[::-1]

def main():
    welcome_message()
    global input_mode, S
    input_mode = get_input_mode()
    S = int(input("\nIngrese el límite superior para los dígitos (S): "))
    array = get_array()
    array = remove_digits(array, S)
    array = reorder_array(array)
    print("\nEste es el arreglo ordenado:", array)
    print("\nFin del programa.\n")

if __name__ == "__main__":
    main()
