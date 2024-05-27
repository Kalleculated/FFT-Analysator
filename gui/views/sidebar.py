import panel as pn
from gui.components.file_input import FileInputComponent
from gui.components.multi_choice import MultiChoice
from gui.components.accordion import Accordion

class Sidebar:
    def __init__(self, callback=None):
        self.file_input = FileInputComponent()
        self.multi_choice = MultiChoice()
        self.accordion = Accordion(self.file_input, self.multi_choice)
        self.layout = pn.Column(self.accordion._component, sizing_mode='stretch_width')

        if callback:
            self.file_input.component.param.watch(callback, "value")
            self.multi_choice._component.param.watch(callback, "value")
    
    def update_sidebar(self, data_callback):
        # Update the multi_choice component with the new data
        self.multi_choice._component.name = "Wähle 1-2 Channel aus!"
        self.multi_choice._component.options = [i for i in range(data_callback.get_channel_count())]
        self.multi_choice._component.max_items = 2

    def servable(self):
        return self.layout.servable(target="sidebar")