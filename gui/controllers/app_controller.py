import panel as pn
from gui.views.sidebar import Sidebar
from gui.views.main_view import MainView
from analysis.signal_processing import count_channels
import holoviews as hv
import numpy as np

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
        self.sidebar = Sidebar()

    def handle_sidebar_event(self, event):
        # Update the main view when the sidebar event is triggered
        self.main_view.update_main(event)

    def servable(self):
        # Serve app layout
        self.main_view.servable()
        self.sidebar.servable()
