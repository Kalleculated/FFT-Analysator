import panel as pn
from gui.components.file_input import FileInputComponent
from gui.components.multi_choice import MultiChoice
from gui.components.accordion import Accordion
from gui.components.switch import Switch

class Sidebar:
    def __init__(self, callback_fileupload=None, callback=None):
        self.file_input = FileInputComponent()
        self.multi_choice = MultiChoice()
        self.stretching_switch = Switch()

        # We could also make accordion import the components it needs directly in its class definition, instead of passing them as arguments here. (makes sense since its a layout component)
        # Or we could also use **kwargs to pass the components here.
        self.accordion = Accordion(self.file_input, self.multi_choice, self.stretching_switch)
        self.layout = self.accordion._component

        if callback:
            self.file_input.component.param.watch(callback_fileupload, "value")
            self.stretching_switch.component.param.watch(callback, "value")
            self.multi_choice._component.param.watch(callback, "value")
    
    def update_multi_choice(self, data_callback):
        # Update the multi_choice component with the new data
        self.multi_choice._component.name = "Wähle 1-2 Channel aus!"
        self.multi_choice._component.options = [i for i in range(data_callback.get_channel_count())]
        self.multi_choice._component.max_items = 2

    def servable(self):
        return self.layout.servable(target="sidebar")