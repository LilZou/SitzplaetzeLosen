class SitzplanApp:
    def __init__(self, fenster):       
        self.schueler_liste = []
        
    def generate_sitzplan(self):
        durchgaenge = self.reihen.get()
        reihen = self.spalten.get()
    
        # leerer Sitzplan wird erstellt
        sitzplan = []
        for i in range(durchgaenge):
            reihe = []
            for j in range(reihen):
                reihe.append(None)
            sitzplan.append(reihe)
    
        # zufällige Zuweisung
        schueler_liste = self.get_schueler_liste()
        schueler_mit_brille = [schueler for schueler in schueler_liste if schueler.brille]
        schueler_ohne_brille = [schueler for schueler in schueler_liste if not schueler.brille]
        
    
        shuffle(schueler_mit_brille)
        shuffle(schueler_ohne_brille)
    
        index_mit_brille = 0
        index_ohne_brille = 0
    
        for i in range(durchgaenge):
            for j in range(reihen):
                if i < 2 and index_mit_brille < len(schueler_mit_brille):
                    sitzplan[i][j] = schueler_mit_brille[index_mit_brille]
                    index_mit_brille = index_mit_brille + 1
                else:
                    sitzplan[i][j] = schueler_ohne_brille[index_ohne_brille]
                    index_ohne_brille = index_ohne_brille + 1
    
        self.display_sitzplan(sitzplan)
        
        
        

    