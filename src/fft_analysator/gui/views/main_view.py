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
        if channels:
            plot = Plotter(channels,self.tabs, data_callback)

            # generate time plot
            plot.create_time_plot(channels, stretch_value, color_picker_value)

            # generate frequency response plot
            plot.create_frequency_response_plot(channels, stretch_value, color_picker_value)

            # generate frequency response plot
            plot.create_impulse_response_plot(channels, stretch_value, color_picker_value)
        else:
            self.tabs.component[0] = (self.tabs.str_signal_tab, 'No data chosen!')
            self.tabs.component[1] = (self.tabs.str_frequency_response_tab, 'No data chosen!')
            self.tabs.component[2] = (self.tabs.str_impulse_response_tab, 'No data chosen!')


    def update_analysis_plot(self, data_callback, channels, stretch_value, color_picker_value, analysis_callback,
                             window, overlap):
        if channels:
            plot = Plotter(channels,self.tabs, data_callback)

            # plot analysis function
            if analysis_callback == "Auto Spectral Density - Input":
                # generate Auto Spectral Density plot
                plot.create_auto_and_cross_power_spectrum_plot(window,overlap, channels, stretch_value, color_picker_value,type='xx')

            elif analysis_callback == "Auto Spectral Density - Output":
                # generate Auto Spectral Density plot
                plot.create_auto_and_cross_power_spectrum_plot(window,overlap, channels, stretch_value, color_picker_value,type='yy')

            elif analysis_callback == "Cross Spectral Density":
                # generate Cross Spectral Density plot
                plot.create_auto_and_cross_power_spectrum_plot(window, overlap, channels, stretch_value, color_picker_value, type='xy')

            elif analysis_callback == "Auto Correlation - Input":
                # generate Auto Correlation - Input plot
                plot.create_correlation_plot(channels, stretch_value, color_picker_value, type='xx')

            elif analysis_callback == "Auto Correlation - Output":
                # generate Auto Correlation - Output plot
                plot.create_correlation_plot(channels, stretch_value, color_picker_value, type='yy')

            elif analysis_callback == "Cross Correlation":
                # generate Cross Spectral Density plot
                plot.create_correlation_plot(channels, stretch_value, color_picker_value, type='xy')

            elif analysis_callback == "Coherence":
                # generate coherence plot
                plot.create_coherence_plot(channels, stretch_value, color_picker_value)

            elif analysis_callback == "No Analysis Function":
                self.tabs.component[3] = (self.tabs.str_analysis_function_tab, "No Analysis Function choosen")
        else:
            self.tabs.component[3] = (self.tabs.str_analysis_function_tab, 'No data chosen!')


    def servable(self):
        self.layout.servable(target="main")




#TODO add on main_view button with enable/disable grid and also selector between linear and logaritmic axis
#TODO Case if both channels are same, then disable the cross correlation and coherence plot ...
#TODO Impulse response shift, impulse peak is also at the end of the signal visble, so the shift is not correct

#TODO Zwei gleiche Signal müssen auch separat als Input und Output (dargestellt),
# als zwei Kanäle behandelt werden können
