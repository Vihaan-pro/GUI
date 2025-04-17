from tkinter import *

root = Tk()
root.geometry('400x400')

# Top button
button_top = Button(root, text='Top', borderwidth=5, background='green')
button_top.pack(side='top')

# Bottom button
button_bottom = Button(root, text='Bottom', borderwidth=5, background='blue')
button_bottom.pack(side='bottom')

# Left button
button_left = Button(root, text='Left', borderwidth=5, background='red')
button_left.pack(side='left')

# Right button
button_right = Button(root, text='Right', borderwidth=5, background='yellow')
button_right.pack(side='right')

root.mainloop()