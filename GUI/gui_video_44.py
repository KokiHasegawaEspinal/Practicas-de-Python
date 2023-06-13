from tkinter import*

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()


# ---------------------------------------
#miLabel=Label(miFrame, text="Hola alumnos de Python")
#miLabel.pack() # debemos usar el metodo "place" para ubicarlo en las coordenadas que le indiquemos

#miLabel.place(x=100, y=200)

#si queremos abreviar el codigo podemos hacerlo de la siguiente manera:

#Label(miFrame, text="Hola alumnos de Python", fg="red", font=("Comic sans MS", 34)).place(x=100,y=200)

# ------------------------------------

miImagen=PhotoImage(file="gato_programer.gif")

Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()