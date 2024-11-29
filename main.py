import tkinter as tk

from Back_End import Back
from Front_End import Front

master = tk.Tk()
master.geometry("1200x700")
master.title("Die To-Do-Liste")
master.config(bg="#7991a2")


back = Back()


e = Front(master, back)


master.mainloop()
