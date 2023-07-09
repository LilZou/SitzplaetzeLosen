from schueler import Schueler
from sitzplan import Sitzplan
from schuelerliste import Schuelerliste
from gui import Gui

# Hauptprogramm
schuelerliste = Schuelerliste()
schueler = schuelerliste.get_schueler_liste()

sitzplan = Sitzplan()
sitzplan.generate_sitzplan(schueler)

gui = Gui(sitzplan.get_sitzplan())
gui.display_sitzplan()