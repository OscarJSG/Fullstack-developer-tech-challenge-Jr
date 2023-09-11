import random

def elegir_metodo():
  while True:
    print("\n ¿Desea generar el arreglo de entrada de forma aleatoria o ingresarlo manualmente?")
    print("1. Generar aleatoriamente")
    print("2. Ingresar manualmente")
    opcion = input("\n Ingrese su opción: ")
    try:
      opcion = int(opcion)
      if opcion == 1 or opcion == 2:
        return opcion
    except ValueError:
      print("\n La opción debe ser un número entero.\n")
    else:
      print("\n La opción debe ser 1 o 2.\n")

def crear_array(n):
  array = []
  for i in range(n):
    array.append(random.randint(0, 99))
  return array

def ingresar_array():
  n = int(input("\n Ingrese el tamaño del arreglo (n): "))
  array = []
  for i in range(n):
    array.append(int(input("Ingrese el valor del elemento {}: ".format(i))))
  return array

def mostrar_array(array):
  print(array)

def borrar_digitos(array, s):
  for i in range(len(array)):
    array[i] = int("".join([d for d in str(array[i]) if int(d) < s]))

def show_resultado(array):
  print(list(reversed([i for i in array if i is not None])))


opcion = elegir_metodo()
if opcion == 1:
  array = crear_array(n)
elif opcion == 2:
  array = ingresar_array()

mostrar_array(array)
borrar_digitos(array, 7)
show_resultado(array)
