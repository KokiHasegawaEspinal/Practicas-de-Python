from io import open


# -------------------------------------------
# se usa para escribir 
# archivo_texto=open("archivo.txt","w")
# frase="Estupendo dia para estudiar Python \n el miercoles"

# archivo_texto.write(frase)

# archivo_texto.close()

# ------------------------------------------
archivo_texto_1=open("archivo.txt","w")
frase_1="Voy a lograr ser un programador de Python en Japon"

archivo_texto_1.write(frase_1)

archivo_texto_1.close()

# ---------------------------------------

# se usa para leer el archivo
# archivo_texto=open("archivo.txt","r")

# texto=archivo_texto.read()

# archivo_texto.close()

# print(texto)
# ---------------------------------------
# convierte el archivo en una lista

# archivo_texto=open("archivo.txt","r")

# lineas_texto=archivo_texto.readlines()

# archivo_texto.close()

# print(lineas_texto[0:2])

# -------------------------------
archivo_texto=open("archivo.txt","a")

archivo_texto.write("\n Seguire adelante con mis sueños")

archivo_texto.close()


# ---------------------------------

# archivo_texto_1=open("archivo.txt","r")

# archivo_texto_1.seek(10)       #nos permite leer el archivo desde la letra N_11

# print(archivo_texto_1.read(10))   #nos permite leer el archivo hasta la letra N_10


# archivo_texto_1=open("archivo.txt","r")

# archivo_texto_1.seek(len(archivo_texto_1.read())/2)

# print(archivo_texto_1.read())

# ----------------------------------------

# archivo_texto_1=open("archivo.txt","r")

# archivo_texto_1.seek(len(archivo_texto_1.readline()))

# print(archivo_texto_1.read())

# -----------------------------

archivo_texto_1=open("archivo.txt","r+")   #modo lectura y escritura

archivo_texto_1.seek(len(archivo_texto_1.readline()))

print(archivo_texto_1.read())