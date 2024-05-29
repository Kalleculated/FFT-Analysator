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
        self.sidebar = Sidebar(self.handle_fileupload_event, self.handle_sidebar_event)

        # Initialization of panel extensions and template
        self.template_layout = pn.template.FastListTemplate(title="FFT-Analysator",
                                                            header_background="#E91E63",
                                                            accent_base_color="#E91E63",
                                                            theme="dark",
                                                            sidebar=self.sidebar.layout,
                                                            main=self.main_view.layout
                                                            )

        # Initialization of data preprocessing and binary file
        self.binary_file = None
        self.preprocessing = None

    def handle_fileupload_event(self, event):
        # Handle the file upload event and update the preprocessing object
        self.binary_file = self.sidebar.accordion.file_input.component.value

        if self.binary_file:
            self.preprocessing = pp.Preprocess(self.binary_file)

            if event.obj == self.sidebar.accordion.file_input.component:
                self.sidebar.update_multi_choice(self.preprocessing)

        else:
            self.sidebar.update_multi_choice()

    def handle_sidebar_event(self, event):
        # Update the main view when the sidebar event is triggered
        # Note, we could also split this into multiple functions

        if (
            event.obj == self.sidebar.accordion.multi_choice.component
            or event.obj == self.sidebar.accordion.stretching_switch.component
        ):
            self.main_view.update_signal(
                self.preprocessing,
                self.sidebar.accordion.multi_choice.component.value,
                self.sidebar.accordion.stretching_switch.component.value,
            )

    def servable(self):
        # Serve app layout
        self.template_layout.servable()
