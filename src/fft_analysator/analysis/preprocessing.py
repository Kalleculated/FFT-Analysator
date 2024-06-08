import io

import h5py
import numpy as np
import acoular as ac

class Preprocess:

    def __init__(self, file_paths=None):

        self.file_paths = file_paths
        self.source = ac.sources.TimeSamples(name=file_paths)

        if file_paths:
            self.table_key = self.get_table_names()[0]
            self.converted_file = self.convert_data()

        self.channel_count = None
        self.channel_size = None
        self.selected_channel_data = []
        self.data = None

        self.set_channel_data(0,2560)

    def set_channel_data(self, channel, block_size):
        for idx, data in enumerate(self.source.result(num=block_size)):
            self.selected_channel_data.append(data[:, channel])

    def get_data_block(self):

        return None

    def get_channel_size(self, channel):
        size = np.array(self.converted_file)[:, channel].shape[0]

        return size

    def get_channel_count(self):
        count = self.source.numchannels
        return count

    def get_abtastrate(self):
        abtastrate = self.source.sample_freq
        return abtastrate

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
