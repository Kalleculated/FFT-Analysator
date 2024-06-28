# Hier kommen unsere Funktionen wie Leistungsdichtespektrum, Korrelation etc.
import numpy as np
import scipy.fft as fft
import scipy.signal as sc
import acoular as ac

class Signal_Process:
    def __init__(self, file_path, window='Hanning', block_size=1024, overlap='50%'):
        self.file_path = file_path
        self.window = window
        self.block_size = block_size
        self.overlap = overlap

        if file_path:
            self.source = ac.MaskedTimeSamples(name=self.file_path)
            self.abtastrate = self.source.sample_freq
            self.numchannels_total = self.source.numchannels_total
            self.invalid_channel_list = []
            self.powerspectra = None
    
    def invalid_channels(self, valid_channels):
        self.invalid_channel_list = [k for k in range(self.numchannels_total) if k not in valid_channels] 
        self.source.invalid_channels = self.invalid_channel_list
    
    def csm(self, signal_x, signal_y, window='Hanning', block_size=1024, overlap='50%'):
        self.invalid_channels([signal_x, signal_y])
        self.powerspectra = ac.PowerSpectra(time_data=self.source, block_size=block_size, window=window, overlap=overlap)
        return self.powerspectra.csm
    #self.powerspectra[:,0,0]-> Autopowerspec from signal_x
    #self.powerspectra[:,1,1]-> Autopowerspec from signal_y
    #self.powerspectra[:,0,1]-> Crosspowerspec
    
    
    def frequency(self):
        return self.powerspectra.fftfreq()

    def coherence(self, signal_x, signal_y):
        csm_matrix = self.csm(signal_x, signal_y)
        coherence = np.abs(csm_matrix[:, 0, 1])**2 / (csm_matrix[:, 0, 0] * csm_matrix[:, 1, 1])
        return coherence
    
    def frequency_response(self, signal_x, signal_y):
        csm_matrix = self.csm(signal_x, signal_y)
        H = np.divide(csm_matrix[:, 0, 1], csm_matrix[:, 0, 0], out=np.zeros_like(csm_matrix[:, 0, 0]), where=(np.abs(csm_matrix[:, 0, 1]) > 1e-10))
        return H
    
    def impuls_response(self, signal_x, signal_y):
        csm_matrix = self.csm(signal_x, signal_y)
        H = np.divide(csm_matrix[:, 0, 1], csm_matrix[:, 0, 0], out=np.zeros_like(csm_matrix[:, 0, 0]), where=(np.abs(csm_matrix[:, 0, 1]) > 1e-10))
        n = len(csm_matrix[:, 0, 0])
        h = fft.irfft(H, n=n)
        time_axis = np.arange(n) / self.abtastrate
        return h, time_axis
        
        
    def corr(self, signal_x, signal_y):
        csm_matrix = self.csm(signal_x, signal_y)
        n = len(csm_matrix[:, 0, 0])
        
        corr_xx = fft.irfft(csm_matrix[:, 0, 0], n=n)
        corr_yy = fft.irfft(csm_matrix[:, 1, 1], n=n)
        corr_xy = fft.irfft(csm_matrix[:, 0, 1], n=n)
        
        time_axis = np.arange(n) / self.abtastrate
        
        return corr_xx, corr_yy, corr_xy, time_axis

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
