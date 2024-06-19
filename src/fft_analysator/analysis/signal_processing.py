# Hier kommen unsere Funktionen wie Leistungsdichtespektrum, Korrelation etc.
import numpy as np
import scipy.fft as fft
import scipy.signal as sc


class Signal_Process:
    def __init__(self, data1, data2, abtastrate):
        self.current_data_input = data1
        self.current_data_output = data2
        self.current_data_abtastrate = abtastrate

    def calculate_fft(self, data):
        fft_result = fft.rfft(data)
        freqs = fft.rfftfreq(len(data), d=1/self.current_data_abtastrate)
        return freqs, fft_result

    def calculate_cross_spectrum(self, window="hann", seg_length=1024, overlap=512):
        f, Pxy = ss.csd(x=self.current_data_input, y=self.current_data_output, window=window, nperseg=seg_length, noverlap=overlap)
        return f, Pxy


    def calculate_correlation(self):
        corr = ss.correlate(self.current_data_input, self.current_data_output, mode='same')
        return corr
    
    def calculate_power_spectrum(self,data, window= "hann", nperseg =512 ):
        freqs , power_spectrum = sc.welch(data, window= "hann", nperseg =512 )
        return  freqs, power_spectrum
    
    
    def calculate_coherence(self, window='hann', seg_length=1024, overlap=512):
        f, Cxy = sc.coherence(self.current_data_input, self.current_data_output, fs=self.current_data_abtastrate, window=window, nperseg=seg_length, noverlap=overlap)
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











