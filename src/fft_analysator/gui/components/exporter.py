import panel as pn
import numpy as np
from tkinter import Tk, filedialog
import os


class FileExporter:
    """
    A class used to export files.

    Attributes:
        file_input_button (pn.widgets.Button):
            An instance of the Panel Button widget.
        _component (pn.widgets.Button):
            The Panel Button widget with specific parameters.
        dir_path (str):
            The directory path where the file will be saved.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the FileExporter object.

        Attributes:
            file_input_button (pn.widgets.Button):
                An instance of the Panel Button widget.
            _component (pn.widgets.Button):
                The Panel Button widget with specific parameters.
            dir_path (str):
                The directory path where the file will be saved.
        """
        self.file_input_button = pn.widgets.Button
        self._component = self.file_input_button(name='\U0001F4BE ' 'Save and Export', margin=(10, 0, 10, 10), width=150,
                                                 disabled=True)
        self.dir_path = None

    def select_directory(self, event, data, chn1, chn2, method, ext, window, overlap):
        """
        Selects the directory and saves the data.

        Args:
            event (object): The event that triggers the directory selection.
            data (np.array): The data to be saved.
            chn1 (int): The first channel.
            chn2 (int): The second channel.
            method (str): The method used.
            ext (str): The file extension.
            window (str): The window type.
            overlap (float): The overlap value.

        Returns:
            None
        """
        root = Tk()
        root.withdraw()
        root.call('wm', 'attributes', '.', '-topmost', True)
        dir = filedialog.askdirectory(initialdir=os.getcwd())
        method = method.replace(" ", "")
        #data = np.array(data)
        if dir:
            self.dir_path = dir
            file_name = str(dir) + "/" + str(method) + "_" + str(chn1) + "_" + str(chn2) + "_" + str(window) + "_" + str(overlap)
            if ext == "Numpy Array":
                np.save(file_name, data)
            if ext == "Binary":
                data = np.abs(data)
                data.tofile(file_name)
        else:
            self.dir_path = None
        root.destroy()

    @property
    def component(self):
        """
        Gets the stored widget.

        Returns:
            _component (object):
                The stored widget.
        """
        return self._component
