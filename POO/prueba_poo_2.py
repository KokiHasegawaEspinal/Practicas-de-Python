# video 27


# clase
class Carro():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enMarcha=False

# metodo
    def arrancar(self,arrancamos):
        self.enMarcha=arrancamos

        if(self.enMarcha):
            return "El carro esta en marcha"

        else:
            return "El carro esta detenido"
            

    def estado(self):
        if(self.enMarcha):
            return "El carro esta en marcha"

        else:

            return "El carro esta detenido"

# objeto, instancia o ejemplar

miCarro1=Carro() #instanciar una clase

print(miCarro1.largoChasis)

print("El largo del carro 1 es ",miCarro1.largoChasis, "centimetros")
print("El carro 1 tiene ",miCarro1.ruedas," ruedas")
print(miCarro1.arrancar())

print(miCarro1.estado())

print(".......A continuacion crearemos el segundo objeto.......")

miCarro2=Carro()
print("El largo del carro 2 es ",miCarro2.largoChasis, " centimetros")
print("El carro 2 tiene ",miCarro2.ruedas, "ruedas")
print(miCarro2.estado())
