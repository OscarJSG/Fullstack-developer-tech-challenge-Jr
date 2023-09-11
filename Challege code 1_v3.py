import random

def welcome_message():
    print("Bienvenido al programa de eliminación de dígitos")

def get_input_mode():

  while True:
    mode = input("Elija el modo de generación del arreglo: (1) manual (2) aleatorio: ")
    if mode in ("1", "2"):
      return mode
    else:
      print("Opción incorrecta. Por favor, elija entre las opciones válidas.")

def get_manual_array():
    n = int(input("Ingrese el tamaño del arreglo: "))
    while n < 1 or n > 100:
        n = int(input("Ingrese un tamaño válido del arreglo (entre 1 y 100): "))

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
        print("Ingrese un número válido.")
        return False

    number = int(number)
    if number < 1 or number > 100:
        print("El número debe estar en el rango de 1 a 100.")
        return False

    for digit in str(number):
        if int(digit) > S:
            print(f"El dígito {digit} no debe ser mayor que {S}.")
            return False

    return True

def get_random_array():
    n = int(input("Ingrese el tamaño del arreglo: "))
    while n < 1 or n > 100:
        n = int(input("Ingrese un tamaño válido del arreglo (entre 1 y 100): "))

    array = generate_random_array(n)
    print("Este es el arreglo generado aleatoriamente:", array)  # Mostrar el arreglo aleatorio
    return array

def generate_random_array(n):
    return [random.randint(1, 100) for _ in range(n)]

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
  n = len(array)
  for i in range(n // 2):
    array[i], array[n - i - 1] = array[n - i - 1], array[i]

  return array


def main():
    welcome_message()
    mode = get_input_mode()
    if mode == "1":
        array = get_manual_array()
    else:
        array = get_random_array()

    array = remove_digits(array, S)
    array = reorder_array(array)

    print("Este es el arreglo ordenado:", array)
    print("Fin del programa.")

if __name__ == "__main__":
    S = int(input("Ingrese el límite superior para los dígitos (S): "))
    main()
