import random
import imprimir as im 
import diccionario as d
from marcador import marcador 
import os # Para borrar la pantalla        




dic = d.diccionario()
marc = marcador()



def resolver(palabraSecreta):
  
  palabraResuelta = input("¿Cual es la palabra?")
  if palabraResuelta == palabraSecreta:
    input("¡Enhorabuena, has resuelto la palabra! ")
    return True    
  else:
    input("Esa no es la palabra secreta")
    return False

def jugarOtra():
  eleccion = False 
  while not eleccion:
    otra = input('¿Quieres jugar otra partida? (Sí o no)')
    if otra.lower().startswith('s'):
      return True
   


def mostrarNormas():
  im.imprimir("Cada letra acertada da 10 puntos\n")
  im.imprimir("Cada letra fallada resta 5 puntos\n")
  im.imprimir("Si resuelves la palabra antes de terminar, ganarás 20 puntos por cada letra que quede\n")
  im.imprimir("Sin embargo, si fallas al resolver, se te restarán los mismos puntos\n")
  im.imprimir("Pedir una vocal te costará 30 puntos\n")


AHORCADO ="AHORCADO"
juegoNuevo = True
# Lista de las letras

nombreJugador = input("Bienvenido al ahorcado, ¿cómo te llamas?")
input(f"hola {nombreJugador}, vamos a jugar al ahorcado")

if input("¿Conoces las normas <s/n>?") == "no":
  mostrarNormas()

marc.puntos = 50
puntosVocal = 30

while juegoNuevo:

  letraIncorrecta = []
  letraCorrecta = [] 

  dic.cargaDiccionario()  
  palabraSecreta = dic.palabra

  longitudPalabra = len(palabraSecreta)

  print ('A H O R C A D O')

  juegoTerminado = False
  
  while (not juegoTerminado) and marc.quedanPuntos():
      
      _ = os.system('cls')    
          
      # Mostrar las letras incorrectas

      print(f"Puntos {nombreJugador}: {marc.getPuntos()}\n")

      print ('\nLetras incorrectas: ', end = '')
      for letra in letraIncorrecta:
          print (letra, end = '') 
      print ("")
      
      # Creamos un string con todo "_"  

      espacio = '_' * longitudPalabra
      for i in range(longitudPalabra): # Remplaza los espacios en blanco por la letra bien escrita
          if palabraSecreta[i] in letraCorrecta:
              espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]

      print(f"La categoria es {dic.categoria.upper()} ")
      # Mostramos la palabra como está ahora

      for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
          print (letra+" ", end = '')
      print ("")
      
      # Elegir una letra
      
      
      letra = dic.eligeLetra()
      
      if letra == "re":
        resuelto = resolver(palabraSecreta)
        letrasSobrantes = len(palabraSecreta) - len(letraCorrecta)
        puntosResolver = letrasSobrantes * 20
        if resuelto:
          juegoTerminado = True
          print(f"Has ganado {letrasSobrantes} x 20 puntos =  {puntosResolver}")
          marc.suma(puntosResolver)
          break
        else:          
          print(f"Has perdido {letrasSobrantes} x 20 puntos =  {puntosResolver}")
          marc.resta(puntosResolver)
          break
      else:
        if letra in "aeiou":
          im.imprimir(f"Comprar vocal: -{puntosVocal}")          
          marc.resta(puntosVocal)      
        if letra in palabraSecreta:
          letraCorrecta.append(letra)          
          marc.suma(10)
          im.imprimir("La letra está en la palabra: +10 puntos")
          # Se fija si el jugador ganó
          letrasEncontradas = True
          for i in range(longitudPalabra):
              if palabraSecreta[i] not in letraCorrecta:
                  letrasEncontradas = False
                  break
          if letrasEncontradas:
              print ('¡Muy bien! La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
              juegoTerminado = True
        else:
          im.imprimir("La letra no está en la palabra: -5 puntos")
          marc.resta(5)
          if letra in letraIncorrecta:
            input ('Esta letra ya la habías dicho <pulsa enter>')
          else:
            letraIncorrecta.append(letra)
          # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
          if len(letraIncorrecta) == len(AHORCADO) - 1:            
              print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
              juegoTerminado = True
      

  juegoNuevo = jugarOtra()