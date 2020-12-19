import random
import json

class diccionario():

    def __init__(self):
        self.archivo = "diccionario.json"
        self.listaPalabras = json.load(open(self.archivo))
        self.categoria =""
        self.palabra =""

    

    def eligeCategoria(self):
        self.categoria = random.choice(list(self.listaPalabras.keys()))        

    def eligePalabra(self): 
        numPalabra = random.randint(0, len(self.listaPalabras[self.categoria]) - 1)
        self.palabra =  self.listaPalabras[self.categoria][numPalabra]    

    def cargaDiccionario(self):
        self.eligeCategoria()
        self.eligePalabra()

    def eligeLetra(self):
        letraCorrecta = False  
        while not letraCorrecta:
            letra = input('Adivina una letra o resuelve (re):') 
            if letra == "re":
                return "re"
            if len(letra) != 1:
                print("Solo se puede una letra a la vez")  
            else:
                if letra not in 'abcdefghijklmnopqrstuvwxyz':
                    print("Tiene que ser una letra del alfabeto")  
                else:
                    letraCorrecta = True     
        return letra