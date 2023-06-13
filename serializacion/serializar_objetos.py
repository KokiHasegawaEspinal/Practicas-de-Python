import pickle

class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False

    def arrancar (self):
        self.enMarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: " , self.frena)


carro1=Vehiculo("Mazda","CX5")
carro2=Vehiculo("Mercedez","c180")
carro3=Vehiculo("Audi","Q9")

carros=[carro1,carro2,carro3]

fichero=open("losCarros","wb")

pickle.dump(carros,fichero)

fichero.close()

del(fichero)

ficheroApertura=open("losCarros","rb")

miscarros=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in miscarros:

    print("\n",c.estado(),"\n")




