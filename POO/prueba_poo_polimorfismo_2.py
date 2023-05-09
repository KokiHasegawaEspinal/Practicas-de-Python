# video 32
# el metodo lo declaramos con "Def", el metodo en este caso es "desplazamiento" y el parametro va entre parentesis, en este caso es "self" y el comportamiento es lo que va a hacer. En este caso es lo que este dentro de "Print"

class Carro(): 
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Moto()

desplazamientoVehiculo(miVehiculo)


