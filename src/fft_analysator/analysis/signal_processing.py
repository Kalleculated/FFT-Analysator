# Hier kommen unsere Funktionen wie Leistungsdichtespektrum, Korrelation etc.
import numpy as np
import scipy.fft as fft
import scipy.signal as sc
import acoular as ac

class Signal_Process:
    def __init__(self, TimeSamples, abtastrate, window='Hanning',block_size=1024,overlap='50%'):

        self.current_data_abtastrate = abtastrate
        self.current_block_idx = 0
        self.timesamples = TimeSamples
        self.abtastrate = abtastrate
        self.window = window
        self.block_size = block_size
        self.overlap = overlap

        if TimeSamples:
            self.FFT_gen = ac.FFTSpectra(source=self.timesamples, window=self.window, block_size=self.block_size, overlap=self.overlap)
            self.FFT_gen_current_result = next(self.FFT_gen.result())
            self.Power_gen = ac.PowerSpectra(time_data=self.timesamples,window=self.window, block_size=self.block_size, overlap=self.overlap)
            self.Power_gen_csm = self.Power_gen.csm

    def reinitialize_source(self):
        self.current_block_idx = 0
        self.FFT_gen = ac.FFTSpectra(source=self.timesamples, window=self.window, block_size=self.block_size, overlap=self.overlap)
        self.FFT_gen_current_result = next(self.FFT_gen.result())
        self.Power_gen = ac.PowerSpectra(time_data=self.timesamples, window=self.window, block_size=self.block_size, overlap=self.overlap)
        self.Power_gen_csm = self.Power_gen.csm
    def get_next_FFT_block(self):
        self.FFT_gen_current_result = next(self.FFT_gen.result())
        self.current_block_idx = self.current_block_idx + 1
        return self.FFT_gen_current_result

    def get_average_FFT(self):
        all_blocks = np.array([np.abs(block) for block in self.FFT_gen.result()])
        average_FFT = np.mean(all_blocks, axis=0)
        return average_FFT

    def get_csm(self,x,y):
        return self.Power_gen_csm[:,x,y]

    def get_frequencies(self):
        return np.fft.rfftfreq(self.FFT_gen.block_size, d=1/self.timesamples.sample_freq)
    def get_coherence(self,x,y):
        return abs(2*self.get_csm(x,y))/(self.get_csm(x,x)*self.get_csm(y,y))

    def get_impulse_response(self,x,y):
        FFT_x = self.get_average_FFT()[:,x]
        FFT_y = self.get_average_FFT()[:,y]
        H = np.divide(FFT_x, FFT_y, out=np.zeros_like(FFT_x), where=(np.abs(FFT_y) > 1e-10))
        n = len(FFT_x)
        h = fft.irfft(H, n=n)
        time_axis = np.arange(n) / self.abtastrate
        return time_axis, h

    def get_impulse_response(self,x,y):
        FFT_x = self.get_average_FFT()[:,x]
        FFT_y = self.get_average_FFT()[:,y]
        H = np.divide(FFT_x, FFT_y, out=np.zeros_like(FFT_x), where=(np.abs(FFT_y) > 1e-10))
        time_axis = self.get_frequencies()
        return time_axis, H

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
