"""
El proposito de este programa es ser una herramienta util para
manejar las tareas y actividades escolares.
"""

# Importar la libreria de archivos
from pathlib import Path
# Importar las librerias propias
from handleOptions import *
from handleFiles import *
from handleData.pendientes import manejarPendientes
from handleData.horario import *
from handleData.materias import *

# Variables de uso comun
data = {"pendientes":{},"horario":{}}
materias = []

# Parametros
materiasfilename = "materias.txt"
datafilename = "data"

def inicializar():
    """ Si el programa no ha sido configurado se inicia la configuracion """

    if not Path(materiasfilename).exists():
        # Si el archivo de las materias no existe, se crea

        print("¿Que materias son impartidas en tu institucion?")
        print("Presiona Ctrl+C cuando ya no quede ninguna")

        # Pide materias, y las guarda como un titulo, con mayuscula al principio
        materias = [i.title() for i in pedirVariasOpcionesStr()]

        # Se escriben las materias en su respectivo archivo
        Path(materiasfilename).write_text("|".join(materias))
    
    if not Path(datafilename).exists():
        # Se crea el archivo de los datos si no existe
        guardarDatos(datafilename,data)

def opciones():
    """
    Ofrece las opciones al usuario
    llama a una funcion u otra segun
    la opcion ingresada por el usuario
    """

    # Muestra las opciones
    mostrarOpciones([
        "Manejar pendientes",
        "Manejar el horario",
        "Configurar las materias",
        "Salir"
    ])
    
    # Pide una opcion
    op = pedirOpcion(1,4)

    if op == 1: # Si la opcion es 1
        # Accede a manejar pendiente y guarda los datos
        manejarPendientes(data,materias)
        guardarDatos(datafilename,data)
    elif op == 2: # Si la opcion es 2 y guarda los datos
        # Accede a manejar el horario
        manejarHorario(data)
        guardarDatos(datafilename,data)
    elif op == 3: # Si la opcion es 3
        # Accede a configurar las materias
        configurarMaterias(materias)
        # Y lo guarda es un archivo, dividiendo las
        # materias por este caracter: '|'
        Path(materiasfilename).write_text("|".join(materias))
    elif op == 4: # Si la opcion es 4
        return 1 # Devuelve 1 y el programa termina

    return 0 # Devuelve 0

if __name__ == "__main__": # Lo primero en ejecutarse
    inicializar() # Si no esta del todo inicializado, se inicializa

    materias = leerMaterias(materiasfilename) # Se leen las materias
    data = leerDatos(datafilename) # Se leen los datos guardados

    while True: # Se crea un bucle infinito

        r = opciones() # Llamamos a la funcion de opciones, el resultado se guarda en r

        if r == 1:
            break # Si r es 1 entonces rompe el bucle y el programa termina

    # Guarda los datos y las materias
    guardarDatos(datafilename,data)
    Path(materiasfilename).write_text("|".join(materias))