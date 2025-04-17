from tkinter import *

root = Tk()
root.config(background='aquamarine')
root.geometry('600x600')

# Username label and entry
label_username = Label(root, text="Username", background='aquamarine')
label_username.place(x=150, y=100)
entry_username = Entry(root, borderwidth=5, background='yellow')
entry_username.place(x=250, y=100)

# Password label and entry
label_password = Label(root, text="Password", background='aquamarine')
label_password.place(x=150, y=150)
entry_password = Entry(root, borderwidth=5, background='yellow', show='*')
entry_password.place(x=250, y=150)

# Submit button
button_submit = Button(root, text='Submit', borderwidth=5, background='green')
button_submit.place(x=250, y=200)

root.mainloop()