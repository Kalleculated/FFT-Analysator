import panel as pn
import numpy as np
from tkinter import Tk, filedialog
import os
class FileExporter:
    def __init__(self):
        self.file_input_button = pn.widgets.Button
        self._component = self.file_input_button(name="Export", margin=(20, 0, 10, 10))
        self.dir_path = None

        # Reference müssen rein.
        self.chn1 = None
        self.chn2 = None
        self.method = None
        self.ext = None
        self.data = None
        pn.bind(self.select_directory, self._component, watch=True)

    def select_directory(self, event):
        root = Tk()
        root.withdraw()
        root.call('wm', 'attributes', '.', '-topmost', True)
        dir = filedialog.askdirectory(initialdir=os.getcwd())
        # Hier muss Code rein damit alle Attribute die aktuellen Werte gesetzt werden.
        # Exporter kommt da rein wo der Channel_selecetor geupdated wird (handle_sidebar_event)
        if dir:
            self.dir_path = dir
            self.export(self.dir_path, self.data, self.ext, self.chn1, self.chn2, self.method)
        else:
            self.dir_path = None
        root.destroy()

    def export(self, dir, data, ext, chn1, chn2, method):
        file_name = str(dir) + "/" + str(method) + "_" + str(chn1) + "_" + str(chn2)
        if ext == "Numpy":
            np.save(file_name, data)
        if ext == "Binary":
            data.astype(np.int64).tofile(file_name)
    @property
    def component(self):
        return self._component
