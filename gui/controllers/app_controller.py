import panel as pn
from gui.views.sidebar import Sidebar
from gui.views.main_view import MainView
import analysis.preprocessing as pp
import holoviews as hv

hv.extension("bokeh", "plotly")

class AppController:
    def __init__(self):

        # Initialization of panel extensions and template
        pn.extension(sizing_mode="stretch_width", template="fast", theme="dark")
        pn.extension("plotly")
        pn.state.template.param.update(
            site="FFT-Analysator",
            title="",
            header_background="#E91E63",
            accent_base_color="#E91E63",
        )

        # Initialization of main and side views
        self.main_view = MainView()
        self.sidebar = Sidebar(self.handle_fileupload_event, self.handle_sidebar_event)

        # Initialization of data preprocessing and binary file
        self.binary_file = None
        self.preprocessing = None

    def handle_fileupload_event(self, event):
        # Handle the file upload event and update the preprocessing object
        self.binary_file = self.sidebar.accordion.file_input.component.value
        self.preprocessing = pp.Preprocess(self.binary_file)

        if event.obj == self.sidebar.accordion.file_input.component:
            self.sidebar.update_multi_choice(self.preprocessing)


    def handle_sidebar_event(self, event):
        # Update the main view when the sidebar event is triggered
        # Note, we could also split this into multiple functions
        
        if event.obj == self.sidebar.accordion.multi_choice._component or event.obj == self.sidebar.accordion.stretching_switch._component:
            self.main_view.update_signal(self.preprocessing, self.sidebar.accordion.multi_choice._component.value, self.sidebar.accordion.stretching_switch._component.value)

    def servable(self):
        # Serve app layout
        self.main_view.servable()
        self.sidebar.servable()
