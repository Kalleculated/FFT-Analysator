import panel as pn
from  analysis.signal_processing import convert_data
import holoviews as hv
import numpy as np
from panel.pane import HoloViews

class MainView:
    def __init__(self):
        self.str_signal_tab = "Signalinput"

        self.tabs = pn.Tabs((self.str_signal_tab, 'Keine Datei ausgewählt!'), sizing_mode='stretch_width', dynamic=True)

        self.main = pn.Column(self.tabs, sizing_mode='stretch_width')

    def update_signal(self, data, channels):
        # Update the main view with the new data
        fig = hv.Curve((np.linspace(0,1,51200), data[:,channels]), 
                       kdims="Zeit in Sekunden", vdims="Amplitude").opts()
        plot_pane = HoloViews(fig, sizing_mode='stretch_width')
        self.tabs[0] = (self.str_signal_tab, pn.Column(plot_pane, sizing_mode='stretch_width'))

    def servable(self):
        self.main.servable(target="main")