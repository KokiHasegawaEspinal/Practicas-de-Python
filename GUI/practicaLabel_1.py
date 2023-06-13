from tkinter import*

root=Tk()

miFrame=Frame(root, width=500, height=400)
miFrame.pack()

miLabel=Label(miFrame, text="Hola alumnos de Python")

miLabel.place(x=100,y=200) #coordenadas desde el borde de arriba y desde el borde izquierda en pixeles

#miLabel=Label(miFrame, text="Hola alumnos de Python")
Label(miFrame, text="Hola alumnos de Python", fg="red", font=("Comic Sans MS",20)).place(x=100,y=200) #se usa para no usar muchas variables y abreviar el codigo
#miLabel.place(x=100,y=200)





root.mainloop()