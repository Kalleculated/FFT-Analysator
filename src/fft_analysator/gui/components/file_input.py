import panel as pn


class FileInputComponent:
    """
    A class used to represent a File Input Component.

    Attributes
    ----------
    file_input : object
        An instance of the panel FileInput widget.
    _component : object
        The panel FileInput widget with specific parameters.

    Methods
    -------
    component()
        Gets the stored widget.
    """

    def __init__(self):
        self.file_input = pn.widgets.FileInput
        self._component = self.file_input(accept=".h5", multiple=True)

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
