import panel as pn


class DataSelector:
    """
    A class used to represent a Data Selector widget.

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
        Constructs all the necessary attributes for the DataSelector object.

        The selector attribute is initialized as a panel Select widget.
        The options attribute is initialized as an empty list.
        The _component attribute is initialized as a panel Select widget with specific parameters.
        """
        self.selector = pn.widgets.Select
        self.options = []
        self._component = self.selector(name='', options=self.options, size=len(self.options)+2,
                                        margin=(20, 0, 0, 20), height=30, width=200)

    @property
    def component(self):
        """
        Gets the stored widget.

        Returns:
            _component (object):
                The stored widget.
        """
        return self._component
