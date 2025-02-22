"""
El proposito de este programa es ser una herramienta util para
manejar las tareas y actividades escolares.
"""

# Importar la libreria de archivos
from pathlib import Path

data = {"pendientes":{},"horario":{}}
materias = []

def guardarDatos(f):
    for i in data:
        f.write(f"--{i}\r\n")
        for j in data[i]:
            f.write(f"-{j}\r\n")
            for k in data[i][j]:
                f.write(f"{k}\r\n")

def leerDatos(f):
    try:
        line = ""
        fatherScope = ""
        childScope = ""
        while (line := f.readline().replace("\n","").replace("\r","")):
            if line.strip() == "":
                continue

            elif line.startswith("--"):
                data[line[2:]] = {}
                fatherScope = line[2:]

            elif line.startswith("-"):
                data[fatherScope][line[1:]] = []
                childScope = line[1:]

            else:
                data[fatherScope][childScope].append(line)
    except FileNotFoundError:
        pass

def pedirOpcion(desde: int,hasta: int) -> int:
    op = "" # Crea una variable que contiene las opciones ingresadas
    if hasta == 0:
        return -1
    while not op in [str(i) for i in range(desde,hasta+1)]:
        # Revisa que op sea digitos y que sea mayor que 0 o menor que 4
        # De no ser asi se repite el proceso

        op = input(">> ")

    return int(op) # Devuelve la opcion a manera de int

def pedirOpcionStr(text: str) -> str:
    op = "" # Crea una variable que contiene las opciones ingresadas
    while "|" in op or "." in op or "-" in op or op.strip() == "":
        # Revisa que op no tenga caracteres especiales
        op = input(text)

    return op # Devuelve la opcion a manera de int

def inicializar(archivo):
    """ Si el programa no ha sido configurado se inicia la configuracion """
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

    f = open(archivo, 'w')
    f.write("|".join(materias))
    f.close()

    f = open("data","w")
    guardarDatos(f)
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

def mostrarOpciones(opciones: list[str], header = True):
    if header: print("Opciones:\n")

    for i in range(0,len(opciones)): # Hace que la variable i vaya desde cero hasta
                                     # el numero de elementos que tiene opciones, en bucle

        print(f"{i+1}. {opciones[i]}") # Se imprime i+1 y la opcion actual
    
    print("") # Hace un salto de linea

def manejarPendientes():
    mostrarOpciones([
        "Ver pendientes",
        "Crear pendientes",
        "Eliminar pendientes"
    ])

    op = pedirOpcion(1,3)
    
    if op == 1:
        mats = list(data["pendientes"].keys())
        mostrarOpciones(mats, False)
        op = pedirOpcion(1,len(mats))-1
        pendientes = data["pendientes"][mats[op]]
        print("\n".join(["- "+i for i in pendientes])+"\n")
    elif op == 2:
        mats = list(data["pendientes"].keys())
        mostrarOpciones(mats, False)
        print("Seleccione la materia del pendiente")
        op = pedirOpcion(1,len(mats))-1
        pendiente = pedirOpcionStr("Inserte el pendiente\n>> ")
        data["pendientes"][mats[op]].append(pendiente)
        print("")
    elif op == 3:
        mats = list(data["pendientes"].keys())
        mostrarOpciones(mats, False)
        print("Seleccione la materia del pendiente")
        op = pedirOpcion(1,len(mats))-1
        pendientes = data["pendientes"][mats[op]]
        mostrarOpciones(pendientes)
        print("Seleccione el pendiente")
        penop = pedirOpcion(1,len(pendientes))-1
        _ = data["pendientes"][mats[op]].pop(penop)

def manejarHorario():
    pass

def configurarMaterias():
    pass

def opciones():
    mostrarOpciones([
        "Manejar pendientes",
        "Manejar el horario",
        "Configurar las materias",
        "Salir"
    ])
    
    op = pedirOpcion(1,4)

    if op == 1:
        manejarPendientes()
    elif op == 2:
        manejarHorario()
    elif op == 3:
        configurarMaterias()
    elif op == 4:
        return 1 # Devuelve 1 y el programa termina

    return 0 # Devuelve 0

if __name__ == "__main__":
    revisarPreInicializacion("Materias.txt") # Se revisa el archivo
    materias = leerMaterias("Materias.txt") # Se leen las materias

    f = open("data","r")
    leerDatos(f)
    f.close()

    while True: # Se crea un bucle infinito

        r = opciones() # Llamamos a la funcion de opciones, el resultado se guarda en r

        if r == 1:
            break # Si r es 1 entonces rompe el bucle y el programa termina

    f = open("data","w")
    guardarDatos(f)
    f.close()