# video 28


# clase
class Carro():
# declarando el metodo constructor
    def __init__(self):

        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enMarcha=False

# metodo
    def arrancar(self,arrancamos):
        self.__enMarcha=arrancamos

        if(self.__enMarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enMarcha and chequeo):
            return "El carro esta en marcha"

        elif(self.__enMarcha and chequeo==False):
           return "Ha ocurrido un problema, por favor verificar"

        else:
            return "El carro esta detenido"
            

    def estado(self):
        print("El carro tiene " , self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas") :

            return True

        else:
            return False





# objeto, instancia o ejemplar son lo mismo
miCarro=Carro() #instanciar una clase

print(miCarro.arrancar(True))

miCarro.estado()

# print(miCarro.estado())

print(".......A continuacion crearemos el segundo objeto.......")

miCarro2=Carro()

print(miCarro2.arrancar(False))

miCarro2.estado()
