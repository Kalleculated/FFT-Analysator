import holoviews as hv
import numpy as np
import panel as pn
from panel.pane import HoloViews

from fft_analysator.gui.components.tabs import Tabs


class MainView:
    def __init__(self):
        self.str_signal_tab = "Signalinput"
        self.tabs = Tabs()
        self.layout = pn.Column(self.tabs.component, sizing_mode='stretch_width')

    def update_signal(self, data_callback, channels, stretch_value):
        # Update the main view with the new data
        self.signals = pn.Column(sizing_mode='stretch_width')

        if channels:
            for channel in channels:

                fig = hv.Curve((np.linspace(0, 1, 51200), data_callback.converted_file[:, channel]),
                            kdims="Zeit in Sekunden", vdims="Amplitude").opts()

                if stretch_value:
                    plot_pane = HoloViews(fig, sizing_mode='stretch_width')
                else:
                    plot_pane = HoloViews(fig)

                self.signals.append(plot_pane)

                self.tabs.component[0] = (self.str_signal_tab, self.signals)

        else:
            self.tabs.component[0] = (self.str_signal_tab, 'Keine Datei ausgewählt!')

    def servable(self):
        self.layout.servable(target="main")
