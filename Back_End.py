import json
import tkinter as tk
from pathlib import Path
from time import strftime


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

    def add_task(self, task):
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
    def save_task(self, user):
        if user == "user1":
            path = Path("mylist_user1.json")
        elif user == "user2":
            path = Path("mylist_user2.json")
        elif user == "user3":
            path = Path("mylist_user3.json")

        self.task_list = json.dumps(self.dict_list, indent=4)
        path.write_text(self.task_list)

    # Funktion für Laden aus Json File
    def load_task(self, aufgabenliste, user):
        if user == "user1":
            path = Path("mylist_user1.json")
        elif user == "user2":
            path = Path("mylist_user2.json")
        elif user == "user3":
            path = Path("mylist_user3.json")
        if path.exists():
            self.task_list = path.read_text()
            self.dict_list = json.loads(self.task_list)
            for wert in self.dict_list:
                task = wert["task"]
                aufgabenliste.insert(tk.END, task)
        else:
            print("Keine Aufgaben gespeichert")

    # Funktion für Lösch Button
    def delete_task(self, aufgabenliste):
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
    def bearbeitung_speichern(self, eingabe, sel_dict, user):
        sel_dict["beschreibung"] = eingabe

        if user == "user1":
            path = Path("mylist_user1.json")
        elif user == "user2":
            path = Path("mylist_user2.json")
        elif user == "user3":
            path = Path("mylist_user3.json")

        task_list = json.dumps(self.dict_list, indent=4)
        path.write_text(task_list)

    def get_datum(self, sel_dict, date):
        sel_dict["faelligkeit"] = date

    def get_check_status(self, sel_dict):
        return "  Abgeschlossen!" if sel_dict["completed"] else "  Noch nicht abgeschlossen"

    def checkbox(self, sel_dict, variable):
        if variable == 1:
            sel_dict["completed"] = True
        else:
            sel_dict["completed"] = False

    def accept_edit(self, dict_index, name):
        sel_dict = self.dict_list[dict_index]
        sel_dict["task"] = name
