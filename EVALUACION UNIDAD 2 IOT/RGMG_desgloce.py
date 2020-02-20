#EJERCICIO 17 DESGLOCE DE IVA
#MIRIAM RAMIREZ GLORIA

class IVA():
    
    def iva(self,cantidad):
        inicial=cantidad
        ivaTotal=(cantidad*0.16)
        sobrante = (cantidad-ivaTotal)
        
        print("Cantidad inicial es: $" +str(inicial))
        print("Importe IVA: $"+str(ivaTotal))
        print("Cambio: $"+str(sobrante))
    

iv = IVA()   
cantidad = float(input("Ingresa tu cantidad de dinero: $"))
iv.iva(cantidad)
