import tkinter as tk


ventana = tk.Tk()
ventana.title("Tarea 3")
ventana.geometry("600x600")

etiqueta = tk.Label(ventana, text="¡Hola, esta es una etiqueta!")
etiqueta.pack()


# Iniciar el bucle principal de la aplicación

ventana.mainloop()