import panel as pn

class OverlapSelector:
    """
    A class used to represent an Overlap Selector widget.

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
        Constructs all the necessary attributes for the OverlapSelector object.

        The selector attribute is initialized as a panel Select widget.
        The options attribute is initialized with a list of overlap options.
        The _component attribute is initialized as a panel Select widget with specific parameters.
        """
        self.selector = pn.widgets.Select
        self.options = ['None', '50%', '75%', '87.5%']
        self._component = self.selector(name='Choose overlap:', options=self.options, width=140, value='50%',
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
