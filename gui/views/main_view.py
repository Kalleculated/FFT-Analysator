import panel as pn
from  analysis.signal_processing import count_channels
import holoviews as hv
import numpy as np
from panel.pane import HoloViews

class MainView:
    def __init__(self):
        self.tabs = pn.Tabs(sizing_mode='stretch_width', dynamic=True)

        self.main = pn.Column(self.tabs, sizing_mode='stretch_width')

    def update_signal(self, file_data):
        # Update the main view with the new data
        data = count_channels(file_data)
        fig = hv.Curve((np.linspace(0,1,51200), data[:,1]), 
                       kdims="Zeit in Sekunden", vdims="Amplitude").opts()
        plot_pane = HoloViews(fig, sizing_mode='stretch_width')
        self.tabs.append(('Signalinput', pn.Column(plot_pane, sizing_mode='stretch_width')))

    def servable(self):
        self.main.servable(target="main")