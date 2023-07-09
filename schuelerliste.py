from schueler import Schueler

class Schuelerliste:
    def __init__(self):
        self.schuelerliste = []

    def get_schueler_liste(self):
        with open('personen.txt', 'r') as file:
            for line in file:
                name, nachname, sitzplatz, brille = line.strip().split(', ')
                schueler = Schueler(name, nachname, int(sitzplatz), brille == 'True')
                self.schuelerliste.append(schueler)
        return self.schuelerliste