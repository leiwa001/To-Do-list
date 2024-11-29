
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

    # Funktion für Speichern in Json File
    def button_action_speichern(self):

        path = Path("mylist.json")
        self.task_list = json.dumps(self.dict_list, indent=4)
        path.write_text(self.task_list)



    # Funktion für Laden aus Json File
    def button_action_laden(self, aufgabenliste):
        path = Path("mylist.json")
        if path.exists():
            self.task_list = path.read_text()
            self.dict_list = json.loads(self.task_list)
            for wert in self.dict_list:
                task = wert["task"]
                aufgabenliste.insert(tk.END, task)
        else:
            print("Keine Aufgaben gespeichert")


    # Funktion für Lösch Button
    def button_action_loeschen(self, aufgabenliste):

        self.sel_task = aufgabenliste.curselection()
        aufgabenliste.delete(self.sel_task)

        for i in range(100):
            if self.sel_task == (i,):
                del self.dict_list[i]




    def get_task_newwindow(self, sel_task):
        for i in range(100):
            if sel_task == (i,):
                sel_dict = self.dict_list[i]
                task = sel_dict["task"]
        return task

    def get_beschreibung_newindow(self, sel_task):
        for i in range(100):
            if sel_task == (i,):
                sel_dict = self.dict_list[i]
                beschreibung = sel_dict["beschreibung"]
        return beschreibung


    def get_sel_dict_newindow(self, sel_task):
        for i in range(100):
            if sel_task == (i,):
                sel_dict = self.dict_list[i]
        return sel_dict


    # speichert Bearbeitung im new_window
    def bearbeitung_speichern(self, eingabe, sel_dict):
        sel_dict["beschreibung"] = eingabe

        path = Path("mylist.json")
        task_list = json.dumps(self.dict_list, indent=4)
        path.write_text(task_list)


    def get_datum(self, sel_dict, date):
        sel_dict["faelligkeit"] = date


    def get_check_status(self, sel_dict):
        return "  Abgeschlossen!" if sel_dict["completed"] else "  Noch nicht abgeschlossen"
    

    def checkbox(self, sel_dict, variable):
        if  variable == 1:
            sel_dict["completed"] = True
        else:
            sel_dict["completed"] = False











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


