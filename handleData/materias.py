"""
Este es el modulo que controla el manejo de materias
"""

# Importa la libreria de opciones
from handleOptions import mostrarOpciones, pedirOpcion, pedirOpcionStr

def verMaterias(data: dict):
    """
    Muestra las materias
    
    Parameters:
        data: contienene los datos de las materias a mostrarse
    """

    # Muestra las materias
    print("\n".join([f"- {i}" for i in data["materias"]]))

def agregarMateria(data: dict[str,dict[list] | list]):
    """
    Agrega una materia a la lista

    Parameters:
        data: contiene los datos registrados
    """

    # Pide el nombre de la materia
    mat = pedirOpcionStr("Inserte el nombre de la materia\n>> ")

    # Agrega la materia
    data["materias"].append(mat.title())

def modificarMateria(data: dict):
    """
    Modifica el nombre de una materia

    Parameters:
        data: Son los datos registrados 
    """

    # Muestra las materias
    mostrarOpciones(data["materias"])

    # Pide que elijas una materia
    op = pedirOpcion(1,len(data["materias"]))-1
    if op == -1:
        print("No hay ninguna materia resgistrada!")
        return

    # Pide el nuevo nombre de la materia
    mat = pedirOpcionStr("Inserte la materia\n>> ")

    # Realiza la modificacion
    data["materias"][op] = mat

def borrarMateria(data: dict):
    """
    Borra una materia de la lista de materias

    Parameters:
        data: Son los datos registrados 
    """

    # Pide que se elija una materia
    print("Eliga la materia a borrar:")
    mostrarOpciones(data["materias"], False)
    op = pedirOpcion(1,len(data["materias"]))-1
    if op == -1:
        print("No hay ninguna materia resgistrada!")
        return

    # Se borra la materia
    data["materias"].pop(op)

def configurarMaterias(data: dict):
    """
    Es la funcion la cual muestra las
    opciones disponibles al usuario.

    Parameters:
        data: Son los datos registrados 
    """

    mostrarOpciones([
        "Ver materias",
        "Agregar materia",
        "Modificar materia",
        "Borrar materia",
        "Cancelar"
    ])

    op = pedirOpcion(1,5)

    if op == 1: # Si se elige 1 se ven las materias
        verMaterias(data)
    elif op == 2: # Si se elige 2 se agrega una materia
        agregarMateria(data)
    elif op == 3: # Si se elige 3 se modifica una materia
        modificarMateria(data)
    elif op == 4: # Si se elige 4 se borra una materia
        borrarMateria(data)