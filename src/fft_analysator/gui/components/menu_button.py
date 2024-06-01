import panel as pn


class MenuButton:
    def __init__(self):
        self.file_items = ["\U0001F4BE Save", "📈 Korrelation", "📈 Leistungsdichte", "📈 Kohärenz", "📈 Impulsantwort", "📈 Frequenzgang"]
        self.help_items = ["📈 Calculations", "\U0001F6C8 About"]
        self._component = pn.Column(pn.Row(
                                pn.widgets.MenuButton(name="File", icon="file", items=self.file_items, width=150, button_type="default"),
                                pn.widgets.MenuButton(name="🔍 Help", items=self.help_items, width=125, button_type="default"),
                                styles={"border-bottom": "1px solid black"}, sizing_mode='stretch_width'
                                ), height=100
                            )

    @property
    def component(self):
        return self._component
