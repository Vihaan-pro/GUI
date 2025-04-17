import tkinter as tk
import time

root = tk.Tk()
root.title("Stopwatch")
root.geometry("200x100")

hours = 0
minutes = 0
seconds = 0
is_running = False

entry_hours = tk.Entry(root, width=2)
entry_hours.grid(row=0, column=0)
entry_hours.insert(0, "00")
entry_minutes = tk.Entry(root, width=2)
entry_minutes.grid(row=0, column=1)
entry_minutes.insert(0, "00")
entry_seconds = tk.Entry(root, width=2)
entry_seconds.grid(row=0, column=2)
entry_seconds.insert(0, "00")

def start_stop():
    global is_running
    is_running = not is_running
    if is_running:
        start_stop_button.config(text="Stop")
        start_time = time.time()
        while is_running:
            elapsed_time = time.time() - start_time
            hours = int(elapsed_time / 3600)
            minutes = int((elapsed_time % 3600) / 60)
            seconds = int(elapsed_time % 60)
            entry_hours.delete(0, tk.END)
            entry_hours.insert(0, str(hours).zfill(2))
            entry_minutes.delete(0, tk.END)
            entry_minutes.insert(0, str(minutes).zfill(2))
            entry_seconds.delete(0, tk.END)
            entry_seconds.insert(0, str(seconds).zfill(2)
            )
            root.update()
    else:
        start_stop_button.config(text="Start")

start_stop_button = tk.Button(root, text="Start", command=start_stop)
start_stop_button.grid(row=1, column=1)

root.mainloop()


