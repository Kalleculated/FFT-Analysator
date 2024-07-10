import panel as pn


class Switch:
    """
    A class used to represent a Switch widget.

    This class encapsulates a panel Switch widget and provides an interface for interacting with it.

    Attributes
    ----------
    switch : object
        An instance of the panel Switch widget.
    _component : object
        The panel Switch widget with specific parameters.

    Methods
    -------
    component()
        Gets the stored widget.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the Switch object.

        The switch attribute is initialized as a panel Switch widget.
        The _component attribute is initialized as a panel Switch widget with specific parameters.
        """
        self.switch = pn.widgets.Switch
        self._component = self.switch(name='Stretch Plot', width=30, margin=(0, 165), height=30, disabled=True)

    @property
    def component(self):
        """
        Gets the stored widget.

        This method returns the panel Switch widget stored in the _component attribute.

        Returns
        -------
        object
            The stored widget.
        """
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component
