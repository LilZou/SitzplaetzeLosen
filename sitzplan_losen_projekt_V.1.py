import tkinter as tk
from random import shuffle
from schuelerklasse import Schueler
from gui_klasse import Gui
from sitzplanapp_klasse import SitzplanApp
from schuelerliste_klasse import Schuelerliste

fenster = tk.Tk()
app = SitzplanApp(fenster)
fenster.mainloop()