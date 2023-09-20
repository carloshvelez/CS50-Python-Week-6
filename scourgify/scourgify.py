import sys
import csv


def main():

    if len(sys.argv) != 3:
        sys.exit ("Se requieren exactamentes tres argumentos")

    if not sys.argv[1].endswith(".csv"):
        sys.exit ("Se requiere un archivo con extensión .csv")

    crear_nuevo_archivo(sys.argv[1], sys.argv[2])


def crear_nuevo_archivo(antes, despues):


    nuevo_archivo = []

    with open(antes) as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            last, first  = fila["name"].split(", ")
            house = fila["house"]
            nueva_fila = {"last" : last, "first" : first, "house": house}
            nuevo_archivo.append(nueva_fila)




    with open(despues, "w") as output:
        writer = csv.DictWriter(output, fieldnames=[ "first", "last", "house"])
        writer.writeheader()
        for fila in nuevo_archivo:
            writer.writerow({"first": fila["first"], "last":fila["last"], "house": fila["house"]})


if __name__ == "__main__":
    main()

