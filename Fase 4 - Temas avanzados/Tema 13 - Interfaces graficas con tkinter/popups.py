from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

# Conf de la raiz
root = Tk()

def test():
	# MessageBox.showinfo("Hola","Hola Mundo")
	# MessageBox.showwarning("Alerta","Sección sólo para administradores")
	# MessageBox.showerror("Error","Hola Mundo")
	# result = MessageBox.askquestion("Salir","¿Está seguro que desea salir sin guardar?")
	# if result == "yes":
	#	root.destroy()

	# color = ColorChooser.askcolor(title="Elige un color")
	# print(color)

	# ruta = FileDialog.askopenfilename(title="Abrir un Fichero", initialdir="C:/Users/polo_/Desktop", # devuelve una ruta
	#	filetypes=(("Fichero de texto,","*.txt"),))
	# print(ruta)

	fichero = FileDialog.asksaveasfile(title="Guardar un Fichero", mode="a+", defaultextension=".txt") # equivale a open('ruta','w')
	if fichero is not None:
		fichero.write("Hola prro pto")
		fichero.close()
	

Button(root, text="Clickeame", command=test).pack()

root.mainloop()