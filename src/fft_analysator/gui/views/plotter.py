import holoviews as hv
import numpy as np
from panel.pane import HoloViews
from fft_analysator.gui.components.tabs import Tabs

class Plotter():
    def __init__(self, data_callback, stretch_value, color_value="default_color"):
        self.data_callback = data_callback
        self.color_value = color_value
        self.stretch_value = stretch_value

    def set_color_value(self, color_value):
        self.color_value = color_value

    def set_data_callback(self, data):
        self.data_callback = data

    def set_stretch_value(self, stretch):
        self.stretch_value = stretch

    def update_signal(self, channel):
        fig = hv.Curve((np.linspace(0, 1, self.data_callback.get_channel_size()), self.data_callback.converted_file[:, channel]),
                            kdims="Zeit in Sekunden", vdims="Amplitude",label= f'Channel {channel}').opts(color=self.color_value,shared_axes=False, width=800, height=400)
        return fig
