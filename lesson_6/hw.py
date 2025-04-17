from tkinter import *
from time import strftime
import random

root = Tk()
root.title("Digital Clock")
root.geometry("800x400")
root.resizable(False, False)    # Prevent resizing of the window

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    if random.choice([True, False]):
        label.config(fg=random_color())
    else:
        label.config(bg=random_color())
    label.after(1000, time)

# Adding a frame for better layout management
frame = Frame(root, bg="black")
frame.pack(expand=True, fill=BOTH)

title_label = Label(frame, text="My Digital Clock", font=("Helvetica", 36, "bold"), bg="black", fg="white")
title_label.pack(pady=20)

label = Label(frame, font=("Helvetica", 72, "bold"), bg="black", fg="cyan", relief="solid", bd=5)
label.pack(pady=20)

# Adding a footer label for additional elegance
footer_label = Label(frame, text="Stay on time, stay elegant", font=("Helvetica", 16, "italic"), bg="black", fg="white")
footer_label.pack(side=BOTTOM, pady=10)

time()   # Call the function to display the time

root.mainloop()