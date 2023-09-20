import sys

def main():

    try:
        if len(sys.argv) != 2:
            sys.exit("Se requiere exactamente un parámetro")
        elif not sys.argv[1].endswith(".py"):
            sys.exit("Not a python file")

        print(contar_lineas(sys.argv[1]))

    except FileNotFoundError:
            sys.exit("No se encuentra el archivo")

def contar_lineas(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()

    contador_lineas = 0
    for linea in lineas:
        if linea.lstrip().startswith("#"):
            continue
        elif linea.isspace():
            continue
        else:
            contador_lineas += 1

    return contador_lineas




if __name__ == "__main__":
    main()


