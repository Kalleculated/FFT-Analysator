import panel as pn

class Switch:
    def __init__(self):
        # Direkt das FileInput-Widget als Attribut speichern
        self.switch = pn.widgets.Switch
        self._component = self.switch(name = 'test')

    @property
    def component(self):
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component