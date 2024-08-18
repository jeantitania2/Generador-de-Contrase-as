import tkinter as tk
import random
import string
import sqlite3
import ttkbootstrap as ttk

# Función para generar la contraseña
def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Función para guardar la contraseña en la base de datos
def guardar_contrasena(contrasena):
    conn = sqlite3.connect('contrasenas.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS contrasenas (id INTEGER PRIMARY KEY, contrasena TEXT)')
    cursor.execute('INSERT INTO contrasenas (contrasena) VALUES (?)', (contrasena,))
    conn.commit()
    conn.close()

# Función para manejar el botón de generar
def generar_y_guardar():
    longitud = int(entry_longitud.get())
    contrasena = generar_contrasena(longitud)
    label_contrasena.config(text=contrasena)
    guardar_contrasena(contrasena)

# Configuración de la ventana principal
root = ttk.Window(themename = 'darkly')
root.title("Generador de Contraseñas")

# Entrada para la longitud de la contraseña
label_longitud = ttk.Label(root, text="Longitud de la contraseña:")
label_longitud.pack()

entry_longitud = ttk.Entry(root)
entry_longitud.pack()

# Botón para generar y guardar la contraseña
boton_generar = ttk.Button(root, text="Generar Contraseña", command=generar_y_guardar)
boton_generar.pack()

# Etiqueta para mostrar la contraseña generada
label_contrasena = ttk.Label(root, text="", font=("Helvetica", 16))
label_contrasena.pack()

# Iniciar el bucle principal de la interfaz
root.mainloop()
