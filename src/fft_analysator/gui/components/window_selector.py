import panel as pn


class WindowSelector:
    def __init__(self):
        self.selector = pn.widgets.Select
        self.options = ['Hanning', 'Rectangular', 'Hamming', 'Bartlett', 'Blackman']
        self._component = self.selector(name='Choose window:', options=self.options, width=140, value='Hanning')

    @property
    def component(self):
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component
