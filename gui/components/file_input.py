import panel as pn

class FileInputComponent:
    def __init__(self):
        self.file_input = pn.widgets.FileInput
        self._component = self.file_input(accept=".h5", multiple=True)

    @property
    def component(self):
        return self._component