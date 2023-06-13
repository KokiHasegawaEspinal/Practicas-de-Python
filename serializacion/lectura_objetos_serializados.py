import pickle


#no podemos usarlo de esta forma. video N 40



ficheroApertura=open("losCarros","rb")

miscarros=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in miscarros:

    print("\n",c.estado(),"\n")
