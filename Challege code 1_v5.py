import random

def welcome_message():
    print("\nBienvenido al programa de eliminación de dígitos\n")

# Unicos modos de entrada son manual o aleatorio 
def get_input_mode():
    while True:
        mode = input("\nElija el modo de generación del arreglo: (1) manual (2) aleatorio: ")
        if mode in ("1", "2"):
            return mode
        print("\nOpción incorrecta. Por favor, elija entre las opciones válidas.\n")

# Tamaño del arreglo entre 1 y 100 y debe ser entero    
def get_size_array():
    while True:
        try:
            n = int(input("\nIngrese el tamaño del arreglo: "))
            if n < 1 or n > 100:
                print("\nIngrese un tamaño válido del arreglo (entre 1 y 100).\n")
                continue
            break
        except ValueError:
            print("\nIngrese un número válido.\n")

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
    # Agregar condiciones adicionales aquí
    if not array:
        print("\nEl arreglo no puede estar vacío.")
        return get_manual_array(n)  # Vuelve a solicitar la entrada si el arreglo está vacío
    if len(set(array)) == 1:
        print("\nTodos los elementos del arreglo son iguales.")
        return get_manual_array(n)  # Vuelve a solicitar la entrada si todos los elementos son iguales
    if all(num > S for num in array):
        print("\nTodos los elementos del arreglo son mayores que S.")
        return get_manual_array(n)  # Vuelve a solicitar la entrada si todos los elementos son mayores que S
    
    return array


def is_valid_manual_input(number): 
    if not number.isdigit():  # Valida que la entrada sea un numero
        print("\nIngrese un número válido.\n")
        return False

    number = int(number)
    if number < 1 or number > 100:  # Valida que el numero ingresado este en el rango
        print("\nEl número debe estar en el rango de 1 a 100.\n")
        return False

    for digit in str(number):
        if int(digit) > S: # Valida que cada digito sea menor a S
            print(f"\nEl dígito {digit} no debe ser mayor que {S}.\n")
            return False

    return True

def generate_random_array(n):
    random_array = [random.randint(1, 100) for _ in range(n)] # Arreglo generado de manera randomica en el rango especificado con n tamaño
    print("\nEste es su arreglo de entrada generado de manera aleatoria:", random_array)
    return random_array


def remove_digits(array, S):
    
    new_array = []

    for number in array:  # Itera a través de los números en la lista 'array'
        new_number = 0
        has_valid_digit = False  # variable 'has_valid_digit' para verificar si al menos un dígito es válido

        for digit in str(number):  # Convierte el número actual en una cadena para iterar a través de los dígitos
    
            if int(digit) < S:
                
                new_number = new_number * 10 + int(digit) # Evalua un primer digito en la segunda pasada si cumple condicion se le agrega las decenas
                has_valid_digit = True 
        
        if has_valid_digit:  # Si al menos un dígito es válido en el número, agrega 'new_number' a la lista 'new_array'
            new_array.append(new_number)

    
    return new_array  # 'new_array' que contiene los números modificados


def reorder_array(array):
    return array[::-1]

def main():
    welcome_message()
    global input_mode, S
    input_mode = get_input_mode()
    
    while True:
        try:
            S = int(input("\nIngrese el límite superior para los dígitos (S): "))
            break
        except ValueError:
            print("\nIngrese un número válido para S.\n")

    array = get_size_array()
    array = remove_digits(array, S)
    array = reorder_array(array)
    print("\nEste es el arreglo ordenado:", array)
    print("\nFin del programa.\n")

if __name__ == "__main__":
    main()
    print(__name__)