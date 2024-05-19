import h5py
import io

def count_channels(file_data):
    # Erstelle ein file-like object aus den Bytes
    #print(io.BytesIO(file_data))
    with h5py.File(io.BytesIO(file_data[0]), 'r') as file:
        # Zugriff auf den gewünschten Datensatz
        data = file['time_data'][:]
        # Die Anzahl der Kanäle (zweite Dimension der Daten)
        # Test ob das Commit + Branches geht.
        # Commite ich im richtigen Branch?
    return data
