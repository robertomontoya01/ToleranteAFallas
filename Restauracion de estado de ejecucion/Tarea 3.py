import pickle
import time

# Función para guardar el estado actual en un archivo
def guardar_estado(estado, archivo):
    with open(archivo, 'wb') as f:
        pickle.dump(estado, f)

# Función para cargar el estado desde un archivo
def cargar_estado(archivo):
    with open(archivo, 'rb') as f:
        estado = pickle.load(f)
    return estado

def imprimir_estado():
    print("\nEstado " + estado + ": ")
    print("Contador:", contador)
    print("Nombre:", nombre)
    print("Lista de tareas:", lista_de_tareas)
    time.sleep(1.5)
    
def modificar_estado():
    contador += 1
    nombre = input("Digita el nombre: ")
    var = input("Digita tarea nueva: ")
    lista_de_tareas.append(var)
    
# Ejemplo de variables de estado
estado = "Inicial"
contador = 0
nombre = "Juan"
lista_de_tareas = ["Tarea 1", "Tarea 2", "Tarea 3"]

# Guardar el estado actual en un archivo
estado_actual = {
    'contador': contador,
    'nombre': nombre,
    'lista_de_tareas': lista_de_tareas
}
guardar_estado(estado_actual, 'estado.txt')

# Imprimir el estado Inicial
imprimir_estado()



# Modificar las variables de estado
contador = contador + 1
nombre = input("Nombre: ")
lista_de_tareas.append("Tarea 4")

# Guardar el estado actual en un archivo
estado_actual = {
    'contador': contador,
    'nombre': nombre,
    'lista_de_tareas': lista_de_tareas
}
guardar_estado(estado_actual, 'estado.txt')

# Imprimir el estado restaurado
imprimir_estado()

# Cargar el estado desde el archivo para restaurarlo
estado_guardado = cargar_estado('estado.txt')
contador = estado_guardado['contador']
nombre = estado_guardado['nombre']
lista_de_tareas = estado_guardado['lista_de_tareas']

# Imprimir el estado restaurado
guardar_estado(estado_actual, 'estado.txt')
imprimir_estado()