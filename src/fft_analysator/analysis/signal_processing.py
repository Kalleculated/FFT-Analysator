# Hier kommen unsere Funktionen wie Leistungsdichtespektrum, Korrelation etc.
import numpy as np
import scipy.fft as fft
import matplotlib.pyplot as plt
import scipy.signal as ss


class SignalProcess:
    def __init__(self, data):
        self.current_data = data

    def calculate_fft(self):
        fft_result = fft.fft(self.current_data)
        freqs = fft.fftfreq(len(self.current_data))
        freqs = freqs[:len(freqs)//2]  #es werdeb nur positive Frequenzen betrachtet
        fft_result = fft.fft(self.current_data)[:len(freqs)]       
        return fft_result, freqs

    def calculate_power_spectrum(self):
        # Calculate the power spectrum
        #fft_result = np.fft.fft(self.current_data)
        #power_spectrum = np.square(np.abs(fft_result))
        freqs , power_spectrum = ss.welch(self.current_data, window= "hann", nperseg =512 )
        return  freqs, power_spectrum

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





