from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def add_book():
    book = book_entry.get()
    author = author_entry.get()
    year = year_spinbox.get()
    genre = genre_var.get()
    
    if book and author and year and genre:
        listbox.insert(END, f"{book} by {author} ({year}) - {genre}")
        book_entry.delete(0, END)
        author_entry.delete(0, END)
        year_spinbox.delete(0, END)
        year_spinbox.insert(0, 2025)
        genre_var.set("")
    else:
        messagebox.showwarning("Incomplete Information", "Please fill in all fields!")

root = Tk()
root.title("Library Management System")
root.geometry("600x600")
root.configure(bg="lightblue")

frame = Frame(root, bg="lightblue", padx=20, pady=20)
frame.pack(pady=20)

# Book title
book_label = Label(frame, text="Book Title:", bg="lightblue", fg="black", font=("Arial", 12, "bold"))
book_label.grid(row=0, column=0, sticky="w", pady=5)
book_entry = Entry(frame, width=30)
book_entry.grid(row=0, column=1, pady=5)

# Author
author_label = Label(frame, text="Author:", bg="lightblue", fg="black", font=("Arial", 12, "bold"))
author_label.grid(row=1, column=0, sticky="w", pady=5)
author_entry = Entry(frame, width=30)
author_entry.grid(row=1, column=1, pady=5)

# Year
year_label = Label(frame, text="Year:", bg="lightblue", fg="black", font=("Arial", 12, "bold"))
year_label.grid(row=2, column=0, sticky="w", pady=5)
year_spinbox = Spinbox(frame, from_=1900, to=2025, width=28)
year_spinbox.grid(row=2, column=1, pady=5)

# Genre
genre_label = Label(frame, text="Genre:", bg="lightblue", fg="black", font=("Arial", 12, "bold"))
genre_label.grid(row=3, column=0, sticky="w", pady=5)
genre_var = StringVar()
genre_dropdown = ttk.Combobox(frame, textvariable=genre_var, values=["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery", "Biography"], width=27)
genre_dropdown.grid(row=3, column=1, pady=5)
genre_dropdown.current(0)

# Add book button
add_button = Button(frame, text="Add Book", command=add_book, bg="gray", fg="black", font=("Arial", 12, "bold"), width=20)
add_button.grid(row=4, columnspan=2, pady=20)

# Listbox with scrollbar
listbox_frame = Frame(root)
listbox_frame.pack(pady=20)

listbox = Listbox(listbox_frame, width=80, height=10)
listbox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

root.mainloop()