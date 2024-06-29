import panel as pn


class ChannelSelector:
    def __init__(self):
        self.selector = pn.widgets.Select
        self.options = []
        self._component = self.selector(name='No data chosen!', options=self.options, width=135, margin=(10,15),
                                        disabled=True)

    @property
    def component(self):
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component
