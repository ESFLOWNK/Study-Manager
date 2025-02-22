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

        materias = [i.title() for i in pedirVariasOpcionesStr()]

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
        manejarPendientes(data,materias)
        guardarDatos(datafilename,data)
    elif op == 2:
        manejarHorario(data)
        guardarDatos(datafilename,data)
    elif op == 3:
        configurarMaterias(materias)
        Path(materiasfilename).write_text("|".join(materias))
    elif op == 4:
        return 1 # Devuelve 1 y el programa termina

    return 0 # Devuelve 0

if __name__ == "__main__":
    inicializar() # Si no esta del todo inicializado, se inicializa

    materias = leerMaterias(materiasfilename) # Se leen las materias
    data = leerDatos(datafilename)

    while True: # Se crea un bucle infinito

        r = opciones() # Llamamos a la funcion de opciones, el resultado se guarda en r

        if r == 1:
            break # Si r es 1 entonces rompe el bucle y el programa termina

    guardarDatos(datafilename,data)
    Path(materiasfilename).write_text("|".join(materias))