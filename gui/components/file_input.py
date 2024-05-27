import panel as pn

class FileInputComponent:
    def __init__(self):
        # Direkt das FileInput-Widget als Attribut speichern
        self.file_input = pn.widgets.FileInput
        self._component = self.file_input(accept=".h5", multiple=True)

    @property
    def component(self):
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component