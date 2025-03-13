import tkinter as tk

from tkinter import messagebox
import random

root = tk.Tk()
root.title("Guess the Number")
root.geometry("400x200")

random_number = random.randint(1, 20)

def check_number():
    user_number = int(entry.get())
    if user_number == random_number:
        messagebox.showinfo("Congratulations", "You guessed the number correctly!")
    elif user_number < random_number:
        messagebox.showerror("Incorrect", "Try guessing a higher number.")
    else:
        messagebox.showerror("Incorrect", "Try guessing a lower number.")

label = tk.Label(root, text="Guess a number between 1 and 20:", font=("Helvetica", 16))
label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 16))
entry.pack(pady=10)

button = tk.Button(root, text="Check", font=("Helvetica", 16), command=check_number)
button.pack(pady=10)                                                
root.mainloop()
# In this snippet, we created a simple game called "Guess the Number". The game generates a random number between 1 and 20, and the player has to guess the number.
