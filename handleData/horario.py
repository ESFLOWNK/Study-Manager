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

    print("Inserte hora y materia por bloque")
    print("Presione Ctrl+C cuando este listo")

    # Pide las materias impartidas en ese dia
    horas = pedirVariasOpcionesStr()

    # Agrega las materias al determinado dia
    # Permite que que la funcion tambien sirva
    # para modificar un dia de la semana
    data["horario"][dia] = horas

def borrarSemana(data: dict):
    """
    Borra un dia de la semana
    del horario

    Parameters:
        data: son los datos guardados
    """
        
    # Pide el dia de la semana
    dia = pedirOpcionStr("Inserte el dia de la semana\n>> ")

    # Borra el dia de la semana
    _ = data["horario"].pop(dia)

def manejarHorario(data: dict):
    """
    Muestra el horario guardado

    Parameters:
        data: son los datos guardados
    """

    # Muestra las opciones
    mostrarOpciones([
        "Ver horario",
        "Agregar o modificar semana",
        "Borrar semana",
        "Cancelar"
    ])

    op = pedirOpcion(1,4)

    if op == 1: # Si se eligio 1 se ve el horario
        verHorario(data)
    elif op == 2: # Si se eligio 2 se agrega un dia de la semana
        agregarSemana(data)
    elif op == 3: # si se eligio 3 se borra un dia de la semana
        borrarSemana(data)