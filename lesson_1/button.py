from tkinter import *

root = Tk()
root.config(background='aquamarine')
root.geometry('400x400')

# button with a border
button = Button(root, text='Click me!', borderwidth=5, background='green')
button.pack(side='top')

# entry box
entry = Entry(root, borderwidth=5, background='yellow')
entry.place(x=100, y=100)

# label
label = Label(root, text='Hello World!', borderwidth=5, background='red')
label.place(x=100, y=150)

root.mainloop()