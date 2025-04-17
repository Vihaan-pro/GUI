import tkinter as tk

def convert():
    try:
        amount = float(entry_amount.get())
        rate = 0.014  # Example conversion rate (Rs to $)
        converted_amount = amount * rate
        
        result_entry.delete(0, tk.END)
        result_entry.insert(tk.END, f"{converted_amount:.2f}")
    except ValueError:
        pass

root = tk.Tk()
root.title("Currency Converter")

frame = tk.Frame(root, bd=2, relief=tk.SOLID)
frame.grid(row=0, column=0, padx=10, pady=10)

header_label = tk.Label(frame, text="Rs -> $ Converter", font=("Arial", 12, "bold"))
header_label.grid(row=0, column=0, columnspan=2, pady=5)

# Input Field
label_amount = tk.Label(frame, text="Source Currency amount (Rs.)")
label_amount.grid(row=1, column=0, padx=5, pady=5)

entry_amount = tk.Entry(frame)
entry_amount.grid(row=1, column=1, padx=5, pady=5)

# Output Field
label_result = tk.Label(frame, text="Target Currency amount ($)")
label_result.grid(row=2, column=0, padx=5, pady=5)

result_entry = tk.Entry(frame)
result_entry.grid(row=2, column=1, padx=5, pady=5)

# Convert Button
convert_button = tk.Button(frame, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
