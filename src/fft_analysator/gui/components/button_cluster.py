import panel as pn


class GeneratorNavigator:
    def __init__(self):
        self.button_back = pn.widgets.Button(name='\u25c0', button_type='default', margin=(2, 5, 5, 5))
        self.button_forward = pn.widgets.Button(name='\u25b6', button_type='default', margin=(2, 5, 5, 5))
        self.reset_button = pn.widgets.Button(name='\u21ba', button_type='default', margin=(2, 5, 5, 5))
        self.index_box = pn.widgets.TextInput(name='Block index:', value='0', margin=(-20, 20, 0, 10), disabled=True, width=80)
        self.goto_button = pn.widgets.Button(name='Go', button_type='default', margin=(2, 5, 5, 5))
        self._component = pn.Row(self.goto_button, self.index_box, self.button_back, self.reset_button, self.button_forward,
                                 margin=(5, 5, 10, 5))

    @property
    def component(self):
        return self._component
