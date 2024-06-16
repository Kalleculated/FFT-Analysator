# Hier kommen unsere Funktionen wie Leistungsdichtespektrum, Korrelation etc.
import numpy as np
import scipy.fft
import scipy.fft as fft
import matplotlib.pyplot as plt
import scipy.signal as ss


class SignalProcess:
    def __init__(self, data):
        self.current_data = data # Muss angepasst werden bzw. wird eigentlich nicht benötigt.

    def calculate_fft(self, signal):
        # Perform the FFT
        fft_result = np.fft.fft(signal)
        freqs = np.fft.fftfreq(len(signal))
        return fft_result, freqs

    def calculate_cross_spectrum(self, signal_x, signal_y, window="hann", seg_length=1024, overlap=512):
        # Calculates the cross power spectra density of two signals.
        # If x and y are the same signal, this will calculate instead the power spectral density of this signal
        f, Pxy = ss.csd(x=signal_x, y=signal_y, window=window, nperseg=seg_length, noverlap=overlap)

        return f, Pxy

    def calculate_correlation(self, signal_x, signal_y):
        return ss.correlate(signal_x, signal_y)


"""
    def plot_power_spectrum(self, power_spectrum, freqs):
        plt.figure(figsize=(10, 6))
        plt.semilogy(freqs, power_spectrum)
        plt.title("Power Spectrum of the Signal")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Power")
        plt.grid(True)
        plt.show()

    def plot_fft(self):
        fft_result, freqs = self.calculate_fft()
        plt.figure(figsize=(10, 6))
        plt.plot(freqs, np.abs(fft_result))
        plt.title("FFT of Channel")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude")
        plt.grid(True)
        plt.show()


# Beispielhafte Verwendung mit der Preprocess-Klasse
#file_paths = "three_sources.h5"
#preprocessor = Preprocess(file_paths=file_paths, block_size=1024)
#preprocessor.set_current_channel(10)  # Setze den aktuellen Kanal auf Kanal 10
#preprocessor.set_channel_data()      # Sammle die Daten des aktuellen Kanals

# Erstellen einer Instanz von SignalProcess und FFT durchführen
#signal_processor = SignalProcess(preprocessor.selected_channel_data)
#signal_processor.plot_fft()


# Plotten des Leistungsdichtespektrums
#signal_processor.plot_power_spectrum(power_spectrum, freqs)


"""
