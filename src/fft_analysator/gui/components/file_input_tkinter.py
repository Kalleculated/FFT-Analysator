import panel as pn

from tkinter import Tk, filedialog
import os

class FileInputComponent:
    """
    A class used to represent a File Input Component.

    Attributes
    ----------
    file_input_button : object
        An instance of the panel Button widget.
    _component : object
        The panel Button widget with specific parameters.
    file_paths : str
        The paths of the selected files. Initially None.

    Methods
    -------
    select_files(event)
        Opens a file dialog to select files.
    component()
        Gets the stored widget.
    """
    def __init__(self):
        self.file_input_button = pn.widgets.Button
        self._component = self.file_input_button(name="Load file", margin=(20, 0, 10, 10))
        self.file_paths = None
        pn.bind(self.select_files, self._component, watch=True)

    def select_files(self, event):
        """
        Opens a file dialog to select files.

        Args:
            event (object): The event object passed by the panel Button widget.
        """
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
        """
        Gets the stored widget.

        Returns
        -------
        object
            The stored widget.
        """
        return self._component
