import panel as pn
from gui.components.tabs import Tabs
import holoviews as hv
import numpy as np
from panel.pane import HoloViews

class MainView:
    def __init__(self):
        self.str_signal_tab = "Signalinput"
        self.tabs = Tabs()
        self.main = pn.Column(self.tabs._component, sizing_mode='stretch_width')

    def update_signal(self, data_callback, channels, stretch_value):
        # Update the main view with the new data
        self.signals = pn.Column(sizing_mode='stretch_width')
        
        if channels:
            for channel in channels:

                fig = hv.Curve((np.linspace(0,1,51200), data_callback.converted_file[:,channel]), 
                            kdims="Zeit in Sekunden", vdims="Amplitude").opts()
                
                if stretch_value:
                    plot_pane = HoloViews(fig, sizing_mode='stretch_width')
                else:
                    plot_pane = HoloViews(fig)
                    
                self.signals.append(plot_pane)
                
                self.tabs._component[0] = (self.str_signal_tab, self.signals)

        else:
            self.tabs._component[0] = (self.str_signal_tab, 'Keine Datei ausgewählt!')

    def servable(self):
        self.main.servable(target="main")