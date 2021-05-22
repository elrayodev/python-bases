from tkinter import *

# Configuracion de la raiz
root = Tk()
"""
# Variables dinamicas
texto = StringVar()
texto.set("Ich esse einen Apfel")


Label(root, text="Primera Etiqueta").pack(anchor="nw")
label = Label(root, text="Segunda Etiqueta")
label.pack()
Label(root, text="Tercera Etiqueta").pack(anchor="se")

label.config(bg="green", fg="white", font=("Verdana",24))
label.config(textvariable=texto)
"""

imagen = PhotoImage(file="imagen.gif")

Label(root, image=imagen, bd=0).pack(side="left")

# Bucle de la aplicación
root.mainloop()