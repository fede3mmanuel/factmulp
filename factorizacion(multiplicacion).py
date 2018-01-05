
def run():
    number = int(input("escribe el numero que deseas evaluar: "))
    result1 = numeroalcuadrado(number)
    print("El numero multiplicado a cuadrado sería: {}".format(result1))
    result2 = facto(number)
    print("El factorial del numero sería: {}".format(result2))

def facto(number):
    if number == 0:
        return 1
    else:
        return number * facto(number - 1)

def numeroalcuadrado(number):
    return number*number

if __name__ == "__main__":
  run()
