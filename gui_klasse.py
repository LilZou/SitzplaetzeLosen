class Gui:
    def __init__(self, fenster):
        self.fenster = fenster
        fenster.title("Sitzplan")
        self.label_liste = []
        self.reihen = tk.IntVar()
        self.spalten = tk.IntVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self.fenster, text="Anzahl Reihen:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        tk.Entry(self.fenster, textvariable=self.reihen).grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.fenster, text="Anzahl Spalten:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        tk.Entry(self.fenster, textvariable=self.spalten).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.fenster, text="Sitzplan generieren", command=self.generate_sitzplan).grid(row=2, columnspan=2, padx=10, pady=10)
        
    def display_sitzplan(self, sitzplan):
        for label in self.label_liste:
            label.grid_forget()
            
        self.label_liste = []
        
        for i, reihe in enumerate(sitzplan):
            for j, schueler in enumerate(reihe):
                if schueler is not None:
                    label_text = f"Vorname: {schueler.vorname}\nNachname: {schueler.nachname}\nSitznummer: {schueler.sitznummer}\nBrille: {schueler.brille}"
                    label = tk.Label(self.fenster, text=label_text, relief=tk.RAISED, width=15, height=5)
                    label.grid(row=i+3, column=j, padx=10, pady=10)
                    self.label_liste.append(label)