import pickle

class Persona:    #video 41

    def __init__(self, nombre, genero, edad):
        self.nombre=nombre 
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

    personas=[]

    def __init__(self):
        listaDePersonas=open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

        except:
            print("El fichero esta vacio")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        ListaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, ListaDePersonas)
        ListaDePersonas.close()
        del(ListaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)

miLista=ListaPersonas()

persona=Persona("Monica", "Femenino", 23)
miLista.agregarPersonas(persona)

# persona=Persona("Anuet", "Masculino", 39)
# miLista.agregarPersonas(persona)

# persona=Persona("Anabel", "Femenino", 19)
# miLista.agregarPersonas(persona)

miLista.mostrarPersonas()