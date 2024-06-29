import holoviews as hv
import panel as pn

import fft_analysator.analysis.preprocessing as pp
from fft_analysator.gui.views.main_view import MainView
from fft_analysator.gui.views.sidebar import Sidebar


hv.extension("bokeh", "plotly")  # type: ignore


class AppController:
    def __init__(self):

        # Initialization of main and side views
        self.main_view = MainView()
        self.sidebar = Sidebar(self.handle_fileupload_event, self.handle_sidebar_event, self.handle_table_choose_event,
                                self.handle_intslider_event, self.handle_blocksize_selector_event)

        # Initialization of panel extensions and template
        self.template_layout = pn.template.FastListTemplate(title="FFT-Analysator",
                                                            header_background="#E91E63",
                                                            accent_base_color="#E91E63",
                                                            theme="dark",
                                                            sidebar=self.sidebar.layout,
                                                            main=self.main_view.layout
                                                            )

        # Initialization of data preprocessing and binary file
        self.file_paths = None
        self.preprocessing = None

    def handle_fileupload_event(self, event):
        # Handle the file upload event and update the preprocessing object
        self.file_paths = self.sidebar.accordion.file_input.file_paths

        if self.file_paths:
            self.preprocessing = pp.Preprocess(self.file_paths, self.sidebar.accordion.blocksize_selector.component.value)
            if event.obj == self.sidebar.accordion.file_input.component:
                self.sidebar.update_file_list()
                self.sidebar.update_selector(self.preprocessing)
                self.sidebar.update_channel_selector(self.preprocessing)
                self.sidebar.update_intslider(self.preprocessing)
                self.sidebar.update_general_plotting_widgets(self.preprocessing)

        else:
            self.sidebar.update_file_list()
            self.sidebar.update_selector()
            self.sidebar.update_channel_selector()
            self.sidebar.update_intslider()
            self.sidebar.update_general_plotting_widgets()

    def handle_sidebar_event(self, event):
        # Update the main view when the sidebar event is triggered
        if ((
            event.obj == self.sidebar.accordion.stretching_switch.component
            or event.obj == self.sidebar.accordion.color_picker_ch1.component
            or event.obj == self.sidebar.accordion.color_picker_ch2.component
            or event.obj == self.sidebar.accordion.channel_selector_input.component
            or event.obj == self.sidebar.accordion.channel_selector_output.component)
            and self.file_paths
            and self.sidebar.accordion.channel_selector_input.component.value is not None
            and self.sidebar.accordion.channel_selector_output.component.value is not None):
            # Update the color picker
            self.sidebar.update_color_picker()

            # Update signal
            self.main_view.update_signal(
                self.preprocessing,
                {self.sidebar.accordion.channel_selector_input.component.value,
                self.sidebar.accordion.channel_selector_output.component.value},
                self.sidebar.accordion.stretching_switch.component.value,
                [self.sidebar.accordion.color_picker_ch1.component.value,
                self.sidebar.accordion.color_picker_ch2.component.value],
            )

        else:
            self.sidebar.update_color_picker()
            self.main_view.update_signal(
                self.preprocessing,
                [],
                self.sidebar.accordion.stretching_switch.component.value,
                [self.sidebar.accordion.color_picker_ch1.component.value,
                self.sidebar.accordion.color_picker_ch2.component.value],

            )

    def handle_table_choose_event(self, event):
        # Update the main view when the table chooser event is triggered
        # Note, we could also split this into multiple functions
        if event.obj == self.sidebar.accordion.selector.component:
            if self.sidebar.accordion.selector.component.value:
                self.preprocessing.table_key = self.sidebar.accordion.selector.component.value
                self.preprocessing.converted_file = self.preprocessing.convert_data()
                self.sidebar.update_channel_selector(self.preprocessing)

    def handle_intslider_event(self, event):
        if (self.sidebar.accordion.int_slider.component.value > self.preprocessing.current_block_idx):
            for _ in range(self.sidebar.accordion.int_slider.component.value - self.preprocessing.current_block_idx):
                self.preprocessing.set_next_data_block()

            self.sidebar.update_color_picker()
            self.main_view.update_signal(
                self.preprocessing,
                {self.sidebar.accordion.channel_selector_input.component.value,
                self.sidebar.accordion.channel_selector_output.component.value},
                self.sidebar.accordion.stretching_switch.component.value,
                [self.sidebar.accordion.color_picker_ch1.component.value,
                self.sidebar.accordion.color_picker_ch2.component.value],

            )
        else:
            self.preprocessing.set_data_block_to_idx(self.sidebar.accordion.int_slider.component.value)
            self.sidebar.update_color_picker()
            self.main_view.update_signal(
                self.preprocessing,
                {self.sidebar.accordion.channel_selector_input.component.value,
                self.sidebar.accordion.channel_selector_output.component.value},
                self.sidebar.accordion.stretching_switch.component.value,
                [self.sidebar.accordion.color_picker_ch1.component.value,
                self.sidebar.accordion.color_picker_ch2.component.value],

            )

    def handle_blocksize_selector_event(self, event):
        if self.file_paths:
            # reinitalize the preprocessing object with the new blocksize
            self.preprocessing = pp.Preprocess(self.file_paths, self.sidebar.accordion.blocksize_selector.component.value)

            # update the sidebar components
            self.sidebar.update_file_list()
            self.sidebar.update_selector(self.preprocessing)
            self.sidebar.update_channel_selector(self.preprocessing)
            self.sidebar.update_intslider(self.preprocessing)
            self.main_view.update_signal(
                self.preprocessing,
                {self.sidebar.accordion.channel_selector_input.component.value,
                self.sidebar.accordion.channel_selector_output.component.value},
                self.sidebar.accordion.stretching_switch.component.value,
                [self.sidebar.accordion.color_picker_ch1.component.value,
                self.sidebar.accordion.color_picker_ch2.component.value],
            )

    def servable(self):
        # Serve app layout
        self.template_layout.servable()
