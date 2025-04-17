from tkinter import *
root = Tk()
root.config(background='aquamarine')
root.geometry('600x600')

Dune = Spinbox(root, from_=0, to=100, width=5)
Dune.pack()

root.mainloop()


