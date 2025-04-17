# from tkinter import *
# import tkinter.font as font

# def convert():
#     temp_celsius = celsius_value.get()

#     if temp_celsius.replace('.', '', 1).isdigit():
#         temp_celsius = float(temp_celsius)
#         temp_fahrenheit = (temp_celsius * 9/5) + 32
#         fahrenheit.config(text=f"{temp_fahrenheit:.2f}°F")
    
#     else:
#         fahrenheit.config(text="Invalid input!")

# root = Tk()
# root.title("Temperature Converter")
# root.geometry("600x600")
# root.configure(bg="lightblue")

# frame = Frame(root, bg="lightblue", padx=20, pady=20)
# frame.pack(pady=20)

# desc = Label(frame, text="Celsius to Fahrenheit", bg="lightblue", fg="black", font=("Arial", 12, "bold"))
# desc.pack()

# message = Label(frame, text="Enter Celsius:", bg="lightblue", fg="black", font=("Arial", 12, "bold"))
# message.grid(row=0, column=0, sticky="w", pady=5)   

# celsius_value = Entry(frame, width=30)
# celsius_value.grid(row=0, column=1, pady=5)

# convert_button = Button(frame, text="Convert", command=convert, bg="gray", fg="black", font=("Arial", 12, "bold"), width=20)
# convert_button.grid(row=1, columnspan=2, pady=20)

# fahrenheit = Label(frame, bg="lightblue", fg="black", font=("Arial", 12, "bold"))
# fahrenheit.grid(row=0, column=0, sticky="w", pady=5) 

# root.mainloop()








from tkinter import *
import tkinter.font as font

def convert():
    temp_celsius = celsius_value.get()

    if temp_celsius.replace('.', '', 1).isdigit() or (temp_celsius.startswith('-') and temp_celsius[1:].replace('.', '', 1).isdigit()):
        temp_celsius = float(temp_celsius)
        temp_fahrenheit = (temp_celsius * 9/5) + 32
        fahrenheit.config(text=f"{temp_fahrenheit:.2f}°F")
    else:
        fahrenheit.config(text="Invalid input!")

root = Tk()
root.title("Temperature Converter")
root.geometry("600x600")
root.configure(bg="lightblue")

frame = Frame(root, bg="lightblue", padx=20, pady=20)
frame.pack(pady=20)

desc = Label(frame, text="Celsius to Fahrenheit", bg="lightblue", fg="black", font=("Arial", 12, "bold"))
desc.grid(row=0, column=0, columnspan=2, pady=10)

message = Label(frame, text="Enter Celsius:", bg="lightblue", fg="black", font=("Arial", 12, "bold"))
message.grid(row=1, column=0, sticky="w", pady=5)

celsius_value = Entry(frame, width=30)
celsius_value.grid(row=1, column=1, pady=5)

convert_button = Button(frame, text="Convert", command=convert, bg="gray", fg="black", font=("Arial", 12, "bold"), width=20)
convert_button.grid(row=2, columnspan=2, pady=20)

fahrenheit = Label(frame, bg="lightblue", fg="black", font=("Arial", 12, "bold"))
fahrenheit.grid(row=3, columnspan=2, pady=5)

root.mainloop()