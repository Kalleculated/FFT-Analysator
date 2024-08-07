from fft_analysator.gui.components.accordion import Accordion
from os import path
import math


class Sidebar:
    """
    A class used to represent the sidebar of the application.

    This class is responsible for handling user interactions with the sidebar and updating the sidebar's state accordingly.

    Attributes:
        accordion (object):
            An instance of the Accordion class.
        layout (object):
            A panel Column layout containing the accordion component.
        ch (list):
            A list of selected channels.
        amount_ch (int):
            The number of selected channels.

    Methods:
        update_channel_selector(data_callback):
            Updates the channel selector based on the provided data.
        update_color_picker():
            Updates the color picker based on the selected channels.
    """

    def __init__(self, callback_fileupload=None, callback=None, callback_table_chooser=None, callback_intslider=None,
                 callback_block_selector=None, callback_analysis_event=None, callback_exporter_event=None,
                 callback_method_event=None):
        """
        Constructs all the necessary attributes for the Sidebar object.

        The accordion attribute is initialized as an Accordion instance.
        The layout attribute is initialized as a panel Column layout containing the accordion component.
        The ch attribute is initialized as an empty list.
        The amount_ch attribute is initialized as 0.

        Args:
            callback_fileupload (function, optional): A callback function for file upload events.
            callback (function, optional): A general callback function.
            callback_table_chooser (function, optional): A callback function for table chooser events.
            callback_intslider (function, optional): A callback function for intslider events.
            callback_block_selector (function, optional): A callback function for block selector events.
            callback_analysis_event (function, optional): A callback function for analysis events.
            callback_exporter_event (function, optional): A callback function for exporter events.
            callback_method_event (function, optional): A callback function for method events.
        """

        self.accordion = Accordion()
        self.layout = self.accordion.component

        if (callback or callback_fileupload or callback_table_chooser or callback_analysis_event or
            callback_exporter_event or callback_method_event):
            self.accordion.file_input.component.param.watch(callback_fileupload, "value")
            self.accordion.channel_selector_input.component.param.watch(callback, "value")
            self.accordion.channel_selector_output.component.param.watch(callback, "value")
            self.accordion.color_picker_ch1.component.param.watch(callback, "value")
            self.accordion.color_picker_ch2.component.param.watch(callback, "value")
            self.accordion.color_picker_result.component.param.watch(callback, "value")
            self.accordion.selector.component.param.watch(callback_table_chooser, "value")
            self.accordion.int_slider.component.param.watch(callback_intslider, "value")
            self.accordion.blocksize_selector.component.param.watch(callback_block_selector, "value")
            self.accordion.method_selector.component.param.watch(callback_analysis_event, "value")
            self.accordion.overlap_selector.component.param.watch(callback_analysis_event, "value")
            self.accordion.window_selector.component.param.watch(callback_analysis_event, "value")
            self.accordion.file_exporter.component.param.watch(callback_exporter_event, "value")
            self.accordion.method_selector.component.param.watch(callback_method_event, "value")
            self.accordion.toggle_group.component.param.watch(callback, "value")
            self.accordion.toggle_x_axis.component.param.watch(callback, "value")
            self.accordion.toggle_y_axis.component.param.watch(callback, "value")



    def update_channel_selector(self, data_callback=None):
        """
        Updates the channel selector based on the provided data.

        Args:
            data_callback (function): A callback function that returns the data to be used for updating the channel selector.

        Returns:
            None
        """
        if data_callback:
            self.accordion.channel_selector_output.component.disabled = False
            self.accordion.channel_selector_input.component.disabled = False
            self.accordion.channel_selector_output.component.name = "Output channel:"
            self.accordion.channel_selector_input.component.name = "Input channel:"
            self.accordion.channel_selector_input.component.options = (list(range(data_callback.get_channel_count())))
            self.accordion.channel_selector_output.component.options = (list(range(data_callback.get_channel_count())))
        else:
            self.accordion.channel_selector_output.component.name = "No data chosen!"
            self.accordion.channel_selector_input.component.name = "No data chosen!"
            self.accordion.channel_selector_input.component.options = []
            self.accordion.channel_selector_output.component.options = []
            self.accordion.channel_selector_output.component.disabled = True
            self.accordion.channel_selector_input.component.disabled = True

    def update_color_picker(self):
        """
        Updates the color picker based on the selected channels.

        Returns:
            None
        """
        # The selector always has a value, so we can check if the options are set
        if (self.accordion.channel_selector_input.component.value is not None
            and self.accordion.channel_selector_output.component.value is not None):

            self.ch = list(dict.fromkeys([self.accordion.channel_selector_input.component.value,
                                          self.accordion.channel_selector_output.component.value]))
            self.amount_ch = len(self.ch)

            if self.amount_ch == 1:
                self.accordion.color_picker_ch1.component.visible = True
                self.accordion.color_picker_ch2.component.visible = False
                self.accordion.color_picker_ch1.component.name = f'CH: {self.ch[0]}'
                self.accordion.color_picker_ch2.component.name = ''
                self.amount_ch = 0
            elif self.amount_ch == 2:
                self.accordion.color_picker_ch1.component.visible = True
                self.accordion.color_picker_ch2.component.visible = True
                self.accordion.color_picker_result.component.visible = True
                self.accordion.color_picker_ch1.component.name = f'CH: {self.ch[0]}'
                self.accordion.color_picker_ch2.component.name = f'CH: {self.ch[1]}'
                self.accordion.color_picker_result.component.name = f'Result'
                self.amount_ch = 0

        else:
            self.accordion.color_picker_ch1.component.visible = False
            self.accordion.color_picker_ch2.component.visible = False
            self.accordion.color_picker_result.component.visible = False
            self.accordion.color_picker_ch1.component.name = ''
            self.accordion.color_picker_ch2.component.name = ''
            self.accordion.color_picker_result.component.name = ''
            self.amount_ch = 0

    def update_selector(self, data_callback=None):
        """
        Updates the selector based on the provided data.

        Args:
            data_callback (function, optional): A callback function to retrieve the data. If not provided, the selector is cleared.

        Returns:
            bool: Always returns True.
        """
        if data_callback:
            self.accordion.selector.component.options = data_callback.get_table_names()
            self.accordion.selector.component.value = data_callback.get_table_names()[0]
            if (len(data_callback.get_table_names()) + 2) > 3:
                self.accordion.selector.component.size = len(data_callback.get_table_names()) + 2

        else:
            self.accordion.selector.component.options = []
            self.accordion.selector.component.value = ""

        return True

    def update_file_list(self):
        """
        Updates the file list based on the file paths in the file input component.

        Returns:
            None
        """
        if self.accordion.file_input.file_paths:
            self.accordion.data_selector.component.options = [path.basename(self.accordion.file_input.file_paths)]

        else:
            self.accordion.data_selector.component.options = []

    def update_intslider(self, data_callback=None):
        """
        Updates the integer slider and the navigation buttons based on the provided data.

        If the file paths attribute of the file input component is not empty and a data callback function is provided, the integer slider and the navigation buttons are enabled and updated based on the data. Otherwise, they are disabled.

        Args:
            data_callback (function, optional): A callback function to retrieve the data. If not provided, the integer slider and the navigation buttons are disabled.

        Returns:
            None
        """
        if self.accordion.file_input.file_paths and data_callback:
            self.accordion.int_slider.component.disabled = False
            self.accordion.int_slider.component.value = 0
            self.accordion.int_slider.component.start = 0
            self.accordion.int_slider.component.end = math.ceil(
                (data_callback.source.numsamples) / data_callback.block_size) - 1

            # update the navigation buttons as well since they are coupled with the int_slider
            self.accordion.gen_nav.index_box.disabled = False
            self.accordion.gen_nav.index_box.start = self.accordion.int_slider.component.start
            self.accordion.gen_nav.index_box.end = self.accordion.int_slider.component.end
            self.accordion.gen_nav.index_box.name = f'{self.accordion.int_slider.component.value}/{self.accordion.gen_nav.index_box.start}-{self.accordion.gen_nav.index_box.end}'
            self.accordion.gen_nav.button_back.disabled = False
            self.accordion.gen_nav.button_forward.disabled = False
            self.accordion.gen_nav.goto_button.disabled = False
            self.accordion.gen_nav.reset_button.disabled = False

        else:
            self.accordion.int_slider.component.disabled = True
            self.accordion.int_slider.component.value = 0

            # update the navigation buttons as well since they are coupled with the int_slider
            self.accordion.gen_nav.index_box.value = 0
            self.accordion.gen_nav.index_box.name = "Index:"
            self.accordion.gen_nav.index_box.disabled = True
            self.accordion.gen_nav.button_back.disabled = True
            self.accordion.gen_nav.button_forward.disabled = True
            self.accordion.gen_nav.goto_button.disabled = True
            self.accordion.gen_nav.reset_button.disabled = True

    def update_nav_index(self):
        """
        Updates the navigation index based on the current value of the integer slider.

        The navigation index is updated to a string of the format 'current value/start-end', where 'current value' is the current value of the integer slider, and 'start' and 'end' are the start and end values of the navigation index box.

        Returns:
            None
        """
        self.accordion.gen_nav.index_box.name = f'{self.accordion.int_slider.component.value}/{self.accordion.gen_nav.index_box.start}-{self.accordion.gen_nav.index_box.end}'

    def update_general_plotting_widgets(self, data_callback=None):
        """
        Updates the general plotting widgets based on the provided data.

        If a data callback function is provided, the widgets are enabled. Otherwise, they are disabled.

        Args:
            data_callback (function, optional): A callback function to retrieve the data. If not provided, the widgets are disabled.

        Returns:
            None
        """
        if data_callback:
            self.accordion.toggle_group.component.disabled = False
            self.accordion.toggle_x_axis.component.disabled = False
            self.accordion.toggle_y_axis.component.disabled = False
            self.accordion.window_selector.component.disabled = False
            self.accordion.overlap_selector.component.disabled = False
            self.accordion.method_selector.component.disabled = False
        else:
            self.accordion.toggle_group.component.disabled = True
            self.accordion.toggle_x_axis.component.disabled = True
            self.accordion.toggle_y_axis.component.disabled = True
            self.accordion.window_selector.component.disabled = True
            self.accordion.overlap_selector.component.disabled = True
            self.accordion.method_selector.component.disabled = True

    def update_exporter(self, method_callback=None):
        """
        Updates the exporter based on the provided method callback.

        If the method callback is "No Analysis Function" or None, the exporter selector and the file exporter are disabled. Otherwise, they are enabled.

        Args:
            method_callback (function, optional): A callback function to retrieve the method. If not provided or if it is "No Analysis Function", the exporter selector and the file exporter are disabled.

        Returns:
            None
        """
        if method_callback == "No Analysis Function" or method_callback is None:
            self.accordion.exporter_selector.component.disabled = True
            self.accordion.file_exporter.component.disabled = True
        else:
            self.accordion.exporter_selector.component.disabled = False
            self.accordion.file_exporter.component.disabled = False

    def update_toggle_group(self):
        """
        Updates the toggle group based on its current value.

        If 'Stretch' is in the toggle group's value, the stretch attribute of the toggle group is set to True. Otherwise, it is set to False.
        If 'Grid' is in the toggle group's value, the grid attribute of the toggle group is set to True. Otherwise, it is set to False.

        Returns:
            None
        """
        if 'Stretch' in self.accordion.toggle_group.component.value:
            self.accordion.toggle_group.stretch = True
        else:
            self.accordion.toggle_group.stretch = False

        if 'Grid' in self.accordion.toggle_group.component.value:
            self.accordion.toggle_group.grid = True
        else:
            self.accordion.toggle_group.grid = False

        if self.accordion.toggle_x_axis.component.value == 'x-log':
            self.accordion.toggle_x_axis.x_log = True
        else:
            self.accordion.toggle_x_axis.x_log = False

        if self.accordion.toggle_y_axis.component.value == 'y-log':
            self.accordion.toggle_y_axis.y_log = True
        else:
            self.accordion.toggle_y_axis.y_log = False

        if "dB" in self.accordion.toggle_group.component.value:
            self.accordion.toggle_group.db = True
        else:
            self.accordion.toggle_group.db = False

    def servable(self):
        """
        Makes the sidebar servable.
        """
        return self.layout.servable(target="sidebar")
