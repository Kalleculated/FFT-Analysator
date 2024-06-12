import holoviews as hv
import numpy as np
import panel as pn
from panel.pane import HoloViews


class Plotter:
    def __init__(self, tabs_callback, data_callback):
        self.data_callback = data_callback
        self.tabs = tabs_callback

    def create_plot_ac(self, channel, color_value):
        # Generate the figure for the given channel
        signal_data = self.data_callback.set_channel_on_data_block(channel)

        channel_size = signal_data.shape[0]
        time_axis = np.linspace(0, 1, channel_size)

        fig = hv.Curve((time_axis, signal_data),
                       kdims="Zeit in Sekunden", vdims="Amplitude", label=f'Channel {channel}') \
              .opts(color=color_value, shared_axes=False, width=800, height=400)
        return fig


    def create_signalinput_plot(self, channels=None, stretch_value=None, color_picker_value=None):
        signals = pn.Column(sizing_mode='stretch_width')

        if not channels:
            self.tabs.component[0] = (self.tabs.str_signal_tab, 'Keine Datei ausgewählt!')
            return

        for i, channel in enumerate(channels):
            color_value = color_picker_value[i] if i < len(color_picker_value) else "default_color"
            fig = self.create_plot_ac(channel, color_value)

            # Create a HoloViews pane for the figure
            plot_pane = HoloViews(fig, sizing_mode='stretch_width' if stretch_value else None)

            # Append the plot pane to the signals column
            signals.append(plot_pane)

        # Update the corresponding tab with new signals
        self.tabs.component[0] = (self.tabs.str_signal_tab, signals)
