from PIL import Image
from PIL import ImageOps
import os
import sys


def main():
    try:
        if len(sys.argv) != 3:  ## Salir si no son dos argumentos
            sys.exit("Se requieren exactamente tres argumentos")

        if os.path.splitext(sys.argv[1].lower())[1] not in (
            ".jpg",
            ".jpeg",
            ".png",
        ):  ##Salir si la extensión no es la indicada.
            sys.exit("No es una extensión válida")

        if (
            os.path.splitext(sys.argv[1].lower())[1]
            != os.path.splitext(sys.argv[2].lower())[1]
        ):  ## Salir si las extensiones de los argumentos no coinciden
            sys.exit("Las extensiones no coinciden")

        poner_camisa_cs50(sys.argv[1], sys.argv[2])

    except FileNotFoundError:
        sys.exit("El archivo no se encontró")


def poner_camisa_cs50(input, output):
    imagen1 = Image.open(input)  # Abrir el input
    camisa = Image.open("shirt.png")  # Abrir la camisa

    imagen4 = ImageOps.fit(
        imagen1, camisa.size
    )  # recordar el input según el tamaño de la camisa
    imagen4.paste(camisa, camisa)  # Poner la camisa.
    imagen4.save(output)


if __name__ == "__main__":
    main()
