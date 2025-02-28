from handleOptions import pedirOpcion, mostrarOpciones, pedirOpcionStr

def verPendientes(data: dict):
    """
    Muestra los pendientes guardados.

    Parameters:
        data: son los datos guardados
    """

    # Obtiene todas las materias con pendientes
    mats = list(data["pendientes"].keys())

    # Muestra las materias y te pide que elijas una
    print("Seleccione la materia")
    mostrarOpciones(mats, False)
    op = pedirOpcion(1,len(mats))-1

    if op == -2:
        # Si no hay pendientes avisa de que no los hay
        print("No hay ningun pendiente\n")
        return

    # Busca los pendientes de la materia elegida y los muestra
    pendientes = data["pendientes"][mats[op]]
    print("\n".join(["- "+i for i in pendientes])+"\n")

def crearPendientes(data: dict, mats: list[str]):
    """
    Crea un pendiente nuevo.

    Parameters:
        data: son los datos guardados
        mats: son las materias registradas
    """

    # Te pide que elijas una materia
    print("Seleccione la materia del pendiente")
    mostrarOpciones(mats, False)
    op = pedirOpcion(1,len(mats))-1

    # Si la materia no esta inicializada, se inicializa
    if not mats[op] in data["pendientes"]:
        data["pendientes"][mats[op]] = []

    # Te pide que insertes el nuevo pendiente
    pendiente = pedirOpcionStr("Inserte el pendiente\n>> ")

    # Y agrega el nuevo pendiente
    data["pendientes"][mats[op]].append(pendiente)

    print("") # Muestra un salto de linea

def modificarPendientes(data: dict, mats: list[str]):
    """
    Modifica un pendiente existente.

    Parameters:
        data: son los datos guardados
        mats: son las materias registradas
    """

    # Te pide que elijas una materia
    print("Seleccione la materia del pendiente")
    mostrarOpciones(mats, False)
    op = pedirOpcion(1,len(mats))-1

    # Te pide que elijas un pendiente
    pendientes = data["pendientes"][mats[op]]
    print("Seleccione el pendiente")
    mostrarOpciones(pendientes)
    penop = pedirOpcion(1,len(pendientes))-1

    # Te pide que insertes el nuevo pendiente
    pendiente = pedirOpcionStr("Inserte el pendiente\n>> ")

    # Modificar el viejo pendiente al nuevo
    data["pendientes"][mats[op]][penop] = pendiente

def eliminarPendientes(data: dict, mats: list[str]):
    """
    Elimina un pendiente.

    Parameters:
        data: son los datos guardados
        mats: son las materias registradas
    """

    # Te pide que elijas una materia
    mostrarOpciones(mats, False)
    print("Seleccione la materia del pendiente")
    op = pedirOpcion(1,len(mats))-1

    # Te pide que elijas un pendiente
    pendientes = data["pendientes"][mats[op]]
    print("Seleccione el pendiente")
    mostrarOpciones(pendientes)
    penop = pedirOpcion(1,len(pendientes))-1

    # Borra el pendiente
    _ = data["pendientes"][mats[op]].pop(penop)

    # Si la materia no tiene ningun pendiente es borrada
    if len(data["pendientes"][mats[op]]) == 0:
        _ = data["pendientes"].pop(mats[op])

def manejarPendientes(data: dict, mats: list[str]):
    """
    Muestra todas las opciones
    disponibles conforme al
    manejo de pendientes.

    Parameters:
        data: son los datos guardados
        mats: son las materias registradas
    """

    # Muestra las opciones disponibles
    mostrarOpciones([
        "Ver pendientes",
        "Crear pendientes",
        "Modificar pendientes",
        "Eliminar pendientes",
        "Cancelar"
    ])

    op = pedirOpcion(1,5)
    
    if op == 1: # Si se eligio 1 se ven los pendientes
        verPendientes(data)
    elif op == 2: # Si se eligio 2 se crea un pendiente
        crearPendientes(data,mats)
    elif op == 3: # Si se eligio 3 se modifica un pendiente
        modificarPendientes(data, mats)
    elif op == 4: # Si se eligio 4 se elimina un pendiente
        eliminarPendientes(data, mats)