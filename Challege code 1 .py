import random

def size_array():
  while True:
    n = input("\n Ingrese el tamaño del arreglo (n): ")
    try:
      n = int(n)
      if n <= 100 and n >= 1:
        return n
    except ValueError:
      print("\n El tamaño del arreglo debe ser un número entero.\n")
    else:
      if n > 100:
        print("\n El tamaño del arreglo debe ser menor o igual a 100.\n")
      else:
        print("\n El tamaño del arreglo debe ser mayor que 1.\n")

def crear_array(n):
  array = []
  for i in range(n):
    array.append(random.randint(0, 100))
  return array


def mostrar_array(array):
  print("\n El primer valor numérico del código Hash MD5 es el: 7 por lo tanto S = 7 \n")
  print(array)

  for i in range(len(array)):
    if not isinstance(array[i], int) or array[i] < 0:
      raise ValueError("El elemento {} del arreglo no es un número entero positivo.".format(i))

def borrar_digitos(array, s):
  for i in range(len(array)):
    nueva_cadena = ""
    cadena = str(array[i])
    eliminado = False
    for caracter in cadena:
      if int(caracter) < s:
        nueva_cadena += caracter
      else:
        eliminado = True
    if nueva_cadena == "" and eliminado:
      array[i] = None
    else:
      array[i] = int(nueva_cadena)



def show_resultado(array):
  result = []
  for i in range(len(array) - 1, -1, -1):
    if array[i] is not None:
      result.append(array[i])
  print(result)


n = size_array()
array = crear_array(n)
mostrar_array(array)
borrar_digitos(array, 7)
show_resultado(array)
