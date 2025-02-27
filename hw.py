import tkinter as tk

def convert():
    try:
        kg = float(entry_kg.get())
        gram = kg * 1000
        pounds = kg * 2.20462
        ounce = kg * 35.274
        
        gram_entry.delete(0, tk.END)
        gram_entry.insert(tk.END, f"{gram:.1f}")
        
        pounds_entry.delete(0, tk.END)
        pounds_entry.insert(tk.END, f"{pounds:.3f}")
        
        ounce_entry.delete(0, tk.END)
        ounce_entry.insert(tk.END, f"{ounce:.1f}")
    except ValueError:
        pass

root = tk.Tk()
root.title("Weight Converter")

# Input Field
label_kg = tk.Label(root, text="Enter the weight in Kg")
label_kg.grid(row=0, column=0)

entry_kg = tk.Entry(root)
entry_kg.grid(row=0, column=1)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=0, column=2)

# Output Fields
label_gram = tk.Label(root, text="Gram")
label_gram.grid(row=1, column=0)

gram_entry = tk.Entry(root)
gram_entry.grid(row=1, column=1)

label_pounds = tk.Label(root, text="Pounds")
label_pounds.grid(row=1, column=2)

pounds_entry = tk.Entry(root)
pounds_entry.grid(row=1, column=3)

label_ounce = tk.Label(root, text="Ounce")
label_ounce.grid(row=1, column=4)

ounce_entry = tk.Entry(root)
ounce_entry.grid(row=1, column=5)

root.mainloop()