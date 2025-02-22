def pedirOpcion(desde: int,hasta: int) -> int:
    op = "" # Crea una variable que contiene las opciones ingresadas
    if hasta == 0: # Si desde y hasta son 0
        return -1        # Devuelve -1
    while not op in [str(i) for i in range(desde,hasta+1)]:
        # Revisa que op sea digitos y que sea mayor que 0 o menor que 4
        # De no ser asi se repite el proceso

        op = input(">> ")

    return int(op) # Devuelve la opcion a manera de int


def pedirOpcionStr(text: str = ">> ") -> str:
    op = "" # Crea una variable que contiene las opciones ingresadas
    while "|" in op or "." in op or "-" in op or op.strip() == "":
        # Revisa que op no tenga caracteres especiales
        op = input(text)

    return op # Devuelve la opcion a manera de int


def mostrarOpciones(opciones: list[str], header = True):
    if header: print("Opciones:\n")

    for i in range(0,len(opciones)): # Hace que la variable i vaya desde cero hasta
                                     # el numero de elementos que tiene opciones, en bucle

        print(f"{i+1}. {opciones[i]}") # Se imprime i+1 y la opcion actual
    
    print("") # Hace un salto de linea

def pedirVariasOpcionesStr(text:str = ">> ") -> list[str]:
    ops = [] # Crea la lista de textos
    op = "" # Crea una variable temporal para guardar texto

    try: # Pide texto hasta que se presiona Ctrl + C
        while True:
            pedirOpcionStr(text)
            ops.append(op)
    except KeyboardInterrupt:
        pass

    return ops