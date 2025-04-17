from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("600x200")
root.resizable(False, False)    # Prevent resizing of the window

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("Helvetica", 48), bg="black", fg="cyan")
label.pack(anchor="center")                                                          
time()   # Call the function to display the time

root.mainloop()