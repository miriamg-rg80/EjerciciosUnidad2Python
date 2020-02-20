#EJERCICIO 27 INICIALES AL REVES
#MIRIAM RAMÍREZ GLORIA - GDS0152

class Frase():
    
    def invertir(self):
        frase = input ("Ingresa una palabra: ")
        frase = frase[::-1]
        print (frase)

fra = Frase()
fra.invertir()
