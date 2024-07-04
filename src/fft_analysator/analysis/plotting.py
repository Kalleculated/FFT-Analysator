import holoviews as hv
import numpy as np
import panel as pn
from panel.pane import HoloViews

class Plotter:
    def __init__(self, tabs_callback, data_callback):
        self.data_callback = data_callback
        self.tabs = tabs_callback
        self.fs = self.data_callback.get_abtastrate()
        self.block = data_callback.current_block_idx

    def create_plot_ac(self, channel, color_value):
        # Generate the figure for the given channel
        signal_data = self.data_callback.set_channel_on_data_block(channel)

        channel_size = signal_data.shape[0]
        time_axis = np.arange(channel_size) * (self.block + 1) / self.fs

        fig = hv.Curve((time_axis, signal_data),
                       kdims="Zeit in Sekunden", vdims="Amplitude", label=f'Input_Signal - Channel {channel}') \
              .opts(color=color_value, shared_axes=False, width=800, height=350,show_grid=True)
        return fig

    def creat_plot_ac_spectrum(self, channel, color_value):
        # Generate the figure for the given channel
        signal_data = self.data_callback.set_channel_on_data_block(channel)
        channel_size = signal_data.shape[0]

        #Calculate Frequency Axis
        frequency_axis = np.fft.rfftfreq(channel_size,1/self.fs)

        # Calculate Absolut Spectrum
        abs_spec_data = np.abs(np.fft.rfft(signal_data))
        abs_spec_data_dB = 20*np.log10(abs_spec_data) # if desired normalize to 0 dB with /np.max(abs_spec_data)

        # Calculate phase spectrum in degrees
        angle_deg = np.arctan2(np.imag(np.fft.rfft(signal_data)), np.real(np.fft.rfft(signal_data)))*180/np.pi
        # angle_deg = np.angle(angle_deg)
        # angle_deg = np.unwrap(angle_deg) # if desired unwrap the phase

        fig1 = hv.Curve((frequency_axis,abs_spec_data_dB),
                       kdims="Frequenz in Hz", vdims="Magnitude in dB", label=f' Amplitudengang - Channel {channel}') \
              .opts(color=color_value, shared_axes=False, width=750, height=350,show_grid=True)

        # Create the second plota
        fig2 = hv.Curve((frequency_axis,angle_deg),
                       kdims="Frequenz in Hz", vdims="Phase in Grad °", label=f'Phasengang - Channel {channel}') \
              .opts(color=color_value, shared_axes=False, width=750, height=350,show_grid=True)
        # --> GRID ON/OFF SHOULD BE APPENDED AS A BUTTON

        fig = fig1 + fig2
        return fig


    def create_signalinput_plot(self, channels=None, stretch_value=None, color_picker_value=None):
        signals = pn.Column(sizing_mode='stretch_width')

        if not channels:
            self.tabs.component[0] = (self.tabs.str_signal_tab, 'Keine Datei ausgewählt!')
            return

        for i, channel in enumerate(list(dict.fromkeys(channels))):
            color_value = color_picker_value[i] if i < len(color_picker_value) else "default_color"
            fig = self.create_plot_ac(channel, color_value)

            # Create a HoloViews pane for the figure
            plot_pane = HoloViews(fig, sizing_mode='stretch_width' if stretch_value else None)

            # Append the plot pane to the signals column
            signals.append(plot_pane)

        # Update the corresponding tab with new signals
        self.tabs.component[0] = (self.tabs.str_signal_tab, signals)

    def create_Spektrum_plot(self, channels=None, stretch_value=None, color_picker_value=None):
        signals = pn.Column(sizing_mode='fixed')

        if not channels:
            self.tabs.component[1] = (self.tabs.str_Spektrum_tab, 'Keine Datei ausgewählt!')
            return

        for i, channel in enumerate(list(dict.fromkeys(channels))):
            color_value = color_picker_value[i] if i < len(color_picker_value) else "default_color"
            fig = self.creat_plot_ac_spectrum(channel, color_value)

            # Create a HoloViews pane for the figure
            #plot_pane = HoloViews(fig, sizing_mode='stretch_width' if stretch_value else None)
            plot_pane = HoloViews(fig, sizing_mode='fixed')

            # Append the plot pane to the signals column
            signals.append(plot_pane)

        # Update the corresponding tab with new signals
        self.tabs.component[1] = (self.tabs.str_Spektrum_tab, signals)
