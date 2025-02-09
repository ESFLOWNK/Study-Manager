"""
El proposito de este programa es ser una herramienta util para
manejar las tareas y actividades escolares.
"""

# Importar la libreria de archivos
from pathlib import Path

def inicializar(archivo):
    """ Si el programa no ha sido configurado se inicia la configuracion """
    print("¿Que materias son impartidas en tu institucion?")
    print("Presiona Ctrl+C cuando ya no quede ninguna")

    materias = [] # Se crea una lista de materias

    try:
        # Se insertan materias hasta que se presione Ctrl+C
        while True:
            m = input(">> ") # Se pide que se escriba el nombre de la materia
            materias.append(m) # Se agregan materias a la lista
    except KeyboardInterrupt:
        # Si se presiona Ctrl+C este error sucede
        pass

    print("Listo!")

    f = open(archivo, 'w')
    f.write("|".join(materias))
    f.close()

def revisarPreInicializacion(archivo):
    # Revisa si el archivo existe
    if not Path(archivo).exists():
        inicializar(archivo) # Si no existe se busca inicializarlo

if __name__ == "__main__":
    revisarPreInicializacion("Materias.txt")