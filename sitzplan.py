class Sitzplan:
    def __init__(self):
        self.sitzplan = []

    def generate_sitzplan(self, schuelerliste):
        self.sitzplan = schuelerliste

    def get_sitzplan(self):
        return self.sitzplan