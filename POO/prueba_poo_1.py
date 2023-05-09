# video 26


# clase
class Carro():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enMarcha=False

# metodo
    def arrancar(self):
        self.enMarcha=True     

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


