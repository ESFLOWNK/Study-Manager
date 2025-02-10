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
            materias.append(m.title()) # Se agregan materias a la lista
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

def leerMaterias(archivo) -> list[str]:
    m = []

    f = open(archivo,'r')
    # Se lee el archivo, y el contenido se corta por los |, por ejemplo 1|2|3 = 1, 2, 3
    m = f.readline().split("|")
    f.close()
    
    return m # Devuelve m la cual tiene las materias

def pedirOpcion(desde: int,hasta: int) -> int:
    op = "" # Crea una variable que contiene las opciones ingresadas
    while not op in [str(i) for i in range(desde,hasta+1)]:
        # Revisa que op sea digitos y que sea mayor que 0 o menor que 4
        # De no ser asi se repite el proceso

        op = input(">> ")

    return int(op)

def manejarPendientes():
    pass

def manejarHorario():
    pass

def configurarMaterias():
    pass

def opciones():
    print("Opciones:\n",
          "\n1. Manejar pendientes\n",
          "2. Manejar el horario\n",
          "3. Configurar las materias\n")
    
    op = pedirOpcion(1,3)

    if op == 1:
        manejarPendientes()
    elif op == 2:
        manejarHorario()
    elif op == 3:
        configurarMaterias()

if __name__ == "__main__":
    revisarPreInicializacion("Materias.txt") # Se revisa el archivo
    m = leerMaterias("Materias.txt") # Se leen las materias

    opciones() # Llamamos a la funcion de opciones