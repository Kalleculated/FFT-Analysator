import panel as pn
from gui.components.file_input import FileInputComponent
from gui.components.multi_choice import MultiChoice
import analysis.signal_processing as sp

class Sidebar:
    def __init__(self, callback=None):
        self.file_input = FileInputComponent()
        self.multi_choice = MultiChoice()
        self.accordion = pn.Accordion(('Upload', self.file_input.component), ('Plot', self.multi_choice._component), sizing_mode='stretch_width')
        self.layout = pn.Column(self.accordion, sizing_mode='stretch_width')

        if callback:
            self.file_input.component.param.watch(callback, "value")
            self.multi_choice._component.param.watch(callback, "value")
    
    def update_sidebar(self, data):
        # Update the multi_choice component with the new data
        self.multi_choice._component.name = "Wähle 1-2 Channel aus!"
        self.multi_choice._component.options = [i for i in range(data.shape[1])]
        self.multi_choice._component.max_items = 2

    def servable(self):
        return self.layout.servable(target="sidebar")