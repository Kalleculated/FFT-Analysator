import panel as pn


class MethodSelector:
    def __init__(self):
        self.selector = pn.widgets.Select
        self.options = ["No Analysis Function", "Auto Spectral Density - Input", "Auto Spectral Density - Output",
                        "Cross Spectral Density", "Coherence","Auto Correlation - Input", "Auto Correlation - Output",
                        "Cross Correlation"]
        self._component = self.selector(name='Choose analysis method:', options=self.options, width=300, value='No Analysis Function',
                                        disabled=True)

    @property
    def component(self):
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component
