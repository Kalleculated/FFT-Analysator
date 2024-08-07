import panel as pn


class Selector:
    """
    A class used to represent a Selector widget.

    This class encapsulates a panel Select widget and provides an interface for populating it with options and retrieving the selected option.

    Attributes:
        selector (object):
            An instance of the panel Select widget.
        options (list):
            A list of options for the selector widget. Initially empty.
        _component (object):
            The panel Select widget with specific parameters.

    Methods:
        component():
            Gets the stored widget.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the Selector object.

        The selector attribute is initialized as a panel Select widget.
        The options attribute is initialized as an empty list.
        The _component attribute is initialized as a panel Select widget with specific parameters.
        """
        self.selector = pn.widgets.Select
        self.options = []
        self._component = self.selector(name='Choose table:', options=self.options, size=len(self.options)+2)

    @property
    def component(self):
        """
        Gets the stored widget.

        This method returns the panel Select widget stored in the _component attribute.

        Returns:
            _component (object):
                The stored widget.
        """
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component
