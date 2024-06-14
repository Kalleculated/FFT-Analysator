import panel as pn


class MenuButton:
    def __init__(self):
        self.file_items = ["\U0001F4BE Save", "📈 Korrelation", "📈 Leistungsdichte", "📈 Kohärenz", "📈 Impulsantwort", "📈 Frequenzgang"]
        self.help_items = ["📈 Calculations", "\U0001F6C8 About"]

        # need this to create widgets depending on the chosen menu items
        self.calculation_widgets = pn.Column()
        self._component = pn.Column(pn.Row(
                                pn.widgets.MenuButton(name="File", icon="file", items=self.file_items, width=150, button_type="default"),
                                pn.widgets.MenuButton(name="🔍 Help", items=self.help_items, width=125, button_type="default"),
                                height = 30,
                                sizing_mode='stretch_width'
                                ),
                                pn.layout.Divider(margin=(5, 0, 5, 0)),
                                self.calculation_widgets
                            )

    @property
    def component(self):
        return self._component
