from fft_analysator.gui.components.accordion import Accordion
from os import path
import math


class Sidebar:
    """
    A class used to represent the sidebar of the application.

    This class is responsible for handling user interactions with the sidebar and updating the sidebar's state accordingly.

    Attributes
    ----------
    accordion : object
        An instance of the Accordion class.
    layout : object
        A panel Column layout containing the accordion component.
    ch : list
        A list of selected channels.
    amount_ch : int
        The number of selected channels.

    Methods
    -------
    update_channel_selector(data_callback)
        Updates the channel selector based on the provided data.
    update_color_picker()
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
                """

        self.accordion = Accordion()
        self.layout = self.accordion.component

        if (callback or callback_fileupload or callback_table_chooser or callback_analysis_event or
            callback_exporter_event or callback_method_event):
            self.accordion.file_input.component.param.watch(callback_fileupload, "value")
            self.accordion.stretching_switch.component.param.watch(callback, "value")
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

    def update_channel_selector(self, data_callback=None):
        """
        Updates the channel selector based on the provided data.

        Parameters
        ----------
        data_callback : function
            A callback function to retrieve the data.
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

        Parameters
        ----------
        data_callback : function, optional
            A callback function to retrieve the data. If not provided, the selector is cleared.
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
        """
        if self.accordion.file_input.file_paths:
            self.accordion.data_selector.component.options = [path.basename(self.accordion.file_input.file_paths)]

        else:
            self.accordion.data_selector.component.options = []

    def update_intslider(self, data_callback=None):
        """
        Updates the integer slider and the navigation buttons based on the provided data.

        Parameters
        ----------
        data_callback : function, optional
            A callback function to retrieve the data. If not provided, the integer slider and the navigation buttons are disabled.
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
        Updates the navigation index based on the provided index.

        Parameters
        ----------
        index : int
            The index to update the navigation index to.
        """
        self.accordion.gen_nav.index_box.name = f'{self.accordion.int_slider.component.value}/{self.accordion.gen_nav.index_box.start}-{self.accordion.gen_nav.index_box.end}'

    def update_general_plotting_widgets(self, data_callback=None):
        """
        Updates the general plotting widgets based on the provided data.

        Parameters
        ----------
        data_callback : function, optional
            A callback function to retrieve the data. If not provided, the widgets are disabled.
        """
        if data_callback:
            self.accordion.stretching_switch.component.disabled = False
            self.accordion.window_selector.component.disabled = False
            self.accordion.overlap_selector.component.disabled = False
            self.accordion.method_selector.component.disabled = False
        else:
            self.accordion.stretching_switch.component.disabled = True
            self.accordion.window_selector.component.disabled = True
            self.accordion.overlap_selector.component.disabled = True
            self.accordion.method_selector.component.disabled = True

    def update_exporter(self, method_callback=None):
        if method_callback == "No Analysis Function" or method_callback is None:
            self.accordion.exporter_selector.component.disabled = True
            self.accordion.file_exporter.component.disabled = True
        else:
            self.accordion.exporter_selector.component.disabled = False
            self.accordion.file_exporter.component.disabled = False

    def servable(self):
        """
        Makes the sidebar servable.
        """
        return self.layout.servable(target="sidebar")
