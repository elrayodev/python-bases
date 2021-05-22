from tkinter import *

root =  Tk()

root.title("Hola Mundo")
root.resizable(1,1)
root.iconbitmap('hola.ico')

frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")

frame2 = Frame(root, width=480, height=320)
frame2.pack(fill='both', expand=1)
frame2.config(cursor="pirate")
frame2.config(bg="red")
frame2.config(bd=25)
frame2.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

# Abajo del todo
root.mainloop()