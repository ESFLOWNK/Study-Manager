from handleOptions import pedirOpcion, mostrarOpciones, pedirOpcionStr, pedirVariasOpcionesStr

def verHorario(data: dict):
    for i in data["horario"]: # Revisa cada semana
        print(f"{i}:")
        for j in data["horario"][i]: # Revisa las horas
            print(f"    {j}")
        print("") # Salto de linea

def agregarSemana(data: dict):
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
    # Pide el dia de la semana
    dia = pedirOpcionStr("Inserte el dia de la semana\n>> ")

    # Borra el dia de la semana
    _ = data["horario"].pop(dia)

def manejarHorario(data: dict):
    mostrarOpciones([
        "Ver horario",
        "Agregar o modificar semana",
        "Borrar semana",
        "Cancelar"
    ])

    op = pedirOpcion(1,4)

    if op == 1:
        verHorario(data)
    elif op == 2:
        agregarSemana(data)
    elif op == 3:
        borrarSemana(data)