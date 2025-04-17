# from tkinter import *
# from tkinter.ttk import Progressbar

# root = Tk()
# root.config(background='aquamarine')
# root.geometry('600x600')
# progress_bar = Progressbar(root, orient = HORIZONTAL, length = 100, mode = 'determinate')
# progress_bar.pack()

# def bar():
#     import time
#     progress_bar['value'] = 5
#     root.update_idletasks()
#     time.sleep(1)
#     progress_bar['value'] = 25
#     root.update_idletasks()
#     time.sleep(1)
#     progress_bar['value'] = 45
#     root.update_idletasks()
#     time.sleep(1)
#     progress_bar['value'] = 75
#     root.update_idletasks()
#     time.sleep(1)
#     progress_bar['value'] = 100

#     progress_bar(pady=10)
# Button(root, text='Start', command=progress_bar.start).pack(pady=10)
# root.mainloop()









# importing tkinter module
from tkinter import *
from tkinter.ttk import *
# creating tkinter window
root = Tk()
# Progress bar widget
progress = Progressbar(root, orient=HORIZONTAL,
                       length=100, mode='determinate')

# Function responsible for the updation
# of the progress bar value
def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100

progress.pack(pady=10)
# This button will initialize
# the progress bar
Button(root, text='Start', command=bar).pack(pady=10)
# infinite loop
mainloop()