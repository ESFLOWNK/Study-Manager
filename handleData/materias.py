from handleOptions import mostrarOpciones, pedirOpcion, pedirOpcionStr

def verMaterias(materias: list[str]):
    # Muestra las materias
    print("\n".join([f"- {i}" for i in materias]))

def agregarMateria(materias: list[str]):
    # Pide el nombre de la materia
    mat = pedirOpcionStr("Inserte el nombre de la materia\n>> ")

    # Agrega la materia
    materias.append(mat.title())

def modificarMateria(materias: list[str]):
    # Muestra las materias
    mostrarOpciones(materias)

    # Pide que elijas una materia
    op = pedirOpcion(1,len(materias))-1

    # Pide el nuevo nombre de la materia
    mat = pedirOpcionStr("Inserte la materia\n>> ")

    # Realiza la modificacion
    materias[op] = mat

def borrarMateria(materias: list[str]):
    # Pide que se elija una materia
    print("Eliga la materia a borrar:")
    mostrarOpciones(materias, False)
    op = pedirOpcion(1,len(materias))-1

    # Se borra la materia
    materias.pop(op)

def configurarMaterias(materias: list[str]):
    mostrarOpciones([
        "Ver materias",
        "Agregar materia",
        "Modificar materia",
        "Borrar materia",
        "Cancelar"
    ])

    op = pedirOpcion(1,5)

    if op == 1:
        verMaterias(materias)
    elif op == 2:
        agregarMateria(materias)
    elif op == 3:
        modificarMateria(materias)
    elif op == 4:
        borrarMateria(materias)