
def main():

    cantidad = convert(input("Fraction: "))
    print(gauge(cantidad))




def convert(fraccion):

    #try:
    x, y = fraccion.split("/")

    #except ValueError:
     #   raise ValueError

    if int(y) == 0:
       raise ZeroDivisionError

    if int(x) < int(y):
        return round((int(x) / int(y)) *100)

    else:
        raise ValueError

def gauge(fuel):

    if fuel >= 99:
        return "F"
    elif fuel <= 1:
        return "E"
    else:
        return f"{fuel}%"



if __name__ == "__main__":
    main()






