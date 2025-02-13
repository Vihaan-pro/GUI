import tkinter as tk
from tkinter import ttk

def submit_order():
    email = email_entry.get()
    password = password_entry.get()
    food = food_var.get()
    beverage = beverage_var.get()
    dessert = dessert_var.get()
    print(f"Order Submitted:\nEmail: {email}\nFood: {food}\nBeverage: {beverage}\nDessert: {dessert}")
    
root = tk.Tk()
root.title("Food Delivery Order")
root.geometry("500x500")
root.configure(bg="red")

frame = tk.Frame(root, bg="red", padx=20, pady=20)
frame.pack(pady=20)

# Email
email_label = tk.Label(frame, text="Email:", bg="red", fg="white", font=("Arial", 12, "bold"))
email_label.grid(row=0, column=0, sticky="w", pady=5)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=0, column=1, pady=5)

# Password
password_label = tk.Label(frame, text="Password:", bg="red", fg="white", font=("Arial", 12, "bold"))
password_label.grid(row=1, column=0, sticky="w", pady=5)
password_entry = tk.Entry(frame, show="*", width=30)
password_entry.grid(row=1, column=1, pady=5)

# Food selection
food_label = tk.Label(frame, text="Choose your food:", bg="red", fg="white", font=("Arial", 12, "bold"))
food_label.grid(row=2, column=0, sticky="w", pady=5)
food_var = tk.StringVar()
food_dropdown = ttk.Combobox(frame, textvariable=food_var, values=["Chicken Sandwich", "B.L.T", "Veg Sandwich", "None"], width=27)
food_dropdown.grid(row=2, column=1, pady=5)
food_dropdown.current(0)

# Beverage selection
beverage_label = tk.Label(frame, text="Choose your beverage:", bg="red", fg="white", font=("Arial", 12, "bold"))
beverage_label.grid(row=3, column=0, sticky="w", pady=5)
beverage_var = tk.StringVar()
beverage_dropdown = ttk.Combobox(frame, textvariable=beverage_var, values=["Cola", "Fanta", "Orange Juice", "Water", "None"], width=27)
beverage_dropdown.grid(row=3, column=1, pady=5)
beverage_dropdown.current(0)

# Dessert selection
dessert_label = tk.Label(frame, text="Choose your dessert:", bg="red", fg="white", font=("Arial", 12, "bold"))
dessert_label.grid(row=4, column=0, sticky="w", pady=5)
dessert_var = tk.StringVar()
dessert_dropdown = ttk.Combobox(frame, textvariable=dessert_var, values=["Ice Cream", "Ice Lolly", "Chocolate Cake", "None"], width=27)
dessert_dropdown.grid(row=4, column=1, pady=5)
dessert_dropdown.current(0)

# Submit button
submit_button = tk.Button(frame, text="Submit Order", command=submit_order, bg="gray", fg="black", font=("Arial", 12, "bold"), width=20)
submit_button.grid(row=5, columnspan=2, pady=20)

root.mainloop()
