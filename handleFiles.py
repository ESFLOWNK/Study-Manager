# Funciones para la escritura y lectura de datos

def guardarDatos(filename: str,data: dict):
    f = open(filename,"w")
    for i in data:
        f.write(f"--{i}\r\n")
        for j in data[i]:
            f.write(f"-{j}\r\n")
            for k in data[i][j]:
                f.write(f"{k}\r\n")

    f.close()

def leerDatos(filename: str) -> dict:
    f = open(filename,"r")
    data = {}
    try:
        line = ""
        fatherScope = ""
        childScope = ""
        while (line := f.readline().replace("\n","").replace("\r","")):
            if line.strip() == "":
                continue

            elif line.startswith("--"):
                data[line[2:]] = {}
                fatherScope = line[2:]

            elif line.startswith("-"):
                data[fatherScope][line[1:]] = []
                childScope = line[1:]

            else:
                data[fatherScope][childScope].append(line)
    except FileNotFoundError:
        f.close()
        return {"pendientes":{},"horario":{{}}}

    f.close()
    return data


def leerMaterias(filename: str) -> list[str]:
    m = []

    f = open(filename,"r")
    # Se lee el archivo, y el contenido se corta por los |, por ejemplo 1|2|3 = 1, 2, 3
    m = f.readline().split("|")
    f.close()
    
    return m # Devuelve m la cual tiene las materias