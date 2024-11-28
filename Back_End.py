
import json
import tkinter as tk
from pathlib import Path
from time import strftime

from tkcalendar import Calendar


class Back:
    def __init__(self):


        self.dict_list = []

        self.dictionary = {
            "task": "Aufgabe1",
            "completed": False,
            "beschreibung": "Beschreibung:\n\n",
            "faelligkeit": "-nicht festgelegt-",
            "erstellung": "",
        }


    def add_task(self,task):
        print(task)

        if task == "":
            print("leer")

        else:
            self.dictionary["task"] = task
            time = strftime("%d.%m.%Y")
            self.dictionary["erstellung"] = time
            new_dict = self.dictionary.copy()
            self.dict_list.append(new_dict)

            print(self.dict_list)








    # eingabefeld zurücksetzen, task in liste anzeigen
    def button_action_eingabefeld(self, task):


            bestaetigung_task = "Die Aufgabe: '" + task + "' wurde gespeichert."
            self.task_label.config(text=bestaetigung_task)

            self.eingabefeld.delete(0, tk.END)
            self.aufgabenliste.insert(tk.END, task)


    # Funktion für Speichern in Json File
    def button_action_speichern(self):

        print("spichern")

        self.speicher_label.config(text="Ihre Aufgaben wurden gespeichert!")
        path = Path("mylist.json")
        self.task_list = json.dumps(self.dict_list, indent=4)
        path.write_text(self.task_list)
        self.label_loeschen_speichern()

    # Funktion für Laden aus Json File
    def button_action_laden(self):
        self.lade_label.config(text="Ihre Aufgaben wurden geladen!")
        path = Path("mylist.json")
        if path.exists():
            self.task_list = path.read_text()
            self.dict_list = json.loads(self.task_list)
            for wert in self.dict_list:
                task = wert["task"]
                self.aufgabenliste.insert(tk.END, task)
        else:
            print("Keine Aufgaben gespeichert")
        self.label_loeschen_laden()

    # Funktion für Lösch Button
    def button_action_loeschen(self):
        self.loesch_label.config(text="Die ausgewählte Aufgabe\n wurde gelöscht!")
        self.sel_task = self.aufgabenliste.curselection()
        self.aufgabenliste.delete(self.sel_task)
        self.aufgabe_aus_liste_loeschen()

    # löscht ausgewählte aufgabe aus dict_list
    def aufgabe_aus_liste_loeschen(self):
        for i in range(100):
            if self.sel_task == (i,):
                del self.dict_list[i]
        self.label_loeschen_loeschen()

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


