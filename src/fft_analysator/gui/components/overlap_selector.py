import panel as pn

class OverlapSelector:
    def __init__(self):
        self.selector = pn.widgets.Select
        self.options = ['None', '50%', '75%', '87.5%']
        self._component = self.selector(name='Choose overlap:', options=self.options, width=140, value='50%',
                                        disabled=True)

    @property
    def component(self):
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component
