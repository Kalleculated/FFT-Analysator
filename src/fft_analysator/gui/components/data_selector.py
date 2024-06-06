import panel as pn


class DataSelector:
    def __init__(self):
        self.selector = pn.widgets.Select
        self.options = []
        self._component = self.selector(name='', options=self.options, size=len(self.options)+2,
                                        margin=(20, 0, 0, 20), height=30, width=200)

    @property
    def component(self):
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component
