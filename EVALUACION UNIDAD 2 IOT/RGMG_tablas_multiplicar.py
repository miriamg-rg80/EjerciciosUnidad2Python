#EJERCICIO 34 TABLAS DE MULTIPLICAR
#MIRIAM RAMÍREZ GLORIA - GDS0152

class Tabla(): #CLASE
    def tabla(self,numero): #METODO
        # Tablas hasta 10
        LIMITE = 10

        contador = 1
        while contador <= LIMITE:
            resultado = contador * numero
            print("{} x {} = {}".format(numero, contador, resultado))

            contador = contador + 1

#INSTANCIA
tab=Tabla()
r = int(input("Imprimir todas las tablas? 1 = Si, 2 = No "))

print('Tabla del 1')
tab.tabla(1)    #INSTANCIA.METODO
print('Tabla del 2')
tab.tabla(2)
print('Tabla del 3')
tab.tabla(3)
print('Tabla del 4')
tab.tabla(4)
print('Tabla del 5')
tab.tabla(5)
print('Tabla del 6')
tab.tabla(6)
print('Tabla del 7')
tab.tabla(7)
print('Tabla del 8')
tab.tabla(8)
print('Tabla del 9')
tab.tabla(9)
print('Tabla del 10')
tab.tabla(10)
