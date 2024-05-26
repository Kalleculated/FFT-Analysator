import panel as pn
from gui.components.file_input import FileInputComponent

class Sidebar:
    def __init__(self):
        self.file_input = FileInputComponent()
        self.accordion = pn.Accordion(('Upload', self.file_input.component), ('Autokorrelation', "test"), sizing_mode='stretch_width')
        self.layout = pn.Column(self.accordion, sizing_mode='stretch_width')
    
    def servable(self):
        return self.layout.servable(target="sidebar")