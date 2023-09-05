import tkinter as tk
from tkinter import messagebox

# Función para verificar las credenciales ingresadas por el usuario
def verificar_credenciales():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    # Verifica si las credenciales son correctas (esto es un ejemplo simple)
    if usuario == "usuario" and contrasena == "contrasena":
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
    else:
        messagebox.showerror("Inicio de sesión", "Credenciales incorrectas")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.geometry("600x600")

# Crear etiquetas y campos de entrada
label_usuario = tk.Label(ventana, text="Usuario:")
label_contrasena = tk.Label(ventana, text="Contraseña:")
entry_usuario = tk.Entry(ventana)
entry_contrasena = tk.Entry(ventana, show="*")  # La contraseña se muestra como asteriscos

# Crear botón de inicio de sesión
boton_iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=verificar_credenciales)

# Colocar etiquetas y campos de entrada en la ventana
label_usuario.pack()
entry_usuario.pack()
label_contrasena.pack()
entry_contrasena.pack()
boton_iniciar_sesion.pack()

# Ejecutar la aplicación
ventana.mainloop()