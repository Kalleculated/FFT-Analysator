import panel as pn
import numpy as np
from tkinter import Tk, filedialog
import os
class FileExporter:
    def __init__(self):
        self.file_input_button = pn.widgets.Button
        self._component = self.file_input_button(name='\U0001F4BE ' 'Save and Export', margin=(10, 0, 10, 10), width=150)
        self.dir_path = None

        # Reference müssen rein.
        #self.chn1 = None
        #self.chn2 = None
        #self.method = None
        #self.ext = None
        #self.data = None
        #pn.bind(self.select_directory, self._component, watch=True)

    def select_directory(self, event, data, chn1, chn2, method, ext):
        root = Tk()
        root.withdraw()
        root.call('wm', 'attributes', '.', '-topmost', True)
        dir = filedialog.askdirectory(initialdir=os.getcwd())
        method = method.replace(" ", "_")
        print(ext)
        if dir:
            self.dir_path = dir
            file_name = str(dir) + "/" + str(method) + "_" + str(chn1) + "_" + str(chn2)
            print(file_name)
            if ext == "Numpy Array":
                np.save(file_name, data)
            if ext == "Binary":
                data.astype(np.int64).tofile(file_name)
        else:
            self.dir_path = None
        root.destroy()

    @property
    def component(self):
        return self._component
