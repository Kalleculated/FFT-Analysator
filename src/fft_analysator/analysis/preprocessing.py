import h5py
from acoular import sources as ac
import numpy as np


class Preprocess:
    """
    The Preprocess class handles everything after importing the user file. It is an interface between Acoular and our
    internal Signalprocessing class. It contains information about the block size, data, channel count and size and
    sample frequency. It is able to return the complete data as a Numpy array or iterate over the defined block size.

    Attributes:
        file_paths (str): A Path to import.
        block_size (int): Block size for processing.
        table_key (str): Table key names.
        source (TimeSamples): Acoular TimeSamples class.
        source_result (generator): Generator of the current block result.
        selected_data_block (numpy_array): Selected data block.
        current_block_idx (int): Index of the current data block.
        selected_channel_data (numpy_array): All data of selected channel.


    Methods:
        reinitialize_source(): Reinitializes the generator
        set_channel_data(int): Gives the complete data of a channel
        set_channel_on_data_block(int): Gives the data block of a channel
        set_next_data_block(): Gives the next data block
        set_current_channel(int): Changes the current selected channel
        set_data_block_to_idx(int): Returns the data block of an idx
        get_channel_size(): Gets the channel size
        get_channel_count(): Gets the channel count
        get_abtastrate(): Gets the sample frequency
        get_table_names(): Gets the table names
    """
    def __init__(self, file_paths=None, block_size=1024):
        """
        Constructs all the necessary attributes for the Preprocess object.


        Args:
            file_paths (object): Get the callback to the data object
            block_size (int): Length of data block.
        """

        self.file_paths = file_paths
        self.block_size = block_size

        if file_paths:
            self.table_key = self.get_table_names()[0]
            self.source = ac.TimeSamples(name=self.file_paths)
            self.source_result = self.source.result(num=self.block_size)
            self.selected_data_block = next(self.source_result)

        self.current_block_idx = 0

        self.selected_channel_data = np.array([])

    def reinitialize_source(self):
        """
        The reinitialize_source function reinitializes the generator from Acoular. It is used for returning to already
        viewed data blocks.
        """
        self.current_block_idx = 0
        self.source = ac.TimeSamples(name=self.file_paths)
        self.source_result = self.source.result(num=self.block_size)
        self.selected_data_block = next(self.source_result)


    def set_channel_data(self, channel):
        """
        Set_channel_data sets returns the complete channel by iterating over the generator of Acoular and
        saving the data blocks in a Numpy Array.

        Args:
            channel (int): Channel number.
        """
        loop_list = []
        for data in self.source_result:
            loop_list.extend(data[:, channel])
        self.selected_channel_data = np.array(loop_list)

    def set_channel_on_data_block(self, channel):
        """
        Set_channel_data_on_data_block sets returns the block data of a channel as a Numpy Array.

        Args:
            channel (int): Channel number.
        Returns:
            numpy_array
        """
        return self.selected_data_block[:, channel]

    def set_next_data_block(self):
        """
        Set_next_data_block sets the attribute selected_data_block by selecting the next element of
        the generator from Acoular and saving this data blocks in a Numpy Array.
        """
        self.current_block_idx += 1
        self.selected_data_block = next(self.source_result)

    def set_current_channel(self, channel):
        """
        Set_current_channel sets the attribute current_channel by taking a channel.

        Args:
            channel (int): Channel number switching to.
        """
        self.current_channel = channel

    def set_data_block_to_idx(self, idx):
        """
        Set_data_block_to_idx sets the attribute selected_data_block by selecting a specific element of
        the generator from Acoular and saving this data blocks in a Numpy Array.

        Args:
            idx (int): Idx element to which the generator iterates to.
        """
        self.reinitialize_source()
        try:
            self.current_block_idx = idx
            if idx > 0:
                for i in range(idx):
                    self.selected_data_block = next(self.source_result)
        except StopIteration:
            print('End of file reached')

    def get_channel_size(self):
        """
        Get_channel_size returns the size of the current channel

        Returns:
            size (int): Channel size
        """
        size = np.array(self.converted_file)[:, self.current_channel].shape[0]

        return size

    def get_channel_count(self):
        """
        Get_channel_count returns the number of channels of the current .h5 file

        Returns:
            count (int): Number of channels
        """
        count = self.source.numchannels

        return count

    def get_abtastrate(self):
        """
        Get_abtastrate returns the sample_freq from the current .h5 file via Acoular

        Returns:
            abtasterate (int): Sample Frequency
        """
        abtastrate = self.source.sample_freq

        return abtastrate

    def get_table_names(self):
        """
        Get_table_names returns a list of all data set keyword contained in the current .h5 File

        Returns:
            keys (list): A list of table names
        """
        with h5py.File(self.file_paths, 'r') as file:
            # Zugriff auf den gewünschten Datensatz
            keys = list(file.keys())

        return keys
