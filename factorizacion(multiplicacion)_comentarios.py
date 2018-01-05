
def run():
    #2. Se solicita el numero, y se convierte este a entero
    number = int(input("escribe el numero que deseas evaluar: "))
    #3. Se pasa el numero por la función "numeroalcuadrado"
    #5. El resultado es guardado en la variable "result1"
    result1 = numeroalcuadrado(number)
    #6. El numero se imprime en la consola
    print("El numero multiplicado a cuadrado sería: {}".format(result1))
    #7. Despues el numero es ingresado a la función "facto"
    #11. El resultado es guardado en "result2"
    result2 = facto(number)
    #13.Se imprime el resultado en la consola
    print("El factorial del numero sería: {}".format(result2))

def facto(number):
    #8. Se revisa que el numero no sea cero, debido a que si es cero y se continua da un "error matemático"
    if number == 0:
        #9. El factorial de 0 es uno por lo que eso es lo que se devuelve si se da el caso
        return 1
    #10. En caso de que el numero sea diferente de 0, se multplica ese numero por el factorial del numero menos 1
    else:
        return number * facto(number - 1)

def numeroalcuadrado(number):
    #4. Multiplica el numero por si mismo y eso lo "devuelve"
    return number*number

if __name__ == "__main__":
    #1. Se verifica que el programa sea el principal, en caso de que así sea se ejecuta "run"
  run()
