from os import getcwd
from os import path
import numpy as np
import h5py
from acoular import __file__ as bpath, MicGeom, WNoiseGenerator, PointSource, Mixer, WriteH5, SineGenerator


sfreq = 51200
duration = 100
n_channels = 64  # Number of channels
nsamples = duration*sfreq

folder_name = "test_data"
current_directory = getcwd()
full_path = path.join(current_directory, folder_name)
h5savefile = path.join(full_path, 'sine_waves.h5')
#micgeofile = path.join(path.split(bpath)[0],'xml','array_64.xml')

# Initialize an array to hold the data for all channels
data = np.zeros((nsamples, n_channels))

# Generate sine waves for each channel with different frequencies
for channel in range(n_channels):
    freq = (channel + 1) * 10  # Example frequency increment: 10 Hz per channel
    t = np.arange(nsamples) / sfreq
    sine_wave = np.sin(2 * np.pi * freq * t)
    data[:, channel] = sine_wave

# Save the data to an .h5 file
with h5py.File(h5savefile, 'w') as f:
    f.create_dataset('sine_data', data=data)


""""
sin = SineGenerator(sample_freq=51200, numsamples=51200*100, freq=10)
#sin = SineGenerator(sample_freq=51200, numsamples=51200*100, freq=100)
#sin = SineGenerator(sample_freq=51200, numsamples=51200*100, freq=1000)
#sin = SineGenerator(sample_freq=51200, numsamples=51200*100, freq=1000)

# Daten generieren (hier nur beispielhaft als Zufallszahlen)
data_64_channels = np.random.rand(6400).reshape(100, 64)  # Beispiel für 64 Kanäle
data_32_channels = np.random.rand(3200).reshape(100, 32)  # Beispiel für 32 Kanäle

# h5py verwenden, um die Daten in einer Datei zu speichern
with h5py.File(h5savefile, 'w') as f:
    f.create_dataset('time_data', data=data_64_channels)
    f.create_dataset('channel_data', data=data_32_channels)
"""

