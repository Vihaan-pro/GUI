from tkinter import *

root = Tk()
width = 450
height = 300

Label(root, text="Average Speed Calculator", font=("Helvetica", 18, "bold"), fg="blue").pack()
def average_speed_calculator():
    hrs = int(hours.get())
    mins = int(minutes.get())
    dist = int(distance.get())
    value = dist / (hrs + (mins / 60))
    average_speed.config(text=f"{value:.2f} Km/Hr")

frame = Frame(root)
frame.pack()
frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack()

Label(frame, text="Hours", width=15, font=("Helvetica", 14, "bold"), borderwidth=2, relief="solid").pack(side=LEFT, padx=10, pady=10)
hours = Spinbox(frame, from_=0, to=10000000, width=5, font=("Helvetica", 14, "bold"))
hours.pack(side=LEFT, pady=10)

Label(frame1, text="Minutes", width=15, font=("Helvetica", 14, "bold"), borderwidth=2, relief="solid").pack(side=LEFT, padx=10, pady=10)
minutes = Spinbox(frame1, from_=0, to=10000000, width=5, font=("Helvetica", 14, "bold"))
minutes.pack(side=LEFT, pady=10)

Label(frame2, text="Distance (Km)", width=15, font=("Helvetica", 14, "bold"), borderwidth=2, relief="solid").pack(side=LEFT, padx=10, pady=10)
distance = Spinbox(frame2, from_=0, to=10000000, width=5, font=("Helvetica", 14, "bold"))
distance.pack(side=LEFT, pady=10)

Button(root, text="Average Speed", width=15, font=("Helvetica", 14, "bold"), command=average_speed_calculator, fg="red", bg="black").pack(pady=20)
average_speed = Label(root, text="", width=20, font=("Helvetica", 14, "bold"), relief="solid")
average_speed.pack()

root.mainloop()