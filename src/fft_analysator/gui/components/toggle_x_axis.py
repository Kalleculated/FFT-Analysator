import panel as pn


class ToggleXAxis:
    """
    A class used to represent a ToggleGroup widget.

    This class encapsulates a panel ToggleGroup widget and provides an interface for populating it with options and retrieving the selected option.

    Attributes
    ----------
    selector : object
        An instance of the panel ToggleGroup widget.
    options : list
        A list of options for the ToggleGroup widget. Initially empty.
    _component : object
        The panel Select widget with specific parameters.

    Methods:
        component():
            Gets the stored widget.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the ToggleGroup object.

        The toggle_group attribute is initialized as a panel ToggleGroup widget.
        The options attribute is initialized as an empty list.
        The _component attribute is initialized as a panel ToggleGroup widget with specific parameters.
        """
        self.x_log = False
        self.toggle_group = pn.widgets.ToggleGroup
        self.options = ['x-linear', 'x-log']
        self._component = self.toggle_group(name='Choose table:', options=self.options, width=140, disabled=True,
                                            behavior="radio", value='x-linear')

    @property
    def component(self):
        """
        Gets the stored widget.

        This method returns the panel ToggleGroup widget stored in the _component attribute.

        Returns:
            _component (object):
                The stored widget.
        """
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component
