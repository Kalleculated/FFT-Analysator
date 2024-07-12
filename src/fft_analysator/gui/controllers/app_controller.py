import holoviews as hv
import panel as pn
import numpy as np

import fft_analysator.analysis.preprocessing as pp
import fft_analysator.analysis.signal_processing as sp
from fft_analysator.gui.views.main_view import MainView
from fft_analysator.gui.views.sidebar import Sidebar
from fft_analysator.analysis.signal_processing import Signal_Process


hv.extension("bokeh", "plotly")  # type: ignore


class AppController:
    """
    A class used to control the application's logic.

    This class is responsible for handling user interactions and updating the application's state accordingly.

    Attributes
    ----------
    main_view : object
        An instance of the MainView class.
    current_method : str
        The currently selected analysis method.
    sidebar : object
        An instance of the Sidebar class.
    template_layout : object
        A FastListTemplate instance for the application layout.
    file_paths : str
        The paths to the data files.

    Methods
    -------
    handle_fileupload_event()
        Handles the file upload event.
    handle_sidebar_event()
        Handles the sidebar event.
    handle_table_choose_event()
        Handles the table choose event.
    handle_intslider_event()
        Handles the intslider event.
    handle_blocksize_selector_event()
        Handles the blocksize selector event.
    handle_update_analysis_event()
        Handles the update analysis event.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the AppController object.

        The main_view attribute is initialized as a MainView instance.
        The current_method attribute is initialized with a string value.
        The sidebar attribute is initialized as a Sidebar instance with specific event handlers.
        The template_layout attribute is initialized as a FastListTemplate instance with specific parameters.
        The file_paths attribute is initialized as None.
        """
        # Initialization of main and side views
        self.main_view = MainView()
        self.current_method = 'No Analysis Function'
        self.sidebar = Sidebar(self.handle_fileupload_event, self.handle_sidebar_event, self.handle_table_choose_event,
                                self.handle_intslider_event, self.handle_blocksize_selector_event, self.handle_update_analysis_event,
                                self.handle_export_event)

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
        """
        Handles the file upload event.

        This method is called when a file upload event occurs.
        """
        # Handle the file upload event and update the preprocessing object
        self.file_paths = self.sidebar.accordion.file_input.file_paths

        if self.file_paths:
            self.preprocessing = pp.Preprocess(self.file_paths, self.sidebar.accordion.blocksize_selector.component.value)
            self.signal_process = Signal_Process(channels=[], file_path=self.file_paths,
                                                block_size=self.sidebar.accordion.blocksize_selector.component.value)
            # signal_process insert
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
        """
        Handles the sidebar event.

        This method is called when a sidebar event occurs.
        """
        # Update the main view when the sidebar event is triggered
        if ((
            event.obj == self.sidebar.accordion.stretching_switch.component
            or event.obj == self.sidebar.accordion.color_picker_ch1.component
            or event.obj == self.sidebar.accordion.color_picker_ch2.component
            or event.obj == self.sidebar.accordion.color_picker_result.component
            or event.obj == self.sidebar.accordion.channel_selector_input.component
            or event.obj == self.sidebar.accordion.channel_selector_output.component
            or event.obj == self.sidebar.accordion.calculation_menu.signal_menu.clicked
            or event.obj == self.sidebar.accordion.overlap_menu.overlap_menu.clicked
            or event.obj == self.sidebar.accordion.window_menu.window_menu.clicked

            or event.obj == self.sidebar.accordion.method_selector.component
            or event.obj == self.sidebar.accordion.overlap_selector.component
            or event.obj == self.sidebar.accordion.window_selector.component
        )
            and self.file_paths
            and self.sidebar.accordion.channel_selector_input.component.value is not None
            and self.sidebar.accordion.channel_selector_output.component.value is not None):

            # Update the color picker
            self.sidebar.update_color_picker()
            # Update signal
            self.main_view.update_signal(
                self.preprocessing,
                self.signal_process,
                [self.sidebar.accordion.channel_selector_input.component.value,
                self.sidebar.accordion.channel_selector_output.component.value],
                self.sidebar.accordion.stretching_switch.component.value,
                [self.sidebar.accordion.color_picker_ch1.component.value,
                self.sidebar.accordion.color_picker_ch2.component.value,
                self.sidebar.accordion.color_picker_result.component.value],
                self.sidebar.accordion.window_selector.component.value,
                self.sidebar.accordion.overlap_selector.component.value
            )

            self.main_view.update_analysis_plot(
                        self.preprocessing,
                        self.signal_process,
                        [self.sidebar.accordion.channel_selector_input.component.value,
                        self.sidebar.accordion.channel_selector_output.component.value],
                        self.sidebar.accordion.stretching_switch.component.value,
                        [self.sidebar.accordion.color_picker_ch1.component.value,
                        self.sidebar.accordion.color_picker_ch2.component.value,
                        self.sidebar.accordion.color_picker_result.component.value],
                        self.sidebar.accordion.method_selector.component.value,
                        self.sidebar.accordion.window_selector.component.value,
                        self.sidebar.accordion.overlap_selector.component.value
                    )
        else:

            self.sidebar.update_color_picker()
            self.main_view.update_signal(
                self.preprocessing,
                self.signal_process,
                [],
                self.sidebar.accordion.stretching_switch.component.value,
                [self.sidebar.accordion.color_picker_ch1.component.value,
                self.sidebar.accordion.color_picker_ch2.component.value,
                self.sidebar.accordion.color_picker_result.component.value],
                self.sidebar.accordion.window_selector.component.value,
                self.sidebar.accordion.overlap_selector.component.value
            )

            self.main_view.update_analysis_plot(
                        self.preprocessing,
                        self.signal_process,
                        [],
                        self.sidebar.accordion.stretching_switch.component.value,
                        [self.sidebar.accordion.color_picker_ch1.component.value,
                        self.sidebar.accordion.color_picker_ch2.component.value,
                        self.sidebar.accordion.color_picker_result.component.value],
                        self.sidebar.accordion.method_selector.component.value,
                        self.sidebar.accordion.window_selector.component.value,
                        self.sidebar.accordion.overlap_selector.component.value
                    )

    def handle_table_choose_event(self, event):
        """
        Handles the table choose event.

        This method is called when a table choose event occurs.
        """
        # Update the main view when the table chooser event is triggered
        # Note, we could also split this into multiple functions
        if event.obj == self.sidebar.accordion.selector.component:
            if self.sidebar.accordion.selector.component.value:
                self.preprocessing.table_key = self.sidebar.accordion.selector.component.value
                self.sidebar.update_channel_selector(self.preprocessing)

    def handle_intslider_event(self, event):
        """
        Handles the intslider event.

        This method is called when an intslider event occurs.
        """
        if self.file_paths:
            if (self.sidebar.accordion.int_slider.component.value > self.preprocessing.current_block_idx):
                for _ in range(self.sidebar.accordion.int_slider.component.value - self.preprocessing.current_block_idx):
                    self.preprocessing.set_next_data_block()

                self.sidebar.update_color_picker()
                self.sidebar.update_nav_index()
                self.main_view.update_signal(
                    self.preprocessing,
                    self.signal_process,
                    [self.sidebar.accordion.channel_selector_input.component.value,
                    self.sidebar.accordion.channel_selector_output.component.value],
                    self.sidebar.accordion.stretching_switch.component.value,
                    [self.sidebar.accordion.color_picker_ch1.component.value,
                    self.sidebar.accordion.color_picker_ch2.component.value,
                    self.sidebar.accordion.color_picker_result.component.value],
                    self.sidebar.accordion.window_selector.component.value,
                    self.sidebar.accordion.overlap_selector.component.value
                )
            else:
                self.preprocessing.set_data_block_to_idx(self.sidebar.accordion.int_slider.component.value)
                self.sidebar.update_color_picker()
                self.sidebar.update_nav_index()
                self.main_view.update_signal(
                    self.preprocessing,
                    self.signal_process,
                    [self.sidebar.accordion.channel_selector_input.component.value,
                    self.sidebar.accordion.channel_selector_output.component.value],
                    self.sidebar.accordion.stretching_switch.component.value,
                    [self.sidebar.accordion.color_picker_ch1.component.value,
                    self.sidebar.accordion.color_picker_ch2.component.value,
                    self.sidebar.accordion.color_picker_result.component.value],
                    self.sidebar.accordion.window_selector.component.value,
                    self.sidebar.accordion.overlap_selector.component.value
                )

    def handle_blocksize_selector_event(self, event):
        """
        Handles the blocksize selector event.

        This method is called when a blocksize selector event occurs.
        """
        if self.file_paths:
            # reinitalize the preprocessing object with the new blocksize
            self.preprocessing = pp.Preprocess(self.file_paths, self.sidebar.accordion.blocksize_selector.component.value)
            self.signal_process = Signal_Process(channels=[], file_path=self.file_paths,
                                                block_size=self.sidebar.accordion.blocksize_selector.component.value)

            # update the sidebar components
            self.sidebar.update_file_list()
            self.sidebar.update_selector(self.preprocessing)
            self.sidebar.update_channel_selector(self.preprocessing)
            self.sidebar.update_intslider(self.preprocessing)
            self.main_view.update_signal(
                self.preprocessing,
                self.signal_process,
                [self.sidebar.accordion.channel_selector_input.component.value,
                self.sidebar.accordion.channel_selector_output.component.value],
                self.sidebar.accordion.stretching_switch.component.value,
                [self.sidebar.accordion.color_picker_ch1.component.value,
                self.sidebar.accordion.color_picker_ch2.component.value,
                self.sidebar.accordion.color_picker_result.component.value],
                self.sidebar.accordion.window_selector.component.value,
                self.sidebar.accordion.overlap_selector.component.value
            )
            self.main_view.update_analysis_plot(
                        self.preprocessing,
                        self.signal_process,
                        [self.sidebar.accordion.channel_selector_input.component.value,
                        self.sidebar.accordion.channel_selector_output.component.value],
                        self.sidebar.accordion.stretching_switch.component.value,
                        [self.sidebar.accordion.color_picker_ch1.component.value,
                        self.sidebar.accordion.color_picker_ch2.component.value,
                        self.sidebar.accordion.color_picker_result.component.value],
                        self.sidebar.accordion.method_selector.component.value,
                        self.sidebar.accordion.window_selector.component.value,
                        self.sidebar.accordion.overlap_selector.component.value
                    )

    def handle_update_analysis_event(self, event):
        """
        Handles the update analysis event.

        This method is called when an update analysis event occurs.
        """
        if (self.file_paths
            and self.sidebar.accordion.channel_selector_input.component.value is not None
            and self.sidebar.accordion.channel_selector_output.component.value is not None):

            self.main_view.update_signal(
                self.preprocessing,
                self.signal_process,
                [self.sidebar.accordion.channel_selector_input.component.value,
                self.sidebar.accordion.channel_selector_output.component.value],
                self.sidebar.accordion.stretching_switch.component.value,
                [self.sidebar.accordion.color_picker_ch1.component.value,
                self.sidebar.accordion.color_picker_ch2.component.value,
                self.sidebar.accordion.color_picker_result.component.value],
                self.sidebar.accordion.window_selector.component.value,
                self.sidebar.accordion.overlap_selector.component.value
            )

            self.main_view.update_analysis_plot(
                        self.preprocessing,
                        self.signal_process,
                        [self.sidebar.accordion.channel_selector_input.component.value,
                        self.sidebar.accordion.channel_selector_output.component.value],
                        self.sidebar.accordion.stretching_switch.component.value,
                        [self.sidebar.accordion.color_picker_ch1.component.value,
                        self.sidebar.accordion.color_picker_ch2.component.value,
                        self.sidebar.accordion.color_picker_result.component.value],
                        self.sidebar.accordion.method_selector.component.value,
                        self.sidebar.accordion.window_selector.component.value,
                        self.sidebar.accordion.overlap_selector.component.value
                    )
        else:
            self.main_view.update_signal(
                self.preprocessing,
                self.signal_process,
                [self.sidebar.accordion.channel_selector_input.component.value,
                self.sidebar.accordion.channel_selector_output.component.value],
                self.sidebar.accordion.stretching_switch.component.value,
                [self.sidebar.accordion.color_picker_ch1.component.value,
                self.sidebar.accordion.color_picker_ch2.component.value,
                self.sidebar.accordion.color_picker_result.component.value],
                self.sidebar.accordion.window_selector.component.value,
                self.sidebar.accordion.overlap_selector.component.value
            )

            self.main_view.update_analysis_plot(
                self.preprocessing,
                self.signal_process,
                [],
                self.sidebar.accordion.stretching_switch.component.value,
                [self.sidebar.accordion.color_picker_ch1.component.value,
                self.sidebar.accordion.color_picker_ch2.component.value,
                self.sidebar.accordion.color_picker_result.component.value],
                self.sidebar.accordion.method_selector.component.value,
                self.sidebar.accordion.window_selector.component.value,
                self.sidebar.accordion.overlap_selector.component.value
            )

    def data_selection(self, method):
        data = self.signal_process.current_data

        if method == "Cross Spectral Density":
            data = np.abs(self.signal_process.current_data[:, 0, 1])

        if method == "Auto Spectral Density - Input":
            data = np.abs(self.signal_process.current_data[:, 0, 0])

        if method == "Auto Spectral Density - Output":
            data = np.abs(self.signal_process.current_data[:, 1, 1])

        if method == "Impulse Response":
            data = self.signal_process.impulse_response_data

        if method == "Amplitude Response":
            data = self.signal_process.amplitude_response_data

        if method == "Phase Response":
            data = self.signal_process.phase_response_data

        return data

    def handle_export_event(self, event):
        if (event.obj == self.sidebar.accordion.file_exporter.component):
            data = self.data_selection(self.sidebar.accordion.method_selector.component.value)

            self.sidebar.accordion.file_exporter.select_directory(event, data,
                        self.sidebar.accordion.channel_selector_input.component.value,
                        self.sidebar.accordion.channel_selector_output.component.value,
                        self.sidebar.accordion.method_selector.component.value,
                        self.sidebar.accordion.exporter_selector.component.value,
                        self.sidebar.accordion.window_selector.component.value,
                        self.sidebar.accordion.overlap_selector.component.value,
                                                                  )

    def servable(self):
        """
        Makes the application servable.
        """
        # Serve app layout
        self.template_layout.servable()
