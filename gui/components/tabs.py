import panel as pn

class Tabs:
    def __init__(self):
        self.tabs = pn.Tabs
        self._component = self.tabs(('Signalinput', 'Keine Datei ausgewählt!'), 
                                    sizing_mode='stretch_width', dynamic=True)

    @property
    def component(self):
        return self._component