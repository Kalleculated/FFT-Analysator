import panel as pn

from tkinter import Tk, filedialog
import os

class Overlap_MenuButton:
    def __init__(self):
        self.file_items = ['None','50%','75%','87.5%']
        self.overlap_menu = pn.widgets.MenuButton(name="Overlap", icon="layers-intersect", items=self.file_items, width=150, button_type="default")

        self._component = pn.Column(pn.Row(
                                self.overlap_menu,
                                height = 30,
                                sizing_mode='stretch_width'
                                ),
                                pn.layout.Divider(margin=(5, 0, 5, 0)),
                                pn.bind(self.handle_selection, self.overlap_menu.param.clicked)
                            )

    def handle_selection(self, clicked):
            return f'The current overlap is: "{clicked}"'

    @property
    def component(self):
        return self._component
