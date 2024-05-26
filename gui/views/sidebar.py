import panel as pn
from gui.components.file_input import FileInputComponent

class Sidebar:
    def __init__(self, callback=None):
        self.file_input = FileInputComponent()
        self.accordion = pn.Accordion(('Upload', self.file_input.component), ('Autokorrelation', "test"), sizing_mode='stretch_width')
        self.layout = pn.Column(self.accordion, sizing_mode='stretch_width')

        if callback:
            self.file_input.component.param.watch(callback, "value")
    
    def servable(self):
        return self.layout.servable(target="sidebar")