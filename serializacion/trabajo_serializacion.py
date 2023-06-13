import pickle

# lista_nombres=["Pedro","Ana","Maria","Isabel"]

# fichero_binario=open("lista_nombres","wb")

# pickle.dump(lista_nombres,fichero_binario)   #volcar o ingresar los dartos a un archivo

# fichero_binario.close()

# del (fichero_binario)


# -----------------------

fichero=open("lista_nombres","rb")

lista=pickle.load(fichero)        #cargar los datos u obtenerlos desde un archivo

print(lista)