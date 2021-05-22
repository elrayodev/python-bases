from tkinter import *

root = Tk()

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="disabled")

label = Label(root, text="Nombre muy largo: ")
label.grid(row=0, column=0, sticky="e", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="left")

label2 = Label(root, text="Apellidos: ")
label2.grid(row=1, column=0, sticky="e", padx=5, pady=5)

entry3 = Entry(root)
entry3.grid(row=2, column=1, padx=5, pady=5)
entry3.config(justify="center", show="*")

label3 = Label(root, text="Contraseña: ")
label3.grid(row=2, column=0, sticky="e", padx=5, pady=5)

root.mainloop()