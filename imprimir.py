import sys
import time
def imprimir(cadena):
    for letter in cadena:
        sys.stdout.write(letter)
        time.sleep(.05)


def imprimeEntreLineas(frase):
    print('+------------------------------------+\n')
    imprimir(frase+"\n")
    print("+------------------------------------+")
