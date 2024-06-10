import holoviews as hv
import numpy as np
import panel as pn
from panel.pane import HoloViews
from fft_analysator.gui.components.tabs import Tabs
from fft_analysator.analysis.plotting import Plotter


class MainView:
    def __init__(self):
        self.str_signal_tab = "Signalinput"
        self.str_Spektrum_tab = "Spektrum"
        self.str_Impulsantwort_tab = "Impulsantwort"
        self.str_Analysefuktionen_tab = "Analysefunktionen"
        self.tabs = Tabs()
        self.layout = pn.Column(self.tabs.component, sizing_mode='stretch_width')

    def update_signal(self, data_callback, channels, stretch_value, color_picker_value):
        # Create a new panel column for signals
        signals = pn.Column(sizing_mode='stretch_width')

        if not channels:
            self.tabs.component[0] = (self.str_signal_tab, 'Keine Datei ausgewählt!')
            return

        # Iterate through each channel and create a plot
        for i, channel in enumerate(channels):
            color = color_picker_value[i] if i < len(color_picker_value) else "default_color"
            plotter = Plotter(data_callback, stretch_value, color)
            fig = plotter.create_plot(channel)

            # Create a HoloViews pane for the figure
            plot_pane = HoloViews(fig, sizing_mode='stretch_width' if stretch_value else None)

            # Append the plot pane to the signals column
            signals.append(plot_pane)

        # Update the corresponding tab with new signals
        self.tabs.component[0] = (self.str_signal_tab, signals)


    def servable(self):
        self.layout.servable(target="main")
