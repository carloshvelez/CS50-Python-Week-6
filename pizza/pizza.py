import sys
from tabulate import tabulate
import csv

def main():

    if len(sys.argv) != 2:
        sys.exit("Se debe ingresar exactamente un comando")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Es necesario que ingrese un archivo CSV")

    print (embellecer_tabla(sys.argv[1]))

def embellecer_tabla(ruta_archivo_csv):

    filas = []
    with open(ruta_archivo_csv) as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            filas.append(fila)
        return tabulate(filas, headers="firstrow", tablefmt="grid")


if __name__ == "__main__":
    main()




