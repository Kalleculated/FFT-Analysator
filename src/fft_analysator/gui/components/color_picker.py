import panel as pn


class Colorpicker:
    def __init__(self):
        self.color_picker = pn.widgets.ColorPicker
        self._component = self.color_picker(name='', value='#FF0000', margin=(10, 15), visible=False)

    @property
    def component(self):
        return self._component
