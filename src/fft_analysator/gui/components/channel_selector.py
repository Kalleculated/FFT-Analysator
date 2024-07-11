import panel as pn


class ChannelSelector:
    """
    A class used to represent a Channel Selector widget.

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
        """
        The selector attribute is initialized as a panel Select widget.
        """
        self.selector = pn.widgets.Select
        self.options = []
        self._component = self.selector(name='No data chosen!', options=self.options, width=135, margin=(10,15),
                                        disabled=True)

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
