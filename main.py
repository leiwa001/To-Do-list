import tkinter as tk

from Back_End import Back
from Front_End import Front

master = tk.Tk()
master.geometry("1200x700")
master.title("Die To-Do-Liste")


back = Back()


e = Front(master, back)


master.mainloop()
