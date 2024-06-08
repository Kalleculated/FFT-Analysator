import io

import h5py
import numpy as np
import acoular as ac

class Preprocess:

    def __init__(self, file_paths=None, block_size=512):

        self.file_paths = file_paths
        self.block_size = block_size

        self.source = ac.sources.TimeSamples(name=self.file_paths)
        self.source_result = self.source.result(num=self.block_size)

        if file_paths:
            self.table_key = self.get_table_names()[0]
            self.converted_file = self.convert_data()

        self.data = None
        self.channel_count = None
        self.channel_size = None
        self.selected_channel_data = np.array([])
        self.selected_channel_data_block = None
        self.block_idx = 0
        self.current_channel = 0

    def set_channel_data(self, channel):
        self.current_channel = channel
        for idx, data in enumerate(self.source_result):
            self.selected_channel_data = np.append(self.selected_channel_data, data[:, channel])

    def set_channel_data_block(self,channel):
        self.block_idx = self.block_idx + 1
        for idx in range(self.block_idx):
            self.selected_channel_data_block = next(self.source_result)[:, channel]

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
