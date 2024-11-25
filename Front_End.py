import tkinter as tk

fenster = tk.Tk()
fenster.geometry("1200x700")
fenster.title("Die To-Do-Liste")


class Front:
    def __init__(self, master):
        # Eingabefeld beschreiben und mit Enter bestätigen
        self.eingabefeld = tk.Entry(master, bd=3, width=80)
        self.eingabefeld.bind("<Return>", self.callback)
        self.eingabefeld.place(relx=0.2, rely=0.1)

        # Label s.Text
        self.anfangs_label = tk.Label(master, text="Gib deine Aufgabe ein: ")
        self.anfangs_label.place(relx=0.05, rely=0.1)

        # Label, dass die Aufgabe als gespeichert anzeigt
        self.task_label = tk.Label(master)
        self.task_label.place(relx=0.36, rely=0.155)

        # Button, um task zu bestätigen
        self.task_button = tk.Button(master, text="Bestätigen", command=self.button_action_eingabefeld, bd=5)
        self.task_button.place(relx=0.41, rely=0.2, width=100, height=40)

        # Button, um Daten in Json zu speichern
        self.speicher_button = tk.Button(master, text="Speichern", command=self.button_action_speichern, bd=5)
        self.speicher_button.place(relx=0.2, rely=0.85, width=100, height=40)

        # Button, um Daten aus Json zu laden
        self.lade_button = tk.Button(master, text="Laden", command=self.button_action_laden, bd=5)
        self.lade_button.place(relx=0.33, rely=0.85, width=100, height=40)

        # Label, um Speichern/Laden zu bestätigen
        self.speicher_label = tk.Label(master)
        self.speicher_label.place(relx=0.34, rely=0.45)
        self.lade_label = tk.Label(master)
        self.lade_label.place(relx=0.36, rely=0.45)

        # Exit Button
        self.exit_button = tk.Button(master, text="Beenden", command=master.quit, bd=5)
        self.exit_button.place(relx=0.07, rely=0.85, width=100, height=40)

        # Bearbeiten-Button
        self.bearbeiten_button = tk.Button(master, text="Bearbeiten", bd=5)
        self.bearbeiten_button.place(relx=0.9, rely=0.03, width=100, height=40)

        # Auflistung hinzufügen
        self.aufgabenliste = tk.Listbox(master, width=28, height=28, bd=5)
        self.aufgabenliste.place(relx=0.79, rely=0.1)

        scrollbar = tk.Scrollbar(master)
        scrollbar.place(in_=self.aufgabenliste, relx=1.0, relheight=1.0, bordermode="outside")
        self.aufgabenliste.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.aufgabenliste.yview)

        self.aufgabenliste.bind("<Double-1>", self.edit_start)

        self.aufgaben_label = tk.Label(master, text="Deine Aufgaben:")
        self.aufgaben_label.place(relx=0.79, rely=0.06)
        self.loesch_button = tk.Button(master, text="Löschen", command=self.button_action_loeschen, bd=5)
        self.loesch_button.place(relx=0.85, rely=0.85, width=100, height=40)
        self.loesch_label = tk.Label(master)
        self.loesch_label.place(relx=0.82, rely=0.92)

    def button_action_eingabefeld(self):
        task = self.eingabefeld.get()
        if task == "":
            self.task_label.config(text="Gib zuerst eine Aufgabe ein!")
        else:
            self.task_label.config(text="Die Aufgabe '" + task + "' wurde gespeichert!")
        self.label_loeschen_eingabe()

    def button_action_speichern(self):
        self.speicher_label.config(text="Ihre Aufgaben wurden gespeichert!")
        self.label_loeschen_speichern()

    def button_action_laden(self):
        self.lade_label.config(text="Ihre Aufgaben wurden geladen!")
        self.label_loeschen_laden()

    def button_action_loeschen(self):
        self.loesch_label.config(text="Die ausgewählte Aufgabe\n wurde gelöscht!")
        self.label_loeschen_loeschen()

    # Index des zu bearbeitenden Elements
    def edit_start(self, event):
        index = self.aufgabenliste.index(f"@{event.x},{event.y}")
        self.task_edit(index)

    # Einbinden Doppelklick und dann entsprechende Bearbeitung
    def task_edit(self, index):
        self.aufgabenliste.edit_item = index
        text = self.aufgabenliste.get(index)
        y0 = self.aufgabenliste.bbox(index)[1]
        entry = tk.Entry(self.fenster, borderwidth=0, highlightthickness=1)
        entry.bind("<Return>", self.accept_edit)
        entry.bind("<Escape>", self.cancel_edit)

        entry.insert(0, text)
        entry.selection_from(0)
        entry.selection_to("end")
        entry.place(relx=0.8, y=y0 + 70, relwidth=0.2, width=-1)
        entry.focus_set()

    # bei 'ESC' berabeiten abbrechen
    def cancel_edit(self, event):
        event.widget.destroy()

    # bei 'Enter' alten Eintrag löschen und neuen hinzufügen
    def accept_edit(self, event):
        new_data = event.widget.get()
        self.aufgabenliste.delete(self.aufgabenliste.edit_item)
        self.aufgabenliste.insert(self.aufgabenliste.edit_item, new_data)
        event.widget.destroy()

    # mit Enter bestätigen Hilfsfunktion
    def callback(self, event):
        self.button_action_eingabefeld()

    # Loesch-Funktionen, um nur 1 Label gleichzeitig anzuzeigen
    def label_loeschen_eingabe(self):
        self.speicher_label.config(text="")
        self.lade_label.config(text="")
        self.loesch_label.config(text="")

    def label_loeschen_speichern(self):
        self.task_label.config(text="")
        self.lade_label.config(text="")
        self.loesch_label.config(text="")

    def label_loeschen_laden(self):
        self.task_label.config(text="")
        self.speicher_label.config(text="")
        self.loesch_label.config(text="")

    def label_loeschen_loeschen(self):
        self.task_label.config(text="")
        self.speicher_label.config(text="")
        self.lade_label.config(text="")


e = Front(fenster)
fenster.mainloop()
