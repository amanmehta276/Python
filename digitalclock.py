from logging import root
import time
import tkinter as tk

def update_time():
    current_time=time.strftime("%H:%M:%S")

    label.config(text=current_time)
    root.after(1000,update_time)

    rott=tk.Tk()
    root.title("Digital Clock")

    label=tk.label(root,font=("Aerial",50),background="black",foreground="cyan")
    label.pack(anchor="center")

update_time()
root.mainloop()