
from fft_analysator.gui.components.accordion import Accordion


class Sidebar:
    def __init__(self, callback_fileupload=None, callback=None):

        self.accordion = Accordion()
        self.layout = self.accordion.component

        if callback:
            self.accordion.file_input.component.param.watch(callback_fileupload, "value")
            self.accordion.stretching_switch.component.param.watch(callback, "value")
            self.accordion.multi_choice.component.param.watch(callback, "value")

    def update_multi_choice(self, data_callback=None):
        # Update the multi_choice component with the new data
        if data_callback:
            self.accordion.multi_choice.component.name = "Wähle 1-2 Channel aus!"
            self.accordion.multi_choice.component.options = list(range(data_callback.get_channel_count()))
            self.accordion.multi_choice.component.max_items = 2

        else:
            self.accordion.multi_choice.component.name = "Keine Datei ausgewählt!"
            self.accordion.multi_choice.component.options = []

    def servable(self):
        return self.layout.servable(target="sidebar")
