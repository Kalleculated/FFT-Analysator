import holoviews as hv
import numpy as np
import panel as pn
from panel.pane import HoloViews
from fft_analysator.gui.components.tabs import Tabs
from fft_analysator.analysis.plotting import Plotter



class MainView:
    """
    A class used to represent the main view of the application.

    This class is responsible for updating the signal and analysis plots based on the provided data.

    Attributes:
        tabs (object):
            An instance of the Tabs class.
        layout (object):
            A panel Column layout containing the tabs component.

    Methods:
        update_signal(data_callback, channels, stretch_value, color_picker_value, window, overlap):
            Updates the signal plots based on the provided data.
        update_analysis_plot(data_callback, channels, stretch_value, color_picker_value, analysis_callback, window, overlap):
            Updates the analysis plots based on the provided data.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the MainView object.

        The tabs attribute is initialized as a Tabs instance.
        The layout attribute is initialized as a panel Column layout containing the tabs component.
        """
        self.tabs = Tabs()
        self.layout = pn.Column(self.tabs.component, sizing_mode='stretch_width')


    def update_signal(self, data_callback, signal_process_callback, channels, stretch_value, color_picker_value, window, overlap, show_grid,x_log,y_log, db):
        """
        Updates the signal plots based on the provided data.

        Args:
            data_callback (function): A callback function that returns the data to be plotted.
            channels (list): A list of channels to be plotted.
            stretch_value (int): The stretch value for the plot.
            color_picker_value (str): The color for the plot.
            window (str): The window type for the plot.
            overlap (float): The overlap value for the plot.

        Returns:
            None
        """
        if channels:
            signal_process_callback.set_parameters(channels, window, overlap)

            print(show_grid)
            plot = Plotter(signal_process_callback, channels, self.tabs, data_callback, window, overlap,
                            color_picker_value, stretch_value, show_grid,x_log,y_log, db)

            # generate time plot
            plot.create_time_plot()

            # generate frequency response plot
            plot.create_frequency_response_plot()

            # generate frequency response plot
            plot.create_impulse_response_plot()
        else:
            self.tabs.component[0] = (self.tabs.str_signal_tab, 'No data chosen!')
            self.tabs.component[1] = (self.tabs.str_frequency_response_tab, 'No data chosen!')
            self.tabs.component[2] = (self.tabs.str_impulse_response_tab, 'No data chosen!')


    def update_analysis_plot(self, data_callback, signal_process_callback, channels, stretch_value, color_picker_value, analysis_callback,
                             window, overlap, show_grid,x_log,y_log, db):
        """
        Updates the analysis plots based on the provided data.

        Args:
            data_callback (function): A callback function that returns the data to be plotted.
            channels (list): A list of channels to be plotted.
            stretch_value (int): The stretch value for the plot.
            color_picker_value (str): The color for the plot.
            analysis_callback (function): A callback function that returns the analysis data to be plotted.
            window (str): The window type for the plot.
            overlap (float): The overlap value for the plot.

        Returns:
            None
        """
        if channels:
            signal_process_callback.set_parameters(channels, window, overlap)

            plot = Plotter(signal_process_callback, channels, self.tabs, data_callback, window, overlap,
                            color_picker_value, stretch_value, show_grid,x_log,y_log, db)

            # plot analysis function
            if analysis_callback == "Auto Spectral Density - Input":
                # generate Auto Spectral Density plot
                plot.create_auto_and_cross_power_spectrum_plot(type='xx')

            elif analysis_callback == "Auto Spectral Density - Output":
                # generate Auto Spectral Density plot
                plot.create_auto_and_cross_power_spectrum_plot(type='yy')

            elif analysis_callback == "Cross Spectral Density":
                # generate Cross Spectral Density plot
                plot.create_auto_and_cross_power_spectrum_plot(type='xy')

            elif analysis_callback == "Auto Correlation - Input":
                # generate Auto Correlation - Input plot
                plot.create_correlation_plot(type='xx')

            elif analysis_callback == "Auto Correlation - Output":
                # generate Auto Correlation - Output plot
                plot.create_correlation_plot(type='yy')

            elif analysis_callback == "Cross Correlation":
                # generate Cross Spectral Density plot
                plot.create_correlation_plot(type='xy')

            elif analysis_callback == "Coherence":
                # generate coherence plot
                plot.create_coherence_plot()

            elif analysis_callback == "No Analysis Function":
                self.tabs.component[3] = (self.tabs.str_analysis_function_tab, "No Analysis Function is choosen")

            elif analysis_callback == "Impulse Response" or analysis_callback == "Amplitude Response" or analysis_callback == "Phase Response":

                self.tabs.component[3] = (self.tabs.str_analysis_function_tab, "No Analysis Function for this Tab is choosen")

        else:
            self.tabs.component[3] = (self.tabs.str_analysis_function_tab, 'No data chosen!')


    def servable(self):
        """
        Makes the main view servable.
        """
        self.layout.servable(target="main")
