import tkinter as tk


class Front:
    def __init__(self, master, back):


        fenster = master

        # Eingabefeld beschreiben und mit Enter bestätigen
        eingabefeld = tk.Entry(fenster, bd=3, width=80)
        eingabefeld.bind("<Return>", back.callback)
        eingabefeld.place(relx=0.2, rely=0.1)

        # Label s.Text
        anfangs_label = tk.Label(fenster, text="Gib deine Aufgabe ein: ")
        anfangs_label.place(relx=0.05, rely=0.1)

        # Label, dass die Aufgabe als gespeichert anzeigt
        task_label = tk.Label(fenster)
        task_label.place(relx=0.36, rely=0.155)

        # Button, um task zu bestätigen
        task_button = tk.Button(fenster, text="Bestätigen", command=back.button_action_eingabefeld, bd=5)
        task_button.place(relx=0.41, rely=0.2, width=100, height=40)

        # Button, um Daten in Json zu speichern
        speicher_button = tk.Button(fenster, text="Speichern", command=back.button_action_speichern, bd=5)
        speicher_button.place(relx=0.2, rely=0.85, width=100, height=40)

        # Button, um Daten aus Json zu laden
        lade_button = tk.Button(fenster, text="Laden", command=back.button_action_laden, bd=5)
        lade_button.place(relx=0.33, rely=0.85, width=100, height=40)

        # Label, um Speichern/Laden zu bestätigen
        speicher_label = tk.Label(fenster)
        speicher_label.place(relx=0.34, rely=0.45)
        lade_label = tk.Label(fenster)
        lade_label.place(relx=0.36, rely=0.45)

        # Exit Button
        exit_button = tk.Button(fenster, text="Beenden", command=fenster.quit, bd=5)
        exit_button.place(relx=0.07, rely=0.85, width=100, height=40)

        # Bearbeiten-Button
        bearbeiten_button = tk.Button(fenster, text="Bearbeiten", bd=5)
        bearbeiten_button.place(relx=0.9, rely=0.03, width=100, height=40)

        # Auflistung hinzufügen
        aufgabenliste = tk.Listbox(fenster, width=28, height=28, bd=5)
        aufgabenliste.place(relx=0.79, rely=0.1)

        scrollbar = tk.Scrollbar(fenster)
        scrollbar.place(in_=aufgabenliste, relx=1.0, relheight=1.0, bordermode="outside")
        aufgabenliste.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=aufgabenliste.yview)

        aufgabenliste.bind("<Double-1>", back.edit_start)

        aufgaben_label = tk.Label(fenster, text="Deine Aufgaben:")
        aufgaben_label.place(relx=0.79, rely=0.06)
        loesch_button = tk.Button(fenster, text="Löschen", command=back.button_action_loeschen, bd=5)
        loesch_button.place(relx=0.85, rely=0.85, width=100, height=40)
        loesch_label = tk.Label(fenster)
        loesch_label.place(relx=0.82, rely=0.92)