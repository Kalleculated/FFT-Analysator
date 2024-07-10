import panel as pn


class DataSelector:
    """
    A class used to represent a Data Selector widget.

    Attributes
    ----------
    selector : object
        An instance of the panel Select widget.
    options : list
        A list of options for the selector widget. Initially empty.
    _component : object
        The panel Select widget with specific parameters.
    """

    def __init__(self):
        self.selector = pn.widgets.Select
        self.options = []
        self._component = self.selector(name='', options=self.options, size=len(self.options)+2,
                                        margin=(20, 0, 0, 20), height=30, width=200)

    @property
    def component(self):
        """
        Gets the stored widget.

        Returns
        -------
        object
            The stored widget.
        """
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component
