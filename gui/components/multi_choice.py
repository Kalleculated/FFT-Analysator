import panel as pn

class MultiChoice:
    def __init__(self):
        # Direkt das MultiSelector-Widget als Attribut speichern
        self.multi_select = pn.widgets.MultiChoice
        self._component = self.multi_select(name='Keine Datei ausgewählt!', value=[],
                        options=[])

    @property
    def component(self):
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component