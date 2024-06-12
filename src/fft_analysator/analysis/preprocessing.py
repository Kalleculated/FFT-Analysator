import io

import h5py
import numpy as np
import acoular as ac


class Preprocess:

    def __init__(self, file_paths=None, block_size=512):

        self.file_paths = file_paths
        self.block_size = block_size

        if file_paths:
            self.table_key = self.get_table_names()[0]
            self.converted_file = self.convert_data()
            self.source = ac.sources.TimeSamples(name=self.file_paths)
            self.source_result = self.source.result(num=self.block_size)
            self.selected_data_block = next(self.source_result)

        self.current_block_idx = 0

        # brauchen wir das wirklich alles? wir sollten wirklich schauen, was wir als Attribut speichern
        # oft lohnt sich returnen und in der plot function weiterverarbeiten mehr
        self.data = None
        self.channel_count = None
        self.channel_size = None
        self.selected_channel_data = np.array([])

    def reinitialize_source(self):
        self.source = ac.sources.TimeSamples(name=self.file_paths)
        self.source_result = self.source.result(num=self.block_size)
        self.selected_data_block = next(self.source_result)

    def set_channel_data(self, channel):
        loop_list = []
        for data in self.source_result:
            loop_list = np.append(loop_list, data[:, channel])
        self.selected_channel_data = np.array(loop_list)

    def set_channel_on_data_block(self, channel):
        return self.selected_data_block[:, channel]

    def set_next_data_block(self):
        self.current_block_idx += 1
        self.selected_data_block = next(self.source_result)
        print('next')

    def set_current_channel(self, channel):
        self.current_channel = channel

    def set_data_block_to_idx(self, idx):
        self.current_block_idx = 0
        self.reinitialize_source()
        try:
            if idx > 0:
                for i in range(idx):
                    self.selected_data_block = next(self.source_result)
            print('previous')
        except StopIteration:
            print('End of file reached')


    def get_channel_size(self):
        size = np.array(self.converted_file)[:, self.current_channel].shape[0]
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
