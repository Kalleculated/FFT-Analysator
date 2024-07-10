import panel as pn


class MenuButton:
    def __init__(self):
        self.file_items = ["No Analysis Function", "Auto Spectral Density - Input", "Auto Spectral Density - Output",
                           "Cross Spectral Density", "Coherence","Auto Correlation - Input", "Auto Correlation - Output", "Cross Correlation"]
        self.signal_menu = pn.widgets.MenuButton(name="Method", icon="file", items=self.file_items, width=300, button_type="default")

        self._component = pn.Column(pn.Row(
                                self.signal_menu,
                                #self.help_menu,
                                height = 30,
                                sizing_mode='stretch_width'
                                ),
                                pn.layout.Divider(margin=(5, 0, 5, 0)),
                                pn.bind(self.handle_selection, self.signal_menu.param.clicked)
                            )

    def handle_selection(self, clicked):
        if clicked == self.file_items[0]:
            return pn.widgets.Button(name="Save", button_type="default", width=150)

        else:

            return f'Go to the Analysis Functions tab to view: "{clicked}"'

    @property
    def component(self):
        return self._component
