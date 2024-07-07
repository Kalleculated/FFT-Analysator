import panel as pn


class Tabs:
    def __init__(self):
        self.tabs = pn.Tabs
        self.str_signal_tab = "Input/Output"
        self.str_frequency_response_tab = "Frequency Response"
        self.str_impulse_response_tab = "Impulse Response"
        self.str_analysis_function_tab = "Analysis Functions"
        self._component = self.tabs(
            (self.str_signal_tab, 'No data chosen!'),
            (self.str_frequency_response_tab, 'No data chosen!'),
            (self.str_impulse_response_tab, 'No data chosen!'),
            (self.str_analysis_function_tab, 'No data chosen!'),
            sizing_mode='stretch_width', dynamic=True)

    @property
    def component(self):
        return self._component
