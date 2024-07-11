import panel as pn


class Colorpicker:
    """
    A class used to represent a Color Picker widget.

    Attributes
    ----------
    color_picker : object
        An instance of the panel ColorPicker widget.
    _component : object
        The panel ColorPicker widget with specific parameters.

    """

    def __init__(self):
        """
        The color picker is initialized as a panel ColorPicker widget with specific parameters.
        """
        self.color_picker = pn.widgets.ColorPicker
        self._component = self.color_picker(name='', value='#FF0000', margin=(10, 30), visible=False)

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
