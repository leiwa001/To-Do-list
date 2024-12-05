import tkinter as tk

def on_right_click(event):
    context_menu.post(event.x_root, event.y_root)

root = tk.Tk()
root.title("Rechtsklick-Menü Beispiel")

# Erstelle ein Kontextmenü
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Option 1")
context_menu.add_command(label="Option 2")
context_menu.add_separator()
context_menu.add_command(label="Beenden", command=root.quit)

# Binde den Rechtsklick an die Funktion
root.bind("<Button-3>", on_right_click)

root.mainloop()