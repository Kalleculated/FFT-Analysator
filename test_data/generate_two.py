import h5py
import numpy as np
from os import getcwd, path
from acoular import __file__ as bpath, MicGeom, WNoiseGenerator, PointSource, Mixer

folder_name = "test_data"
current_directory = getcwd()
full_path = path.join(current_directory, folder_name)
h5savefile = path.join(full_path, 'combined_sources.h5')

# Daten generieren (hier nur beispielhaft als Zufallszahlen)
data_64_channels = np.random.rand(6400).reshape(100, 64)  # Beispiel für 64 Kanäle
data_32_channels = np.random.rand(3200).reshape(100, 32)  # Beispiel für 32 Kanäle

# h5py verwenden, um die Daten in einer Datei zu speichern
with h5py.File(h5savefile, 'w') as f:
    f.create_dataset('time_data', data=data_64_channels)
    f.create_dataset('channel_data', data=data_32_channels)
