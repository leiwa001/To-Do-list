import tkinter as tk

from Back_End import Back
from Front_End import Front

master = tk.Tk()


back = Back()


e = Front(master, back)


master.mainloop()
