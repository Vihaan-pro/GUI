from tkinter import *
root = Tk()
root.config(background='aquamarine')
root.geometry('400x400')

# button with a border
button = Button(root, text='Click me!', borderwidth=5,background='green')
button.pack(side= 'top')
root.mainloop()