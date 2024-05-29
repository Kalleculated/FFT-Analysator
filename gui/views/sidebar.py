
from gui.components.accordion import Accordion


class Sidebar:
    def __init__(self, callback_fileupload=None, callback=None):

        self.accordion = Accordion()
        self.layout = self.accordion._component

        if callback:
            self.accordion.file_input.component.param.watch(callback_fileupload, "value")
            self.accordion.stretching_switch.component.param.watch(callback, "value")
            self.accordion.multi_choice._component.param.watch(callback, "value")

    def update_multi_choice(self, data_callback):
        # Update the multi_choice component with the new data
        self.accordion.multi_choice._component.name = "Wähle 1-2 Channel aus!"
        self.accordion.multi_choice._component.options = list(range(data_callback.get_channel_count()))
        self.accordion.multi_choice._component.max_items = 2

    def servable(self):
        return self.layout.servable(target="sidebar")
