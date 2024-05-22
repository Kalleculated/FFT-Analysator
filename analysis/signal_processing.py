import h5py
import io
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

def get_channel_data(h5_file, channel):
    with h5py.File(h5_file, 'r') as file:
        channel_data = np.array(file['time_data'][:])[:, channel]
    return channel_data
def get_channel_size(h5_file, channel):
    with h5py.File(h5_file, 'r') as file:
        size = np.array(file['time_data'][channel])
    return size

def count_channels(h5_file):
    # Erstelle ein file-like object aus den Bytes
    with h5py.File(h5_file, 'r') as file:
        # Zugriff auf den gewünschten Datensatz
        count = np.array(file['time_data'][:]).shape[1]
        # Die Anzahl der Kanäle (zweite Dimension der Daten)
    return count


data_directory = Path.joinpath(Path().absolute().parent, "test_data")
file_path = Path.joinpath(data_directory, "three_sources.h5")

channel_nr = count_channels(file_path)
channel_info = get_channel_data(file_path, 1)
channel_size = get_channel_size(file_path, 1)

print(channel_info)
print(channel_size)
print(channel_info.shape)
