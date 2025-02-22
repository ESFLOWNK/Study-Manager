from handleOptions import pedirOpcion, mostrarOpciones, pedirOpcionStr

def verPendientes(data: dict):
    # Obtiene todas las materias con pendientes
    mats = list(data["pendientes"].keys())

    # Muestra las materias y te pide que elijas una
    print("Seleccione la materia")
    mostrarOpciones(mats, False)
    op = pedirOpcion(1,len(mats))-1

    # Busca los pendientes de la materia elegida y los muestra
    pendientes = data["pendientes"][mats[op]]
    print("\n".join(["- "+i for i in pendientes])+"\n")

def crearPendientes(data: dict):
    # Obtiene las materias con pendientes
    mats = list(data["pendientes"].keys())

    # Te pide que elijas una
    print("Seleccione la materia del pendiente")
    mostrarOpciones(mats, False)
    op = pedirOpcion(1,len(mats))-1

    # Te pide que insertes el nuevo pendiente
    pendiente = pedirOpcionStr("Inserte el pendiente\n>> ")

    # Y agrega el nuevo pendiente
    data["pendientes"][mats[op]].append(pendiente)

    print("") # Muestra un salto de linea

def modificarPendientes(data: dict):
    # Obtiene las materias con pendientes
    mats = list(data["pendientes"].keys())

    # Te pide que elijas una
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

def eliminarPendientes(data: dict):
    # Obtiene todas las materias con pendientes
    mats = list(data["pendientes"].keys())

    # Te pide que elijas una
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

def manejarPendientes(data: dict):
    mostrarOpciones([
        "Ver pendientes",
        "Crear pendientes",
        "Modificar pendientes",
        "Eliminar pendientes"
    ])

    op = pedirOpcion(1,3)
    
    if op == 1:
        verPendientes(data)
    elif op == 2:
        crearPendientes(data)
    elif op == 3:
        modificarPendientes(data)
    elif op == 4:
        eliminarPendientes(data)