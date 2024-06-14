import panel as pn


class MenuButton:
    def __init__(self):
        self.file_items = ["\U0001F4BE Save", "Korrelation", "Leistungsdichte", "Kohärenz", "Impulsantwort", "Frequenzgang"]
        self.help_items = ["🧮 Calculations", "\U0001F6C8 About"]
        self.signal_menu = pn.widgets.MenuButton(name="Signal", icon="file", items=self.file_items, width=150, button_type="default")
        self.help_menu = pn.widgets.MenuButton(name="🔍 Help", items=self.help_items, width=125, button_type="default")

        self._component = pn.Column(pn.Row(
                                self.signal_menu,
                                self.help_menu,
                                height = 30,
                                sizing_mode='stretch_width'
                                ),
                                pn.layout.Divider(margin=(5, 0, 5, 0)),
                                pn.bind(self.handle_selection, self.signal_menu.param.clicked)
                            )

    def handle_selection(self, clicked):
        if clicked == self.file_items[0]:
            return pn.widgets.Button(name="Save", button_type="default", width=150)

        if clicked == self.file_items[1]:
            return f'You clicked menu item: "{clicked}"'

        else:
            return

    @property
    def component(self):
        return self._component
