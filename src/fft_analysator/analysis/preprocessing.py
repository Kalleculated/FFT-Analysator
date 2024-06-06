import io

import h5py
import numpy as np


class Preprocess:

    def __init__(self, file_paths=None):

        self.file_paths = file_paths

        if file_paths:
            self.table_key = self.get_table_names()[0]
            self.converted_file = self.convert_data()

        self.channel_count = None
        self.channel_size = None
        self.selected_channel_data = None
        self.data = None

    def get_channel_data(self, channel):
        data = np.array(self.converted_file)[:, channel]

        return data

    def get_channel_size(self, channel):
        size = np.array(self.converted_file)[:, channel].shape[0]

        return size

    def get_channel_count(self):
        count = np.array(self.converted_file).shape[1]

        return count

    def get_abtastrate(self):
        # Muss noch befüllt werden. Vermutlich bietet Acourlar hier eine Funktion oder es kann aus dem Datenset
        # gelesen werden
        return None

    def convert_data(self):
        with h5py.File(self.file_paths, 'r') as file:
            # Zugriff auf den gewünschten Datensatz
            data = file[self.table_key][:]  # type: ignore

        return data

    def get_table_names(self):
        with h5py.File(self.file_paths, 'r') as file:
            # Zugriff auf den gewünschten Datensatz
            keys = list(file.keys())

        return keys
