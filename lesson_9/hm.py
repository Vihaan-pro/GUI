import tkinter as tk
from tkinter import ttk

# Function to show order
def show_order():
    pizza = pizza_var.get()
    qty = quantity_var.get()
    size = size_var.get()
    result = f"You ordered {qty} {pizza} {size} Size Pizza(s)"
    result_label.config(text=result)

# Main window
root = tk.Tk()
root.title("Pizza App")
root.geometry("400x250")
root.configure(bg="white")

# Title
title = tk.Label(root, text="Welcome to Pizza Hut", font=("Arial", 12), bg="white")
title.pack(pady=10)

# Pizza selection
pizza_frame = tk.Frame(root, bg="white")
pizza_frame.pack()

tk.Label(pizza_frame, text="Select Your Fav Pizza:", bg="white").grid(row=0, column=0, padx=5, pady=5)
pizza_var = tk.StringVar()
pizza_options = ttk.Combobox(pizza_frame, textvariable=pizza_var)
pizza_options['values'] = ("Veg Extravaganza", "Pepperoni", "Margherita")
pizza_options.current(0)
pizza_options.grid(row=0, column=1, padx=5)

# Quantity selection
tk.Label(pizza_frame, text="Enter Quantity:", bg="white").grid(row=1, column=0, padx=5, pady=5)
quantity_var = tk.StringVar(value="1")
quantity_entry = ttk.Combobox(pizza_frame, textvariable=quantity_var)
quantity_entry['values'] = [str(i) for i in range(1, 21)]
quantity_entry.grid(row=1, column=1)

# Size selection
size_frame = tk.Frame(root, bg="white")
size_frame.pack(pady=5)
tk.Label(size_frame, text=" ", bg="white").pack(side="left")  # Spacer
size_var = tk.StringVar(value="Small")
tk.Radiobutton(size_frame, text="S", variable=size_var, value="Small", bg="white").pack(side="left")
tk.Radiobutton(size_frame, text="M", variable=size_var, value="Medium", bg="white").pack(side="left")
tk.Radiobutton(size_frame, text="L", variable=size_var, value="Large", bg="white").pack(side="left")

# Order button
order_btn = tk.Button(root, text="Order", command=show_order)
order_btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", fg="red", bg="white", font=("Arial", 10))
result_label.pack()

root.mainloop()
