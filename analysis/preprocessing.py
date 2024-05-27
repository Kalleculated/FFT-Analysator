#Script für das Preprocessing. Beispiel Auswahl der Kanäle oder ähnliches.
import h5py
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
            data = np.array(file['time_data'][:])[:, channel]
        return data

    def get_channel_size(self, channel):
        with h5py.File(self.current_file, 'r') as file:
            size = np.array(file['time_data'][:])[:, channel].shape[0]
        return size

    def get_channel_count(self):
        # Erstelle ein file-like object aus den Bytes
        with h5py.File(self.current_file, 'r') as file:
            # Zugriff auf den gewünschten Datensatz
            count = np.array(file['time_data'][:]).shape[1]
            # Die Anzahl der Kanäle (zweite Dimension der Daten)
        return count

    def get_abtastrate(self):
        # Muss noch befüllt werden. Vermutlich bietet Acourlar hier eine Funktion oder es kann aus dem Datenset gelesen
        # gelesen werden
        return "test"
    



print(Preprocess.get_abtastrate(Preprocess))


