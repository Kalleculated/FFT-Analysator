import panel as pn


class IntSlider:
    def __init__(self):
        self.int_slider = pn.widgets.IntSlider
        self._component = self.int_slider(name='Current Block', start=0, step=1, margin=(15, 20, 25, 20),
        sizing_mode='stretch_width', disabled=True, align='start')

    @property
    def component(self):
        return self._component
