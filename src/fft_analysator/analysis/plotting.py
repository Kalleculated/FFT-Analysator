import holoviews as hv
import numpy as np
import panel as pn
from panel.pane import HoloViews
import acoular as ac
from fft_analysator.analysis.signal_processing import Signal_Process

class Plotter:

    def __init__(self, signal_process_callback, channels, tabs_callback, data_callback,
                window, overlap, color_picker_value,stretch_value=None):
        self.data_callback = data_callback
        self.tabs = tabs_callback
        self.fs = self.data_callback.get_abtastrate()
        self.block = data_callback.current_block_idx
        self.signal_process = signal_process_callback
        self.channels = channels
        self.color_picker_value = color_picker_value
        self.stretch_value = stretch_value

        if channels:
            if len(channels) == 1:
                self.input_channel = self.channels[0]
                self.output_channel = self.channels[0]
            else:
                self.input_channel = self.channels[0]
                self.output_channel = self.channels[1]

    def create_time_plot(self):

        # set the signals column
        signals = pn.Column(sizing_mode='stretch_width')

        for i, channel in enumerate(list(dict.fromkeys(self.channels))):

            color_value = self.color_picker_value[i] if i < len(self.color_picker_value) else "default_color"

            # Get the time_data block wise for the given channel
            time_data = self.data_callback.set_channel_on_data_block(channel)

            # Create the dynamic time axis for the given blocks
            t = self.signal_process.create_time_axis(len(time_data)) * (self.block + 1)

            # set title
            if self.input_channel == self.output_channel:
                title = f"Input/Output signal - Channel {channel}"
            elif channel == self.input_channel:
                role = "Input"
                title =  f"{role} signal - Channel {channel}"
            elif channel == self.output_channel:
                role = "Output"
                title =  f"{role} signal - Channel {channel}"

            # Create the figure
            fig = hv.Curve((t, time_data),
                       kdims="Time in s", vdims="Amplitude", label=  title) \
                  .opts(color=color_value, shared_axes=False, width=800, height=350,show_grid=True)

            # Create a HoloViews pane for the figure
            plot_pane = HoloViews(fig, sizing_mode='stretch_width' if self.stretch_value else None)

            # Append the plot pane to the signals column
            signals.append(plot_pane)

        # Update the corresponding tab with new signals
        self.tabs.component[0] = (self.tabs.str_signal_tab, signals)


    def create_frequency_response_plot(self):

        # set the signals column
        signals = pn.Column(sizing_mode='stretch_width')

        # set a own color picker for results
        color_value = self.color_picker_value[2]

        H =  self.signal_process.frequency_response(frq_rsp_dB=True)
        phi = self.signal_process.phase_response(deg=True)
        f = self.signal_process.create_frequency_axis()

        # Create frequency response fig
        fig1 = hv.Curve((f,H),
                    kdims="Frequency in Hz", vdims="Magnitude in dB", label=f'Amplitude Response') \
                .opts(color=color_value, shared_axes=False, width=750, height=350,show_grid=True)

        # Create phase response fig
        fig2 = hv.Curve((f,phi),
                    kdims="Frequency in Hz", vdims="Phase in degree ° ", label=f'Phase Response') \
                .opts(color=color_value, shared_axes=False, width=750, height=350,show_grid=True)

        for fig in [fig1, fig2]:

            # Create a HoloViews pane for the figure
            plot_pane = HoloViews(fig,  sizing_mode='stretch_width' if self.stretch_value else None)

            # Append the plot pane to the signals column
            signals.append(plot_pane)

        # Update the corresponding tab with new signals
        self.tabs.component[1] = (self.tabs.str_frequency_response_tab, signals)


    def create_impulse_response_plot(self):
        # set a own color picker for results
        color_value = self.color_picker_value[2]

        h = self.signal_process.impuls_response()

        # Create the dynamic time axis for the given blocks
        t = self.signal_process.create_time_axis(len(h)) * 100

        # Create frequency response fig
        fig = hv.Curve((t,h),
                    kdims="Time in s", vdims="Amplitude", label = f'Impulse Response') \
                .opts(color=color_value, shared_axes=False, width=750, height=350,show_grid=True)

        # Create a HoloViews pane for the figure
        plot_pane = HoloViews(fig,  sizing_mode='stretch_width' if self.stretch_value else None)

        # Update the corresponding tab with new signals
        self.tabs.component[2] = (self.tabs.str_impulse_response_tab, plot_pane)


    def create_coherence_plot(self):
        # set a own color picker for results
        color_value = self.color_picker_value[2]

        coherence =  self.signal_process.coherence()
        f = self.signal_process.create_frequency_axis()

        # Create frequency response fig r'$\gamma_{XY}^2$'
        fig = hv.Curve((f,coherence),
                    kdims="Frequency in Hz", vdims="Coherence", label="Coherence ") \
                .opts(color=color_value, shared_axes=False, width=750, height=350, show_grid=True,
                   ylim=(-0.1,1.1))

        # Create a HoloViews pane for the figure
        plot_pane = HoloViews(fig,  sizing_mode='stretch_width' if self.stretch_value else None)

        # Update the corresponding tab with new signals
        self.tabs.component[3] = (self.tabs.str_analysis_function_tab, plot_pane)


    def create_auto_and_cross_power_spectrum_plot(self,type=None):
        # set a own color picker for results
        color_value = self.color_picker_value[2]

        csm =  self.signal_process.csm()
        f = self.signal_process.create_frequency_axis()

        if type == 'xx':
            title = "Auto Power Spectrum - Input"
            csm_value = csm[:,0,0]
        elif type == 'yy':
            if self.input_channel == self.output_channel:
                csm_value = csm[:,0,0]
            else:
                csm_value = csm[:,1,1]
            title = "Auto Power Spectrum - Output"
        elif type == 'xy':
            title = "Cross Power Spectrum"
            csm_value = csm[:,0,1]

        fig = hv.Curve((f,np.abs(csm_value)),
                    kdims="Frequency in Hz", vdims=" Power density in Pa^2/Hz", label=title ) \
                .opts(color=color_value, shared_axes=False, width=750, height=350, show_grid=True)

        # Create a HoloViews pane for the figure
        plot_pane = HoloViews(fig,  sizing_mode='stretch_width' if self.stretch_value else None)

        # Update the corresponding tab with new signals
        self.tabs.component[3] = (self.tabs.str_analysis_function_tab, plot_pane)


    def create_correlation_plot(self,type=None):
        # set a own color picker for results
        color_value = self.color_picker_value[2]

        if type == 'xx':
            title = "Auto Correlation - Input"
            corr = self.signal_process.correlation(type='xx')
        elif type == 'yy':
            title = "Auto Correlation - Output"
            corr = self.signal_process.correlation(type='yy')
        elif type == 'xy':
            title = "Cross Correlation"
            corr = self.signal_process.correlation(type='xy')

        # create time delay axis
        tau = self.signal_process.create_correlation_axis(len(corr))


        fig = hv.Curve((tau,corr),
                    kdims="Time delay in s", vdims="Correlation", label=title ) \
                .opts(color=color_value, shared_axes=False, width=750, height=350, show_grid=True)
                      #xlim=(np.min(tau)+0.1*np.min(tau), max(tau)+0.1*np.max(tau)))

        # Create a HoloViews pane for the figure
        plot_pane = HoloViews(fig,  sizing_mode='stretch_width' if self.stretch_value else None)

        # Update the corresponding tab with new signals
        self.tabs.component[3] = (self.tabs.str_analysis_function_tab, plot_pane)
