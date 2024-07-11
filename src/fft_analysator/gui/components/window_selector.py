import panel as pn


class WindowSelector:
    """
    A class used to represent a Window Selector widget.

    This class encapsulates a panel Select widget and provides an interface for populating it with window options and retrieving the selected option.

    Attributes
    ----------
    selector : object
        An instance of the panel Select widget.
    options : list
        A list of options for the selector widget.
    _component : object
        The panel Select widget with specific parameters.

    Methods
    -------
    component()
        Gets the stored widget.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the WindowSelector object.

        The selector attribute is initialized as a panel Select widget.
        The options attribute is initialized with a list of window options.
        The _component attribute is initialized as a panel Select widget with specific parameters.
        """
        self.selector = pn.widgets.Select
        self.options = ['Hanning', 'Rectangular', 'Hamming', 'Bartlett', 'Blackman']
        self._component = self.selector(name='Choose window:', options=self.options, width=140, value='Hanning',
                                        disabled=True)

    @property
    def component(self):
        """
        Gets the stored widget.

        This method returns the panel Select widget stored in the _component attribute.

        Returns
        -------
        object
            The stored widget.
        """
        return self._component
