
from fft_analysator.gui.components.accordion import Accordion
from os import path
import math


class Sidebar:
    def __init__(self, callback_fileupload=None, callback=None, callback_table_chooser=None, callback_intslider=None,
                 callback_block_selector=None):

        self.accordion = Accordion()
        self.layout = self.accordion.component

        if callback or callback_fileupload or callback_table_chooser:
            self.accordion.file_input.component.param.watch(callback_fileupload, "value")
            self.accordion.stretching_switch.component.param.watch(callback, "value")
            self.accordion.multi_choice.component.param.watch(callback, "value")
            self.accordion.color_picker_ch1.component.param.watch(callback, "value")
            self.accordion.color_picker_ch2.component.param.watch(callback, "value")
            self.accordion.selector.component.param.watch(callback_table_chooser, "value")
            self.accordion.int_slider.component.param.watch(callback_intslider, "value")
            self.accordion.blocksize_selector.component.param.watch(callback_block_selector, "value")

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
            self.accordion.multi_choice.component.name = "Choose input channel:"
            self.accordion.multi_choice.component.value = []
            self.accordion.multi_choice.component.options = (
                list(range(data_callback.get_channel_count()))
            )
            self.accordion.multi_choice.component.max_items = 2

            self.accordion.channel_selector_output.component.disabled = False
            self.accordion.channel_selector_input.component.disabled = False
            self.accordion.channel_selector_output.component.name = "Output channel:"
            self.accordion.channel_selector_input.component.name = "Input channel:"
            self.accordion.channel_selector_input.component.options = (list(range(data_callback.get_channel_count())))
            self.accordion.channel_selector_output.component.options = (list(range(data_callback.get_channel_count())))

        else:
            self.accordion.multi_choice.component.name = "No data chosen!"
            self.accordion.multi_choice.component.options = []

            self.accordion.channel_selector_output.component.name = "No data chosen!"
            self.accordion.channel_selector_input.component.name = "No data chosen!"

    def update_color_picker(self):

        # Get amount of channels
        if self.accordion.multi_choice.component.value:
            # self.ch = self.accordion.multi_choice.component.value
            # values can only be converted through iteration
            self.ch = [int(item) for item in self.accordion.multi_choice.component.value]
            self.amount_ch = 0
            for _ in self.accordion.multi_choice.component.value:
                self.amount_ch += 1

            if self.amount_ch == 1:
                self.accordion.color_picker_ch1.component.visible = True
                self.accordion.color_picker_ch2.component.visible = False
                self.accordion.color_picker_ch1.component.name = f'CH: {self.ch[0]}'
                self.accordion.color_picker_ch2.component.name = ''
                self.amount_ch = 0
            elif self.amount_ch == 2:
                self.accordion.color_picker_ch1.component.visible = True
                self.accordion.color_picker_ch2.component.visible = True
                self.accordion.color_picker_ch1.component.name = f'CH: {self.ch[0]}'
                self.accordion.color_picker_ch2.component.name = f'CH: {self.ch[1]}'
                self.amount_ch = 0
        else:
            self.accordion.color_picker_ch1.component.visible = False
            self.accordion.color_picker_ch2.component.visible = False
            self.accordion.color_picker_ch1.component.name = ''
            self.accordion.color_picker_ch2.component.name = ''
            self.amount_ch = 0

    def update_selector(self, data_callback=None):

        if data_callback:
            self.accordion.selector.component.options = data_callback.get_table_names()
            self.accordion.selector.component.value = data_callback.get_table_names()[0]
            if (len(data_callback.get_table_names()) + 2) > 3:
                self.accordion.selector.component.size = len(data_callback.get_table_names()) + 1

        else:
            self.accordion.selector.component.options = []
            self.accordion.selector.component.value = ""

        return True

    def update_file_list(self):
        if self.accordion.file_input.file_paths:
            self.accordion.data_selector.component.options = [path.basename(self.accordion.file_input.file_paths)]
        else:
            self.accordion.data_selector.component.options = []

    def update_intslider(self, data_callback=None):
        if self.accordion.file_input.file_paths:
            self.accordion.int_slider.component.disabled = False
            self.accordion.int_slider.component.value = 0
            self.accordion.int_slider.component.start = 0
            self.accordion.int_slider.component.end = math.ceil(data_callback.get_abtastrate()/data_callback.block_size)-1

            # update the navigation buttons as well since they are coupled with the int_slider
            self.accordion.gen_nav.index_box.disabled = False
            self.accordion.gen_nav.index_box.start = self.accordion.int_slider.component.start
            self.accordion.gen_nav.index_box.end = self.accordion.int_slider.component.end
            self.accordion.gen_nav.index_box.name = f'{self.accordion.gen_nav.index_box.start} - {self.accordion.gen_nav.index_box.end}'
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

    def update_general_plotting_widgets(self, data_callback=None):
        if data_callback:
            self.accordion.stretching_switch.component.disabled = False
        else:
            self.accordion.stretching_switch.component.disabled = True

    def servable(self):
        return self.layout.servable(target="sidebar")
