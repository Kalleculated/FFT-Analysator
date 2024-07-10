import panel as pn


class MethodSelector:
    """
    A class used to represent a Method Selector widget.

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
        Constructs all the necessary attributes for the MethodSelector object.

        The selector attribute is initialized as a panel Select widget.
        The options attribute is initialized with a list of analysis methods.
        The _component attribute is initialized as a panel Select widget with specific parameters.
        """
        self.selector = pn.widgets.Select
        self.options = ["No Analysis Function", "Auto Spectral Density - Input", "Auto Spectral Density - Output",
                        "Cross Spectral Density", "Coherence","Auto Correlation - Input", "Auto Correlation - Output",
                        "Cross Correlation"]
        self._component = self.selector(name='Choose analysis method:', options=self.options, width=300, value='No Analysis Function',
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
