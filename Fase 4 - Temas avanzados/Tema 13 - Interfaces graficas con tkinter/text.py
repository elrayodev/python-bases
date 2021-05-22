from tkinter import *

root = Tk()

frame = Frame(root, bg="black")
frame.pack()
frame.config(padx=5, pady=5)

texto = Text(frame)
texto.pack()
texto.config(width=30, height=10, font=("Consolas", 12), padx=15, pady=15, selectbackground="blue")


root.mainloop()