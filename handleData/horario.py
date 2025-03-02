from handleOptions import pedirOpcion, mostrarOpciones, pedirOpcionStr, pedirVariasOpcionesStr

def verHorario(data: dict):
    """
    Muestra el horario guardado

    Parameters:
        data: son los datos guardados
    """

    for i in data["horario"]: # Revisa cada semana
        print(f"{i}:")
        for j in data["horario"][i]: # Revisa las horas
            print(f"    {j}")
        print("") # Salto de linea

def agregarSemana(data: dict):
    """
    Agrega un dia de la semana
    al horario y sus materias
    correspondientes.

    Tambien puede modificar un
    dia de la semana como
    consecuencia del uso de dicts.

    Parameters:
        data: son los datos guardados
    """
    # Pide el dia de la semana
    dia = pedirOpcionStr("Inserte el dia de la semana\n>> ")

    if dia in data["horario"]:
        print("Este dia de la semana ya sido registrado!")
        return

    print("Inserte hora y materia por bloque")
    print("Presione Ctrl+C cuando este listo")

    # Pide las materias impartidas en ese dia
    horas = pedirVariasOpcionesStr()

    # Agrega las materias al determinado dia
    # Permite que que la funcion tambien sirva
    # para modificar un dia de la semana
    data["horario"][dia] = horas

def modificarSemana(data: dict[str,dict[str,list] | list]):
    """
    Modifica un dia de la semana ya existente

    Parametros:
        data: Son los datos guardados
    """

    # Pide un dia de la semana
    mostrarOpciones(data["horario"].keys())

    op = pedirOpcion(1,len(data["horario"]))-1
    if op == -2:
        print("No hay ningun dia de la semana resgistrado!")
        return
    
    print("Inserte horas y materias por bloque del dia correspondiente")
    print("Presione Ctrl+C cuando este listo")

    # Pide las materias impartidas en ese dia
    horas = pedirVariasOpcionesStr()

    # Se asignan las horas al dia de la semana elegido
    data["horario"][data["horario"].keys()[op]] = horas

def borrarSemana(data: dict[str,dict]):
    """
    Borra un dia de la semana
    del horario

    Parameters:
        data: son los datos guardados
    """
        
    # Pide el dia de la semana
    mostrarOpciones(data["horario"].keys())

    op = pedirOpcion(1,len(data["horario"]))-1
    if op == -2:
        print("No hay ningun dia de la semana resgistrado!")
        return

    # Borra el dia de la semana
    _ = data["horario"].pop(data["horario"].keys()[op])

def manejarHorario(data: dict):
    """
    Muestra el horario guardado

    Parameters:
        data: son los datos guardados
    """

    # Muestra las opciones
    mostrarOpciones([
        "Ver horario",
        "Agregar semana",
        "Modificar semana",
        "Borrar semana",
        "Cancelar"
    ])

    op = pedirOpcion(1,5)

    if op == 1: # Si se eligio 1 se ve el horario
        verHorario(data)
    elif op == 2: # Si se eligio 2 se agrega un dia de la semana
        agregarSemana(data)
    elif op == 3:
        modificarSemana(data)
    elif op == 4: # si se eligio 3 se borra un dia de la semana
        borrarSemana(data)