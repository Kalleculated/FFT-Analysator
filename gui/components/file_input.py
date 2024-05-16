import panel as pn

class FileInputComponent:
    def __init__(self):
        # Direkt das FileInput-Widget als Attribut speichern
        self._component = pn.widgets.FileInput(accept=".h5", multiple=True)

    @property
    def component(self):
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component
