# ejercicio_dos
# Área del círculo


import math
class Circulo():
      
      def area(self,r):
            print ("Area del circulo:")
            print(3.1416*math.pow(r,2))

ar = Circulo()
n1 = int(input("Teclea el radio del círculo: "))
ar.area(n1)
