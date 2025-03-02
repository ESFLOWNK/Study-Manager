def pedirOpcion(desde: int,hasta: int) -> int:
    """
    Pide al usuario ingresar un numero
    entre `desde` y `hasta`.

    Continuara pidiendelo mientras se
    den datos incorrectos.

    Parameters:
        desde: es el numero minimo (inclusive)
               que se puede ingresar
        hasta: es el numero maximo (inclusive)
               que se puede ingresar
    """

    op = "" # Crea una variable que contiene las opciones ingresadas
    if hasta == 0: # Si desde y hasta son 0
        return -1  # Devuelve -1
    while True:
        # Revisa que op sea digitos y que sea mayor que 0 o menor que 4
        # De no ser asi se repite el proceso

        op = input(">> ")

        if op.isdigit() and int(op) >= desde and int(op) <= hasta:
            break
        else:
            print("Insertaste un valor incorrecto")

    return int(op) # Devuelve la opcion a manera de int


def pedirOpcionStr(text: str = ">> ") -> str:
    """
    Pide un texto, se volvera a pedir
    mientras se ingresen datos con
    caracteres invalidos.

    Parameters:
        text: Es el texto mostrado antes
              de pedir texto al usuario
    """
    op = "" # Crea una variable que contiene las opciones ingresadas
    while "." in op or "-" in op or op.strip() == "":
        # Revisa que op no tenga caracteres especiales
        op = input(text)
        if "." in op or "-" in op or op.strip() == "":
            print("El texto contiene caracteres invalidos!")

    return op # Devuelve la opcion a manera de int


def mostrarOpciones(opciones: list[str], header = True):
    """
    Muestra una lista de opciones de
    manera enumerada.

    Parameters:
        opciones: Es la lista de opciones
                  que van a ser mostradas
        header: Si es verdadero mostrara
                la cabezera antes de
                mostrar las opciones
    """

    if header: 
        print("Opciones:\n")

    for i in range(0,len(opciones)): # Hace que la variable i vaya desde cero hasta
                                     # el numero de elementos que tiene opciones, en bucle

        print(f"{i+1}. {opciones[i]}") # Se imprime i+1 y la opcion actual
    
    print("") # Hace un salto de linea

def pedirVariasOpcionesStr(text:str = ">> ") -> list[str]:
    """
    Pide texto al usuario hasta que
    se presione la combinacion de
    teclas `Ctrl + C`

    Parameters:
        text: Es el texto mostrado antes
              de pedir texto al usuario
    """

    ops = [] # Crea la lista de textos
    op = "" # Crea una variable temporal para guardar texto

    try: # Pide texto hasta que se presiona Ctrl + C
        while True:
            op = pedirOpcionStr(text)
            ops.append(op)
    except KeyboardInterrupt:
        # Si se presiona Ctrl + C se entrara aqui
        print("") # Salto de linea
        pass

    return ops