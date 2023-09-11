import tkinter as tk
from tkinter import messagebox
import random

def size_array():
    while True:
        n = input_box.get()
        try:
            n = int(n)
            if n <= 100 and n >= 1:
                return n
        except ValueError:
            messagebox.showerror("Error", "El tamaño del arreglo debe ser un número entero.")
        else:
            if n > 100:
                messagebox.showerror("Error", "El tamaño del arreglo debe ser menor o igual a 100.")
            else:
                messagebox.showerror("Error", "El tamaño del arreglo debe ser mayor que 1.")

def crear_array(n):
    array = []
    for i in range(n):
        array.append(random.randint(0, 100))
    return array

def mostrar_array():
    n = size_array()
    array = crear_array(n)
    result_label.config(text="El primer valor numérico del código Hash MD5 es el: 7 por lo tanto S = 7")
    original_array_label.config(text=str(array))
    borrar_digitos(array, 7)
    show_resultado(array)

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
    resultado_label.config(text=str(result))

# Crear una ventana
ventana = tk.Tk()
ventana.title("Procesador de Arreglo by Oscar Solano")

# Crear etiquetas y cuadros de entrada
input_label = tk.Label(ventana, text="Ingrese el tamaño del arreglo (n):")
input_box = tk.Entry(ventana)
original_array_label = tk.Label(ventana, text="")
result_label = tk.Label(ventana, text="")
resultado_label = tk.Label(ventana, text="")

# Crear botón para calcular y mostrar el resultado
calcular_button = tk.Button(ventana, text="Calcular", command=mostrar_array)

# Colocar elementos en la ventana
input_label.pack()
input_box.pack()
calcular_button.pack()
original_array_label.pack()
result_label.pack()
resultado_label.pack()

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
