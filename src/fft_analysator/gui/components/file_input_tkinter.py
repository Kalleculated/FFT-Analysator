import panel as pn

from tkinter import Tk, filedialog
import os

class FileInputComponent:
    def __init__(self):
        self.file_input_button = pn.widgets.Button
        self._component = self.file_input_button(name="Load file", margin=(20, 0, 10, 10))
        self.file_paths = None
        pn.bind(self.select_files, self._component, watch=True)

    def select_files(self, event):
        root = Tk()
        root.withdraw()
        root.call('wm', 'attributes', '.', '-topmost', True)
        files = filedialog.askopenfilename(
            multiple=False,
            filetypes=[("HDF5 files", "*.h5")],  # Nur .h5 Dateien erlauben
            initialdir=os.getcwd()  # Starten im aktuellen Verzeichnis
        )
        if files:
            self.file_paths = files
        else:
            self.file_paths = None
        root.destroy()

    @property
    def component(self):
        return self._component
