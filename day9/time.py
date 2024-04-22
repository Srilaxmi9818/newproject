import tkinter as tk
from datetime import datetime

def update_clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_clock)  # Update every second (1000 milliseconds)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Arial", 24), bg="black", fg="white")
label.pack(padx=20, pady=20)

update_clock()  # Start the clock update process

root.mainloop()
