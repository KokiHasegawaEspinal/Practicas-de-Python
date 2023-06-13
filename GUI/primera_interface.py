from tkinter import*

raiz=Tk()

raiz.title("Ventana de Pruebas")

#raiz.wm_resizable(1,0)  #(widh, heigh) 0= False, no se puede alterar con el mouse

# buscar conversor.ico en google
raiz.iconbitmap("#") #colocar una imagen

raiz.geometry("650x350") #medidas de la ventana

raiz.config(bg="blue") #cambiar el background
raiz.config(bd=45)
raiz.config(relief="groove")
raiz.config(cursor="pirate")




miFrame=Frame()

miFrame.pack()
#miFrame.pack(fill="both",expand="True") #para expandir horizontal y verticalmente

#miFrame.pack(side="right", anchor="s")

miFrame.config(bg="red")
miFrame.config(width="650",height="350")
miFrame.config(bd=35)  #para cambiar el grosor del borde
#miFrame.config(relief=)

#miFrame.config(relief="groove") #para cambiar el borde
miFrame.config(relief="sunken")

miFrame.config(cursor="hand2")
#miFrame.config(cursor="pirate")



raiz.mainloop()