
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
        """
        The update_multi_choice function is used to update the multi_choice component with new data.
        If a data_callback is provided, then the options of the multi_choice component are set to be
        the number of channels in that callback. The name of the component is also updated accordingly.
        Otherwise, if no data_callback was provided, then we assume that there's no file selected and
        we set both options and name to empty lists/strings respectively.

        Args:
            data_callback (object): Get the callback to the data object
        """
        if data_callback:
            self.accordion.multi_choice.component.name = "Wähle 1-2 Channel aus!"
            self.accordion.multi_choice.component.options = list(range(data_callback.get_channel_count()))
            self.accordion.multi_choice.component.max_items = 2

        else:
            self.accordion.multi_choice.component.name = "Keine Datei ausgewählt!"
            self.accordion.multi_choice.component.options = []

    def servable(self):
        return self.layout.servable(target="sidebar")
