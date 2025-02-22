"""
El proposito de este programa es ser una herramienta util para
manejar las tareas y actividades escolares.
"""

# Importar la libreria de archivos
from pathlib import Path
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

        mats = [] # Se crea una lista de materias

        try:
            # Se insertan materias hasta que se presione Ctrl+C
            while True:
                mat = pedirOpcionStr(">> ") # Se pide que se escriba el nombre de la materia
                mats.append(mat.title()) # Se agregan materias a la lista
        except KeyboardInterrupt:
            # Si se presiona Ctrl+C este error sucede
            pass

        print("Listo!")

        # Se escriben las materias en su respectivo archivo
        Path(materiasfilename).write_text("|".join(materias))
    
    if not Path(datafilename).exists():
        # Se crea el archivo de los datos si no existe
        guardarDatos(datafilename,data)

def opciones():
    mostrarOpciones([
        "Manejar pendientes",
        "Manejar el horario",
        "Configurar las materias",
        "Salir"
    ])
    
    op = pedirOpcion(1,4)

    if op == 1:
        manejarPendientes(data)
    elif op == 2:
        manejarHorario()
    elif op == 3:
        configurarMaterias()
    elif op == 4:
        return 1 # Devuelve 1 y el programa termina

    return 0 # Devuelve 0

if __name__ == "__main__":
    inicializar() # Si no esta del todo inicializado, se inicializa

    materias = leerMaterias("Materias.txt") # Se leen las materias
    data = leerDatos(datafilename)

    while True: # Se crea un bucle infinito

        r = opciones() # Llamamos a la funcion de opciones, el resultado se guarda en r

        if r == 1:
            break # Si r es 1 entonces rompe el bucle y el programa termina

    guardarDatos(datafilename,data)