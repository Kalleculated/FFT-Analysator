import panel as pn

class Tabs:
    def __init__(self):
        # Direkt das MultiSelector-Widget als Attribut speichern
        self.tabs = pn.Tabs
        self._component = self.tabs(('Signalinput', 'Keine Datei ausgewählt!'), 
                                    sizing_mode='stretch_width', dynamic=True)

    @property
    def component(self):
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component