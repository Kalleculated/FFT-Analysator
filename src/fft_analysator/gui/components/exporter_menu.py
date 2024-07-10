import panel as pn

from tkinter import Tk, filedialog
import os

class Exporter_MenuButton:
    def __init__(self):
        self.file_items = ['Numpy Array', 'Binary']
        self.export_menu = pn.widgets.MenuButton(name="Extension", icon="file", items=self.file_items, width=300, button_type="default")

        self._component = pn.Column(pn.Row(
                                self.export_menu,
                                height = 30,
                                sizing_mode='stretch_width'
                                ),
                                pn.layout.Divider(margin=(5, 0, 5, 0)),
                                pn.bind(self.handle_selection, self.export_menu.param.clicked)
                            )

    def handle_selection(self, clicked):
            return f'The current Extension is: "{clicked}"'

    @property
    def component(self):
        return self._component
