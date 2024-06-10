import holoviews as hv
import numpy as np


class Plotter:
    def __init__(self, data_callback, stretch_value, color_value="default_color"):
        self.data_callback = data_callback
        self.stretch_value = stretch_value
        self.color_value = color_value

    def create_plot(self, channel):
        # Generate the figure for the given channel
        channel_size = self.data_callback.get_channel_size(channel)
        time_axis = np.linspace(0, 1, channel_size)
        signal_data = self.data_callback.converted_file[:, channel]
        fig = hv.Curve((time_axis, signal_data),
                       kdims="Zeit in Sekunden", vdims="Amplitude", label=f'Channel {channel}') \
              .opts(color=self.color_value, shared_axes=False, width=800, height=400)
        return fig
