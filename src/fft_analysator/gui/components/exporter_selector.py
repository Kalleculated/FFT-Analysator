import panel as pn

class ExporterSelector:
    def __init__(self):
        self.export_selector = pn.widgets.Select
        self.options = ['Numpy Array', 'Binary']
        self._component = self.export_selector(name='Choose export extension:', options=self.options, width=300,
                                               value='Numpy Array', disabled=True)
    @property
    def component(self):
        return self._component
