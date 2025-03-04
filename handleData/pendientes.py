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
        # Avisa si no hay materias registradas
        print("No hay ninguna materia registrada!")
        return

    # Busca los pendientes de la materia elegida y los muestra
    pendientes = data["pendientes"][mats[op]]
    print("\n".join(["- "+i for i in pendientes])+"\n")

def crearPendientes(data: dict):
    """
    Crea un pendiente nuevo.

    Parameters:
        data: son los datos guardados
    """

    # Te pide que elijas una materia
    print("Seleccione la materia del pendiente")
    mostrarOpciones(data["materias"], False)
    op = pedirOpcion(1,len(data["materias"]))-1

    if op == -2:
        # Avisa si no hay materias registradas
        print("No hay ninguna materia resgistrada!")
        return

    # Si la materia no esta inicializada, se inicializa
    if not data["materias"][op] in data["pendientes"]:
        data["pendientes"][data["materias"][op]] = []

    # Te pide que insertes el nuevo pendiente
    pendiente = pedirOpcionStr("Inserte el pendiente\n>> ")

    # Y agrega el nuevo pendiente
    data["pendientes"][data["materias"][op]].append(pendiente)

    print("") # Muestra un salto de linea

def modificarPendientes(data: dict):
    """
    Modifica un pendiente existente.

    Parameters:
        data: son los datos guardados
    """

    # Te pide que elijas una materia
    print("Seleccione la materia del pendiente")
    mostrarOpciones(data["materias"], False)
    op = pedirOpcion(1,len(data["materias"]))-1

    if op == -2:
        # Avisa si no hay materias registradas
        print("No hay ninguna materia resgistrada!")
        return

    # Te pide que elijas un pendiente
    pendientes = data["pendientes"][data["materias"][op]]
    print("Seleccione el pendiente")
    mostrarOpciones(pendientes)
    penop = pedirOpcion(1,len(pendientes))-1

    if penop == -2:
        # Avisa si no hay pendientes registrados
        print("No hay ningun pendiente resgistrado!")
        return

    # Te pide que insertes el nuevo pendiente
    pendiente = pedirOpcionStr("Inserte el pendiente\n>> ")

    # Modificar el viejo pendiente al nuevo
    data["pendientes"][data["materias"][op]][penop] = pendiente

def eliminarPendientes(data: dict):
    """
    Elimina un pendiente.

    Parameters:
        data: son los datos guardados
    """

    # Te pide que elijas una materia
    mostrarOpciones(data["materias"], False)
    print("Seleccione la materia del pendiente")
    op = pedirOpcion(1,len(data["materias"]))-1

    if op == -2:
        # Avisa si no hay materias registradas
        print("No hay ninguna materia resgistrada!")
        return

    # Te pide que elijas un pendiente
    pendientes = data["pendientes"][data["materias"][op]]
    print("Seleccione el pendiente")
    mostrarOpciones(pendientes)
    penop = pedirOpcion(1,len(pendientes))-1

    if op == -2:
        # Avisa si no hay pendientes registrados
        print("No hay ningun pendiente resgistrado!")
        return

    # Borra el pendiente
    _ = data["pendientes"][data["materias"][op]].pop(penop)

    # Si la materia no tiene ningun pendiente es borrada
    if len(data["pendientes"][data["materias"][op]]) == 0:
        _ = data["pendientes"].pop(data["materias"][op])

def manejarPendientes(data: dict):
    """
    Muestra todas las opciones
    disponibles conforme al
    manejo de pendientes.

    Parameters:
        data: son los datos guardados
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
        crearPendientes(data)
    elif op == 3: # Si se eligio 3 se modifica un pendiente
        modificarPendientes(data)
    elif op == 4: # Si se eligio 4 se elimina un pendiente
        eliminarPendientes(data)