import tkinter as tk
from gtts import gTTS
from playsound import playsound  # Import playsound
import os

root = tk.Tk()
root.geometry("600x600")
root.title("Text to Speech Converter")
root.config(bg="midnight blue") 

frame = tk.Frame(root, bg="midnight blue")
frame.pack(pady=20)

label = tk.Label(frame, text="Text To Speech Converter", font=("Arial", 14), bg="midnight blue", fg="white")
label.pack(pady=10)

label2 = tk.Label(frame, text="Enter Text:", font=("Arial", 12), bg="midnight blue", fg="white")
label2.pack(pady=10)

entry = tk.Entry(frame, width=50, font=("Arial", 12))
entry.pack(pady=10)

button = tk.Button(frame, text="Convert to Speech", command=lambda: convert_to_speech(entry.get()), font=("Arial", 12), bg="light blue")
button.pack(pady=10)

def convert_to_speech(text):
    if text:
        tts = gTTS(text=text, lang='es')
        output_file = "output.mp3"
        
        tts.save(output_file)
        playsound(output_file)  # Use playsound to play the audio
    else:
        tk.messagebox.showwarning("Input Error", "Please enter some text.")

root.mainloop()