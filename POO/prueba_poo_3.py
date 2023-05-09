# video 27


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
            return "El carro esta en marcha"

        else:
            return "El carro esta detenido"
            

    def estado(self):
        print("El carro tiene " , self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

# objeto, instancia o ejemplar son lo mismo

miCarro=Carro() #instanciar una clase

print(miCarro.arrancar(True))

miCarro.estado()

# print(miCarro.estado())

print(".......A continuacion crearemos el segundo objeto.......")

miCarro2=Carro()

print(miCarro2.arrancar(False))

miCarro2.__ruedas=5

miCarro2.estado()

