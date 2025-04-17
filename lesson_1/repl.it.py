from tkinter import *

root = Tk()
root.config(background='aquamarine')
root.geometry('600x600')

# "Pick a template" label and entry
label_template = Label(root, text="Pick a template", background='aquamarine')
label_template.place(x=150, y=100)
entry_template = Entry(root, borderwidth=5, background='yellow')
entry_template.place(x=300, y=100)

# "Name your project" label and entry
label_project = Label(root, text="Name your project", background='aquamarine')
label_project.place(x=150, y=150)
entry_project = Entry(root, borderwidth=5, background='yellow')
entry_project.place(x=300, y=150)

# "Create Repl" button
button_create = Button(root, text='Create Repl', borderwidth=5, background='green')
button_create.place(x=300, y=200)

root.mainloop()