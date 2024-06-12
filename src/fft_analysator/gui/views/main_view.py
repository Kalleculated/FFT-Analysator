import holoviews as hv
import numpy as np
import panel as pn
from panel.pane import HoloViews
from fft_analysator.gui.components.tabs import Tabs
from fft_analysator.analysis.plotting import Plotter


class MainView:
    def __init__(self):
        self.tabs = Tabs()
        self.layout = pn.Column(self.tabs.component, sizing_mode='stretch_width')

    def update_signal(self, data_callback, channels, stretch_value, color_picker_value):

        plot = Plotter(self.tabs, data_callback)
        plot.create_signalinput_plot(channels, stretch_value, color_picker_value)


    def servable(self):
        self.layout.servable(target="main")
