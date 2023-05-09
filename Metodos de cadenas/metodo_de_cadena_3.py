edad=input("Introduce una edad: ")

while (edad.isdigit()==False):
    print("Por favor, introduce un valor numerico")

    edad=input("Introduce una edad: ")

if (int(edad)<18):
    print("No puede pasar")

else:
    print("Puede pasar")