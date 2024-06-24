# Hier kommen unsere Funktionen wie Leistungsdichtespektrum, Korrelation etc.
import numpy as np
import scipy.fft as fft
import scipy.signal as sc
import acoular as ac

class Signal_Process:
    def __init__(self, file_path, channel_x, channel_y, window='Hanning', block_size=1024, overlap='50%'):
        self.file_path = file_path
        self.window = window
        self.block_size = block_size
        self.overlap = overlap
        self.channel_x = channel_x
        self.channel_y = channel_y

        if file_path:
            self.source = ac.MaskedTimeSamples(name=self.file_path)
            self.abtastrate = self.source.sample_freq
            self.numchannels_total = self.source.numchannels_total
            self.invalid_channel_list = [k for k in range(self.numchannels_total) if k not in [self.channel_x, self.channel_y]] # type: ignore
            self.source.invalid_channels = self.invalid_channel_list
            
    
    def update_invalid_channels(self, valid_channels):
        self.invalid_channel_list = [k for k in range(self.numchannels_total) if k not in valid_channels] # type: ignore
        self.source.invalid_channels = self.invalid_channel_list
    
    def csm_x_x(self):
        self.update_invalid_channels([self.channel_x])
        powerspektren = ac.PowerSpectra(time_data=self.source, block_size=self.block_size, window=self.window, overlap=self.overlap)
        freq = powerspektren.fftfreq()
        return powerspektren.csm[:, 0, 0], freq
    
    def csm_y_y(self):
        self.update_invalid_channels([self.channel_y])
        powerspektren = ac.PowerSpectra(time_data=self.source, block_size=self.block_size, window=self.window, overlap=self.overlap)
        freq = powerspektren.fftfreq()
        return powerspektren.csm[:, 0, 0], freq
    
    def csm_x_y(self):
        self.update_invalid_channels([self.channel_x, self.channel_y])
        powerspektren = ac.PowerSpectra(time_data=self.source, block_size=self.block_size, window=self.window, overlap=self.overlap)
        freq = powerspektren.fftfreq()
        return powerspektren.csm[:, 0, 1], freq
    
    def coherence(self):    
        csm_xx, freq = self.csm_x_x()  #unsicher wegen den frequenzen
        csm_yy, _ = self.csm_y_y()  
        csm_xy, _ = self.csm_x_y()  
        coherence = np.abs(csm_xy)**2 / (csm_xx * csm_yy)
        return coherence, freq
    
    def frequency_response(self):
        csm_xy, freq = self.csm_x_y() 
        csm_xx, _ = self.csm_y_y()  
        H = np.divide(csm_xy,csm_xx, out=np.zeros_like(csm_xx), where=(np.abs(csm_xy) > 1e-10))
        return H, freq
    
    
    
    
    


"""
    def calculate_fft(self, data):
        fft_result = fft.rfft(data)
        freqs = fft.rfftfreq(len(data), d=1 / self.current_data_abtastrate)
        return freqs, fft_result

    def calculate_cross_spectrum(self, window="hann", seg_length=1024, overlap=512):
        f, Pxy = sc.csd(x=self.current_data_input, y=self.current_data_output, window=window, nperseg=seg_length,
                        noverlap=overlap)
        return f, Pxy

    def calculate_correlation(self):
        corr = sc.correlate(self.current_data_input, self.current_data_output, mode='same')
        return corr

    def calculate_coherence(self, window='hann', seg_length=1024, overlap=512):
        f, Cxy = sc.coherence(self.current_data_input, self.current_data_output, fs=self.current_data_abtastrate,
                              window=window, nperseg=seg_length, noverlap=overlap)
        return f, Cxy

    def calculate_impulse_response(self):
        freq_x, FFT_X = self.calculate_fft(self.current_data_input)
        freq_y, FFT_Y = self.calculate_fft(self.current_data_output)
        H = np.divide(FFT_X, FFT_Y, out=np.zeros_like(FFT_X), where=(np.abs(FFT_Y) > 1e-10))
        h = fft.irfft(H, n=len(self.current_data_input))
        N = len(self.current_data_input)
        time_axis = np.arange(N) / self.current_data_abtastrate
        return time_axis, h

    def calculate_frequency_response(self):
        freq_x, FFT_X = self.calculate_fft(self.current_data_input)
        freq_y, FFT_Y = self.calculate_fft(self.current_data_output)
        H = np.divide(FFT_X, FFT_Y, out=np.zeros_like(FFT_X), where=(np.abs(FFT_Y) > 1e-10))
        return freq_x, H
"""
