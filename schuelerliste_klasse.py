class Schuelerliste:
    def __init__(self):
        
    
    def get_schueler_liste(self):
        schueler_liste = []
        
        try:
            with open("personen.txt", "r") as file:
                for line in file:
                    vorname, nachname, sitznummer, brille = line.strip().split(",")
                    sitznummer = sitznummer.strip()
                    brille = brille.strip() == "True"
                    schueler = Schueler(vorname, nachname, int(sitznummer), brille)
                    schueler_liste.append(schueler)
        except FileNotFoundError:
            print("Die Datei 'personen.txt' wurde nicht gefunden.")
        
        return schueler_liste    