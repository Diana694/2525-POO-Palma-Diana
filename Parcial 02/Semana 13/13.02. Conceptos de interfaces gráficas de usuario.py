import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    texto = entrada.get()
    if texto:
        lista_datos.insert(tk.END, texto)
        entrada.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa un dato antes de agregar.")

# Función para limpiar la entrada y la lista seleccionada
def limpiar():
    entrada.delete(0, tk.END)
    seleccion = lista_datos.curselection()
    if seleccion:
        lista_datos.delete(seleccion)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos - Aplicación GUI Básica")
ventana.geometry("400x300")  # Tamaño de la ventana

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato, bg="lightgreen")
boton_agregar.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar, bg="lightcoral")
boton_limpiar.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
