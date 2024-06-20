import panel as pn


class Tabs:
    def __init__(self):
        self.tabs = pn.Tabs
        self.str_signal_tab = "Signalinput"
        self.str_Spektrum_tab = "Frequenzgang"
        self.str_Impulsantwort_tab = "Impulsantwort"
        self.str_Analysefuktionen_tab = "Analysefunktionen"
        self._component = self.tabs(
            (self.str_signal_tab, 'No data chosen!'),
            (self.str_Spektrum_tab, 'No data chosen!'),
            (self.str_Impulsantwort_tab, 'No data chosen!'),
            (self.str_Analysefuktionen_tab, 'No data chosen!'),
            sizing_mode='stretch_width', dynamic=True)

    @property
    def component(self):
        return self._component
