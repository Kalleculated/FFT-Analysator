import panel as pn

class Window_MenuButton:
    def __init__(self):
        self.file_items = ['Rectangular','Hanning', 'Hamming', 'Bartlett', 'Blackman']
        self.window_menu = pn.widgets.MenuButton(name="Window", icon="window", items=self.file_items, width=150, button_type="default")

        self._component = pn.Column(pn.Row(
                                self.window_menu,
                                #self.help_menu,
                                height = 30,
                                sizing_mode='stretch_width'
                                ),
                                pn.layout.Divider(margin=(5, 0, 5, 0)),
                                pn.bind(self.handle_selection, self.window_menu.param.clicked)
                            )

    def handle_selection(self, clicked):
            return f'The current window is: "{clicked}"'

    @property
    def component(self):
        return self._component
