import tkinter as tk
import random

class Gui:
    def __init__(self, schuelerliste):
        self.schuelerliste = schuelerliste
        self.window = tk.Tk()
        self.window.title("Sitzplan")

        
        self.label_row = tk.Label(self.window, text="Anzahl der Reihen:")
        self.label_row.grid(row=0, column=0)
        self.entry_row = tk.Entry(self.window)
        self.entry_row.grid(row=0, column=1)

        self.label_column = tk.Label(self.window, text="Anzahl der Spalten:")
        self.label_column.grid(row=1, column=0)
        self.entry_column = tk.Entry(self.window)
        self.entry_column.grid(row=1, column=1)

        # Button zum Generieren des Sitzplans
        self.generate_button = tk.Button(self.window, text="Sitzplan generieren", command=self.display_sitzplan)
        self.generate_button.grid(row=2, columnspan=2, pady=10)

        self.window.mainloop()

    def display_sitzplan(self):
        rows = int(self.entry_row.get())
        columns = int(self.entry_column.get())

        # Lösche vorherige Sitzplan-Labels
        for widget in self.window.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()

    
        random.shuffle(self.schuelerliste)

        
        schueler_mit_brille = []
        schueler_ohne_brille = []
        for schueler in self.schuelerliste:
            if schueler.brille:
                schueler_mit_brille.append(schueler)
            else:
                schueler_ohne_brille.append(schueler)

        
        schueler_pro_reihe = columns if rows >= 2 else columns * 2

       
        sitzplan = []
        for i, schueler in enumerate(schueler_mit_brille):
            platz = i + 1
            name = schueler.vorname
            nachname = schueler.nachname
            brille = schueler.brille
            sitzplan.append((platz, name, nachname, brille))

        
        for i, schueler in enumerate(schueler_ohne_brille):
            platz = i + len(schueler_mit_brille) + 1
            name = schueler.vorname
            nachname = schueler.nachname
            brille = schueler.brille
            sitzplan.append((platz, name, nachname, brille))

        # Schleife über den Sitzplan
        for i, schueler in enumerate(sitzplan):
            platz, vorname, nachname, brille = schueler

            
            row = (i // schueler_pro_reihe) + 3  
            column = i % schueler_pro_reihe

            
            label = tk.Label(self.window, text=f"Platz {platz}: {vorname} {nachname} (Brille: {brille})")
            label.grid(row=row, column=column, padx=10, pady=10)

        # Aktiviere den Button erneut
        self.generate_button.configure(state=tk.NORMAL)
