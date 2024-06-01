import panel as pn


class Selector:
    def __init__(self):
        self.selector = pn.widgets.Select
        self.options = []
        self._component = self.selector(name='Choose table:', options=self.options, size=len(self.options)+2)

    @property
    def component(self):
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component
