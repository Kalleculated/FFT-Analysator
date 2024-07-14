import numpy as np
import panel as pn
from panel.pane import HoloViews
import holoviews as hv
from holoviews import opts
import math
import acoular as ac
from fft_analysator.analysis.signal_processing import Signal_Process


class Plotter:
    """
    A class used to process and plot signals.

    Attributes
    ----------
    signal_process : Signal_Process
        An instance of the Signal_Process class.
    channels : list
        A list of channels.
    color_picker_value : list
        A list of color values for each channel.
    stretch_value : bool
        A flag indicating whether to stretch the plot width.
    input_channel : int
        The input channel number.
    output_channel : int
        The output channel number.
    """

    def __init__(self, signal_process_callback, channels, tabs_callback, data_callback,
                window, overlap, color_picker_value,stretch_value=None,show_grid=None,x_log=None,y_log=None,db=None):
        self.data_callback = data_callback
        self.tabs = tabs_callback
        self.fs = self.data_callback.get_abtastrate()
        self.block = data_callback.current_block_idx
        self.block_size = data_callback.block_size
        self.numsamples = data_callback.source.numsamples
        self.signal_process = signal_process_callback
        self.channels = channels
        self.color_picker_value = color_picker_value
        self.stretch_value = stretch_value
        self.show_grid = show_grid
        self.x_log = x_log
        self.y_log = y_log
        self.db = db
       
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
            
            # set color picker value
            color_value = self.color_picker_value[i] if i < len(self.color_picker_value) else "default_color"

            # values in dB
            if not self.db:
                # Get the time_data block wise for the given channel
                time_data = self.data_callback.set_channel_on_data_block(channel)
                scale_min_factor = 0.2 # set min scale factor
                y_label = "Sound Pressure in Pa"
            else:
                time_data = self.signal_process.SPL(channel)
                scale_min_factor = -0.2 # set min scale factor
                y_label = "SPL in dB" # "Sound Pressure Level

            # set max scale factor
            scale_max_factor = 0.2
            
            # Create the dynamic time axis for the given blocks
            t = self.signal_process.create_time_axis(N=len(time_data))   
            amount_steps = self.numsamples/self.block_size        
            fractional_part, integer_part = math.modf(amount_steps)
            
            # set time axis for current block
            if self.block != 0:
                
                if fractional_part == 0:
                    t = t + self.block * (self.block_size/self.fs)
                else:
                    if integer_part > (self.block):
                        t = t + self.block * (self.block_size/self.fs) 
                    else:                     
                        amount_samp = self.numsamples - (self.block) * self.block_size     
                        t = t + (self.block-1) * (self.block_size/self.fs) + (amount_samp/self.fs) / fractional_part

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
            fig = hv.Curve((t, time_data), kdims="Time in s", vdims=y_label, label=  title)
            fig.opts(color=color_value, shared_axes=False, width=750, height=350,show_grid=self.show_grid,
                     logx = False, logy = self.y_log, ylim=(np.min(time_data) + scale_min_factor * 
                    np.min(time_data), np.max(time_data) + scale_max_factor * np.max(time_data)))

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

        # values in dB
        if not self.db:
            H =  self.signal_process.frequency_response(frq_rsp_dB=False)
            y_label = "Sound Pressure in Pa"
        else:
            H =  self.signal_process.frequency_response(frq_rsp_dB=True)
            y_label = "SPL in dB" # "Sound Pressure Level
        
        # Create the phase response
        phi = self.signal_process.phase_response(deg=True)
        
        # Create frequency axis for the given blocks
        f = self.signal_process.create_frequency_axis()
        
        # Create frequency response fig
        fig1 = hv.Curve((f,H), kdims="Frequency in Hz", vdims=y_label, label=f'Amplitude Response')
        fig1.opts(color=color_value, shared_axes=False, width=750, height=350,show_grid=self.show_grid,
                  logx=self.x_log, logy=self.y_log, xlim=(f[1], None) if self.x_log else (0, None))
        
        fig2 = hv.Curve((f,phi), kdims="Frequency in Hz", vdims="Phase in Degree °", label=f'Phase Response')
        fig2.opts(color=color_value, shared_axes=False, width=750, height=350,show_grid=self.show_grid,
                  logx=self.x_log, logy=False, xlim=(f[1], None) if self.x_log else (0, None))
        
        for fig in [fig1, fig2]:

            # Create a HoloViews pane for the figure
            plot_pane = HoloViews(fig, backend='bokeh', sizing_mode='stretch_width' if self.stretch_value else None)

            # Append the plot pane to the signals column
            signals.append(plot_pane)

        # Update the corresponding tab with new signals
        self.tabs.component[1] = (self.tabs.str_frequency_response_tab, signals)
       

    def create_impulse_response_plot(self):
        # set a own color picker for results
        color_value = self.color_picker_value[2]

        # values in dB
        if not self.db:
            h = self.signal_process.impuls_response(imp_dB=False).real
            scale_min_factor = 0.2 # set min scale factor
            y_label = "Sound Pressure in Pa"
        else:
            h = self.signal_process.impuls_response(imp_dB=True).real  
            scale_min_factor = -0.2 # set min scale factor
            y_label = "SPL in dB" # "Sound Pressure Level

        # set max scale factor
        scale_max_factor = 0.2
        
        # Create and scaling time axis
        block_size_factor = self.data_callback.source.numsamples / self.block_size
        t = self.signal_process.create_time_axis(len(h)) * 4 * block_size_factor 
             
        # Create frequency response fig
        fig = hv.Curve((t,h), kdims="Time in s", vdims=y_label, label = f'Impulse Response')
        fig.opts(color=color_value, shared_axes=False, width=750, height=350,show_grid=self.show_grid,
                logx = False, logy = self.y_log, xlim=(-0.1, np.max(t) + 0.1),
                ylim=(np.min(h) + scale_min_factor * 
                np.min(h), np.max(h) + scale_max_factor * np.max(h))) #if not self.y_log else (0, None))

        # Create a HoloViews pane for the figure
        plot_pane = HoloViews(fig,  sizing_mode='stretch_width' if self.stretch_value else None)

        # Update the corresponding tab with new signals
        self.tabs.component[2] = (self.tabs.str_impulse_response_tab, plot_pane)


    def create_coherence_plot(self):
        
        # set a own color picker for results
        color_value = self.color_picker_value[2]

        coherence =  self.signal_process.coherence()
        f = self.signal_process.create_frequency_axis()
        
        fig = hv.Curve((f,coherence), kdims="Frequency in Hz", vdims=r'$$\gamma_{XY}^2(f)$$', label="Coherence")
        fig.opts(color=color_value, shared_axes=False, width=750, height=350, show_grid=self.show_grid,
                   logx=self.x_log, logy=False,ylim=(-0.1,1.1), xlim=(f[1], None) if self.x_log else (0, None))

        # Create a HoloViews pane for the figure
        plot_pane = HoloViews(fig,  sizing_mode='stretch_width' if self.stretch_value else None)

        # Update the corresponding tab with new signals
        self.tabs.component[3] = (self.tabs.str_analysis_function_tab, plot_pane)


    def create_auto_and_cross_power_spectrum_plot(self,type=None):
        # set a own color picker for results
        color_value = self.color_picker_value[2]

        csm =  self.signal_process.csm()
        csm_dB = self.signal_process.csm(csm_dB=True)
        
        f = self.signal_process.create_frequency_axis()

        if type == 'xx':
            title = "Auto Power Spectrum - Input"
            if self.db:
                csm_value = csm_dB[:,0,0]
                y_label = r'PSD in $$\mathrm{dB}/\mathrm{Hz}$$'
            else:
                csm_value = csm[:,0,0]
                y_label = r'PSD in $$\mathrm{Pa}^{2}/\mathrm{Hz}$$'
                          
        elif type == 'yy':
            title = "Auto Power Spectrum - Output"
            
            if self.db:
                y_label = r'PSD in $$\mathrm{dB}/\mathrm{Hz}$$'
            else:
                y_label = r'PSD in $$\mathrm{Pa}^{2}/\mathrm{Hz}$$'   
                
            if self.input_channel == self.output_channel:
                if self.db:
                    y_label = r'PSD in $$\mathrm{dB}/\mathrm{Hz}$$'
                    csm_value = csm_dB[:,0,0]
                else:
                    y_label = r'PSD in $$\mathrm{Pa}^{2}/\mathrm{Hz}$$'   
                    csm_value = csm[:,0,0]          
            else:
                if self.db:
                    y_label = r'PSD in $$\mathrm{dB}/\mathrm{Hz}$$'
                    csm_value = csm_dB[:,1,1]
                else:
                    y_label = r'PSD in $$\mathrm{Pa}^{2}/\mathrm{Hz}$$'     
                    csm_value = csm[:,1,1]              
        elif type == 'xy':
            title = "Cross Power Spectrum"
            if self.db:
                csm_value = csm_dB[:,0,1]
                y_label = r'PSD in $$\mathrm{dB}/\mathrm{Hz}$$'
            else:
                csm_value = csm[:,0,1]
                y_label = r'PSD in $$\mathrm{Pa}^{2}/\mathrm{Hz}$$'  
                
                
        fig = hv.Curve((f,np.abs(csm_value)),kdims="Frequency in Hz", vdims= y_label, label=title)
        fig.opts(color=color_value, shared_axes=False, width=750, height=350, show_grid=self.show_grid,
                logx=self.x_log, logy=self.y_log, xlim=(f[1], None) if self.x_log else (0, None),
                ylim=(np.min(np.abs(csm_value))-0.2*np.min(np.abs(csm_value)), np.max(np.abs(csm_value)) +
                        0.2*np.max(np.abs(csm_value)))) #if not self.y_log else (, None)))

        # Create a HoloViews pane for the figure
        plot_pane = HoloViews(fig,  sizing_mode='stretch_width' if self.stretch_value else None)

        # Update the corresponding tab with new signals
        self.tabs.component[3] = (self.tabs.str_analysis_function_tab, plot_pane)


    def create_correlation_plot(self,type=None):
        # set a own color picker for results
        color_value = self.color_picker_value[2]

        if type == 'xx':
            title = "Auto Correlation - Input"
            y_label = r'$$\mathrm{\psi}_{xx}(\mathrm{\tau})$$'
            corr = self.signal_process.correlation(type='xx')
            ylim = (-0.1,1.1)
        elif type == 'yy':
            title = "Auto Correlation - Output"
            y_label = r'$$\mathrm{\psi}_{yy}(\mathrm{\tau})$$'
            corr = self.signal_process.correlation(type='yy')
            ylim = (-0.1,1.1)
        elif type == 'xy':
            title = "Cross Correlation"
            y_label = r'$$\mathrm{\psi}_{xy}(\mathrm{\tau})$$'
            corr = self.signal_process.correlation(type='xy')
            ylim = (np.min(corr) - 0.1, np.max(corr) + 0.1)
        
        if len(corr) % 2 != 0:
            corr = np.roll(corr,1) # shift correlation to 1 sample
            
        # create time delay axis
        tau = self.signal_process.create_correlation_axis(len(corr))
        
        fig = hv.Curve((tau,corr),kdims=r'$$\mathrm{\tau}$$ in s', vdims=y_label, label=title )
        fig.opts(color=color_value, shared_axes=False, width=750, height=350, show_grid=self.show_grid,
                 xlim=(np.min(tau)+0.1*np.min(tau),np.max(tau)+0.1*np.max(tau)), 
                 ylim=ylim ,logx=False, logy=False)

        # Create a HoloViews pane for the figure
        plot_pane = HoloViews(fig,  sizing_mode='stretch_width' if self.stretch_value else None)

        # Update the corresponding tab with new signals
        self.tabs.component[3] = (self.tabs.str_analysis_function_tab, plot_pane)
