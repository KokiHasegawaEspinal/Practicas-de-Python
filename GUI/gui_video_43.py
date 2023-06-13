from tkinter import*

raiz=Tk()

raiz.title("Ventana de Pruebas")

raiz.iconbitmap("#")

raiz.config(bg="blue")

raiz.config(bd=45)

raiz.config(relief="groove")

raiz.config(cursor="hand2")




miFrame=Frame()

#miFrame.pack(side="left", anchor="s") #se ancla al sur de la pagina

#miFrame.pack(fill="x") #se expande horizontalmente en el eje de las x

#miFrame.pack(fill="y", expand="True") # se mantiene en el eje de las y

#miFrame.pack(fill="both", expand="True")

miFrame.pack()

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

miFrame.config(bd=35)

#miFrame.config(relief="groove")

miFrame.config(relief="sunken")

#miFrame.config(cursor="hand2")

miFrame.config(cursor="pirate")

raiz.mainloop()