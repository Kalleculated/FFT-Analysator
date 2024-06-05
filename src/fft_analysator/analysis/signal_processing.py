# Hier kommen unsere Funktionen wie Leistungsdichtespektrum, Korrelation etc.
import os
import numpy as np
import fft_analysator.analysis.preprocessing as pp
import scipy as sc
import matplotlib.pyplot as plt
import acoular as ac
class Signal_process:
    def __init__(self, signal1, signal2):
        self.signal1 = signal1
        self.signal2 = signal2

        #self.signal1_h5 = pp.Preprocess.binary_to_h5(self.signal1)
        #self.signal2_h5 = pp.Preprocess.binary_to_h5(self.signal2)
        #self.signal1_np = signal1.numpy_file
        #self.signal2_np = signal2.numpy_file


    def FFT(self):
        data = ac.TimeSamples(name = self.signal1)
        #data_fft = ac.BaseSpectra(source = data)
        data_fft2 = ac.FFTSpectra(source = data)
        a = data_fft2.fftfreq()
        print(a)
        return None


"""
    def power_spectral_density(self, channel, window, seg_len, seg_over):
        channel_data = self.signal1.get_channel_data(channel)
        f, p_xx = sc.signal.welch(x=channel_data, window=window, nperseg=seg_len, noverlap=seg_over) # Check für Normierung
        return [f, p_xx]

    def cross_power_spectral_density(self, channel1, channel2, window, seg_len, seg_over):
        channel_data1 = self.signal1.get_channel_data(channel1)
        channel_data2 = self.signal2.get_channel_data(channel2)

        f, p_xy = sc.signal.csd(channel_data1, channel_data2, window=window, nperseg=seg_len, noverlap=seg_over)
        return [f, p_xy]

"""



