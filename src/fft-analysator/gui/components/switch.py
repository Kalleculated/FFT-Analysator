import panel as pn


class Switch:
    def __init__(self):
        self.switch = pn.widgets.Switch
        self._component = self.switch(name='test', width=30, margin=(0, 20))

    @property
    def component(self):
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component
