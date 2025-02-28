# Funciones para la escritura y lectura de datos

def guardarDatos(filename: str,data: dict):
    """
    Guarda los datos en un archivo.

    Parameters:
        filename: El nombre del archivo
        data: Los datos a guardar
    """

    # Se abre el archivo en modo de escritura
    f = open(filename,"w")

    # Se busca los tipos de datos
    for i in data:
        # Se escribe el nombre
        f.write(f"--{i}\r\n")
        for j in data[i]:
            # Se escriben sus categorias
            f.write(f"-{j}\r\n")
            for k in data[i][j]:
                # Y se escriben sus datos
                f.write(f"{k}\r\n")

    # Finalmente se cierra el archivo
    f.close()

def leerDatos(filename: str) -> dict:
    """ 
    Se leen los datos guardados
    en un archivo.

    Parameters:
        filename: El nombre del archivo a leer
    """

    # Se abre el archivo en modo de lectura
    f = open(filename,"r")
    data = {}

    try:
        line = ""
        fatherScope = ""
        childScope = ""

        # Se lee el archivo linea por linea, se quitan los saltos de linea
        while (line := f.readline().replace("\n","").replace("\r","")):
            if line.strip() == "":
                # Si la linea esta vacia pasa la linea
                continue

            elif line.startswith("--"):
                # Si es un tipo de dato

                # Establece que tipo de dato es
                data[line[2:]] = {}
                fatherScope = line[2:]

            elif line.startswith("-"):
                # Si es una categoria

                # Guarda la categoria en el utimo tipo de dato
                data[fatherScope][line[1:]] = []

                # Establece la categoria en uso
                childScope = line[1:]

            else:
                # Si es un dato
                # Lo guarda en el ultimo tipo de categoria
                data[fatherScope][childScope].append(line)
    except FileNotFoundError:
        # Si no se haya el archivo devuelve datos por defecto
        f.close()
        return {"pendientes":{},"horario":{}}

    # Cierra el archivo y devuelve los datos leidos
    f.close()
    return data


def leerMaterias(filename: str) -> list[str]:
    """
    Lee las materias.

    Parameters:
        filename: El archivo donde se registraron las materias
    """
    m = []

    f = open(filename,"r")
    # Se lee el archivo, y el contenido se corta por los |, por ejemplo 1|2|3 = 1, 2, 3
    m = f.readline().split("|")
    f.close()
    
    return m # Devuelve m la cual tiene las materias