
import tkinter as tk

from Front_End import Front

fenster = tk.Tk()
fenster.geometry("1200x700")
fenster.title("Die To-Do-Liste")


e = Front(fenster)
fenster.mainloop()
