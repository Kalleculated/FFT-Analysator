# Hier kommen unsere Funktionen wie Leistungsdichtespektrum, Korrelation etc.
import acoular as ac
import numpy as np
import fft_analysator.analysis.preprocessing as pp
import matplotlib.pyplot as plt


class Signa_lAnalyzer:
    def __init__(self, file_paths, block_size=512):
        self.preprocess = pp.Preprocess(file_paths=file_paths, block_size=block_size)

    def set_current_channel(self, channel):
        self.preprocess.set_current_channel(channel)

    def calculate_fft(self):
        self.preprocess.set_channel_data()  
        channel_data = self.preprocess.selected_channel_data
        fft_result = fft.fft(channel_data)
        freqs = fft.fftfreq(len(channel_data))
        return freqs, np.abs(fft_result)

    def calculate_power_spectrum(self):
        freqs, fft_result = self.calculate_fft()
        power_spectrum = np.square(np.abs(fft_result))
        return freqs, power_spectrum


    def plot_fft(self):
        freqs, fft_result = self.calculate_fft()
        plt.figure(figsize=(10, 6))
        plt.plot(freqs, fft_result)
        plt.title("FFT of Channel")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude")
        plt.grid(True)
        plt.show()


