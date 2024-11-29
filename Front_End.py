import tkinter as tk

from tkcalendar import Calendar


class Front:
    def __init__(self, master, back):
        self.fenster = master

        # Eingabefeld beschreiben und mit Enter bestätigen
        self.eingabefeld = tk.Entry(self.fenster, bd=3, width=80)
        self.eingabefeld.bind(
            "<Return>",
            lambda event: [back.add_task(self.eingabefeld.get()), self.change_label_add_task(self.eingabefeld.get())],
        )
        self.eingabefeld.place(relx=0.2, rely=0.1)

        # Label s.Text
        anfangs_label = tk.Label(self.fenster, text="Gib deine Aufgabe ein: ")
        anfangs_label.place(relx=0.05, rely=0.1)

        # Label, dass die Aufgabe als gespeichert anzeigt
        self.task_label = tk.Label(self.fenster)
        self.task_label.place(relx=0.36, rely=0.155)

        # Button, um task zu bestätigen
        task_button = tk.Button(
            self.fenster,
            text="Bestätigen",
            command=lambda: [back.add_task(self.eingabefeld.get()), self.change_label_add_task(self.eingabefeld.get())],
            bd=5,
        )

        task_button.place(relx=0.41, rely=0.2, width=100, height=40)

        # Button, um Daten in Json zu speichern
        speicher_button = tk.Button(
            self.fenster,
            text="Speichern",
            command=lambda: [back.button_action_speichern(), self.change_speicher_label()],
            bd=5,
        )
        speicher_button.place(relx=0.2, rely=0.85, width=100, height=40)

        # Button, um Daten aus Json zu laden
        lade_button = tk.Button(
            self.fenster,
            text="Laden",
            command=lambda: [back.button_action_laden(self.aufgabenliste), self.change_lade_label()],
            bd=5,
        )
        lade_button.place(relx=0.33, rely=0.85, width=100, height=40)

        # Label, um Speichern/Laden zu bestätigen
        self.speicher_label = tk.Label(self.fenster)
        self.speicher_label.place(relx=0.34, rely=0.45)
        self.lade_label = tk.Label(self.fenster)
        self.lade_label.place(relx=0.36, rely=0.45)

        # Exit Button
        exit_button = tk.Button(self.fenster, text="Beenden", command=self.fenster.quit, bd=5)
        exit_button.place(relx=0.07, rely=0.85, width=100, height=40)

        # Bearbeiten-Button
        bearbeiten_button = tk.Button(self.fenster, text="Bearbeiten", command=lambda: [self.create_new_window(back)], bd=5)
        bearbeiten_button.place(relx=0.9, rely=0.03, width=100, height=40)

        # Auflistung hinzufügen
        self.aufgabenliste = tk.Listbox(self.fenster, width=28, height=28, bd=5)
        self.aufgabenliste.place(relx=0.79, rely=0.1)

        scrollbar = tk.Scrollbar(self.fenster)
        scrollbar.place(in_=self.aufgabenliste, relx=1.0, relheight=1.0, bordermode="outside")
        self.aufgabenliste.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.aufgabenliste.yview)

        self.aufgabenliste.bind("<Double-1>", lambda event: self.task_edit(self.aufgabenliste.index(f"@{event.x},{event.y}"), back))

        aufgaben_label = tk.Label(self.fenster, text="Deine Aufgaben:")
        aufgaben_label.place(relx=0.79, rely=0.06)
        loesch_button = tk.Button(
            self.fenster,
            text="Löschen",
            command=lambda: [back.button_action_loeschen(self.aufgabenliste), self.change_loesch_label()],
            bd=5,
        )
        loesch_button.place(relx=0.85, rely=0.85, width=100, height=40)
        self.loesch_label = tk.Label(self.fenster)
        self.loesch_label.place(relx=0.82, rely=0.92)

        back.button_action_laden(self.aufgabenliste)

    def change_label_add_task(self, task):
        bestaetigung_task = "Die Aufgabe: '" + task + "' wurde gespeichert."
        self.task_label.config(text=bestaetigung_task)
        self.eingabefeld.delete(0, tk.END)
        self.aufgabenliste.insert(tk.END, task)
        self.label_loeschen_eingabe()

    def change_speicher_label(self):
        self.speicher_label.config(text="Ihre Aufgaben wurden gespeichert!")
        self.label_loeschen_speichern()

    def change_lade_label(self):
        self.lade_label.config(text="Ihre Aufgaben wurden geladen!")
        self.label_loeschen_laden()

    def change_loesch_label(self):
        self.loesch_label.config(text="Die ausgewählte Aufgabe\n wurde gelöscht!")
        self.label_loeschen_loeschen()

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







    # Einbinden Doppelklick und dann entsprechende Bearbeitung
    def task_edit(self, index, back):

        print(index)

        self.aufgabenliste.edit_item = index
        text = self.aufgabenliste.get(index)
        y0 = self.aufgabenliste.bbox(index)[1]
        entry = tk.Entry(self.fenster, borderwidth=0, highlightthickness=1)
        entry.bind("<Return>", lambda event: [self.accept_edit(event.widget.get()), back.accept_edit(index, event.widget.get()), event.widget.destroy()])
        entry.bind("<Escape>", self.cancel_edit)

        entry.insert(0, text)
        entry.selection_from(0)
        entry.selection_to("end")
        entry.place(relx=0.8, y=y0 + 70, relwidth=0.2, width=-1)
        entry.focus_set()

    # bei 'ESC' berabeiten abbrechen
    def cancel_edit(self, event):
        print("exit")
        event.widget.destroy()

    # bei 'Enter' alten Eintrag löschen und neuen hinzufügen
    def accept_edit(self, new_data):
        print("accept")

        self.aufgabenliste.delete(self.aufgabenliste.edit_item)
        self.aufgabenliste.insert(self.aufgabenliste.edit_item, new_data)














    def create_new_window(self, back):
        self.new_window = tk.Toplevel(self.fenster)
        self.new_window.geometry("1000x600")

        sel_task = self.aufgabenliste.curselection()

        task = back.get_task_newwindow(sel_task)
        self.new_window.title(task)

        beschreibung = back.get_beschreibung_newindow(sel_task)

        self.sel_dict = back.get_sel_dict_newindow(sel_task)

        speicher_button = tk.Button(
            self.new_window,
            text="Speichern",
            command=lambda: [
                back.bearbeitung_speichern(self.textfeld.get("1.0", tk.END), self.sel_dict),
                self.new_window.destroy(),
            ],
            bd=5,
        )
        speicher_button.place(relx=0.78, rely=0.85)

        task_label = tk.Label(self.new_window, text=f"Aufgabe: '{task}'", font=("Arial", 20))
        task_label.place(relx=0.42, rely=0.05)

        self.textfeld = tk.Text(self.new_window, height=18, width=30)
        self.textfeld.place(relx=0.7, rely=0.2)
        self.textfeld.insert(tk.END, beschreibung)

        self.cal = Calendar(self.new_window, selectmode="day", year=2024, month=11, day=10, font="Arial 12")
        self.cal.place(relx=0.1, rely=0.48)
        self.cal_button = tk.Button(
            self.new_window,
            text="Auswählen",
            command=lambda: [
                back.get_datum(self.sel_dict, self.cal.get_date()),
                self.cal_label.config(text="Fälligkeitstermin: " + self.cal.get_date()),
            ],
            bd=5,
        )
        self.cal_button.place(relx=0.2, rely=0.85)

        self.cal_label = tk.Label(self.new_window, font="Arial 12")
        self.cal_label.place(relx=0.4, rely=0.85)

        erstellt_label = tk.Label(self.new_window, text="Erstellt am: " + self.sel_dict["erstellung"], font="Arial 12")
        erstellt_label.place(relx=0.1, rely=0.18)
        faellig_label = tk.Label(self.new_window, text="Fällig am: " + self.sel_dict["faelligkeit"], font="Arial 12")
        faellig_label.place(relx=0.1, rely=0.25)

        check_status = back.get_check_status(self.sel_dict)
        self.check_label = tk.Label(self.new_window, text=check_status, font="Arial 12")
        self.check_label.place(relx=0.11, rely=0.32)

        self.var1 = tk.IntVar()

        self.var1.set(1) if check_status == "  Abgeschlossen!" else self.var1.set(0)

        check = tk.Checkbutton(
            self.new_window,
            text="",
            variable=self.var1,
            onvalue=1,
            offvalue=0,
            command=lambda: [back.checkbox(self.sel_dict, self.var1.get()), self.change_check_label()],
        )
        check.place(relx=0.09, rely=0.32)

    def change_check_label(self):
        if self.var1.get() == 1:
            self.check_label.config(text="  Abgeschlossen!")
        else:
            self.check_label.config(text="  Noch nicht erledigt!")
