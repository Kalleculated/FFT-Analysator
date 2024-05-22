#Script für das Preprocessing. Beispiel Auswahl der Kanäle oder ähnliches.
import h5py
from pathlib import Path
import numpy as np

class Preprocess:

    def __init__(self,file_path):

        self.current_file = file_path
        self.channel_count = None
        self.channel_size = None
        self.selected_channel_data = None
        self.data = None
    def get_channel_data(self, channel):
        with h5py.File(self.current_file, 'r') as file:
            channel_data = np.array(file['time_data'][:])[:, channel]
        return channel_data
    def get_channel_size(self, channel):
        with h5py.File(self.current_file, 'r') as file:
            size = np.array(file['time_data'][:])[:, channel].shape[0]
        return size
    def count_channels(self):
        # Erstelle ein file-like object aus den Bytes
        with h5py.File(self.current_file, 'r') as file:
            # Zugriff auf den gewünschten Datensatz
            count = np.array(file['time_data'][:]).shape[1]
            # Die Anzahl der Kanäle (zweite Dimension der Daten)
        return count
