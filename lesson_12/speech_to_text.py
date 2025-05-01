from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
import speech_recognition as sr

root = Tk()
root.geometry("600x600")
root.title("Speech to Text Converter")
root.config(bg="midnight blue")

def convert_speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Info", "Please speak now...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            text_area.delete(1.0, END)
            text_area.insert(END, text)
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand the audio.")
        except sr.RequestError:
            messagebox.showerror("Error", "Could not request results; check your network connection.")

def save_text():
    file = asksaveasfile(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file:
        text = text_area.get(1.0, END)
        file.write(text)
        file.close()
        messagebox.showinfo("Info", "File saved successfully.")

def open_file():
    file = askopenfile(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file:
        text_area.delete(1.0, END)
        text_area.insert(END, file.read())
        file.close()
        messagebox.showinfo("Info", "File opened successfully.")

# Create UI elements
label = Label(root, text="Speech to Text Converter", font=("Arial", 24), bg="midnight blue", fg="white")
label.pack(pady=20)

text_area = Text(root, height=7, width=50, font=("Arial", 14), bg="light gray", fg="black")
text_area.pack(pady=20)

button = Button(root, text="Convert Speech to Text", command=convert_speech_to_text, font=("Arial", 14), bg="green", fg="white").pack(pady=10)

save_button = Button(root, text="Save Text", command=save_text, font=("Arial", 14), bg="blue", fg="white").pack(pady=10)

open_button = Button(root, text="Open File", command=open_file, font=("Arial", 14), bg="orange", fg="white").pack(pady=10)

exit_button = Button(root, text="Exit", command=root.quit, font=("Arial", 14), bg="red", fg="white").pack(pady=10)



root.mainloop()