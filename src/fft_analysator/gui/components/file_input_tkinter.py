import panel as pn
pn.extension('tabulator', 'terminal', 'ipywidgets',sizing_mode = 'stretch_width', loading_spinner='dots')

from tkinter import Tk, filedialog

class FileInputComponent:
    def __init__(self):
        self.file_input_button = pn.widgets.Button
        self._component = self.file_input_button(name="Load file")
        self._component.on_click(self.select_files)

    def select_files(self, *b):
        root = Tk()
        root.withdraw()
        root.call('wm', 'attributes', '.', '-topmost', True)
        files = filedialog.askopenfilename(multiple=False)
        print(files)
        return files

    @property
    def component(self):
        return self._component
