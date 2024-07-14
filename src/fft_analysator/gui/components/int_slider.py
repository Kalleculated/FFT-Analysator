import panel as pn


class IntSlider:
    """
    A helper class used to represent a helper Integer Slider widget to store the logic for the
    generator navigation buttons.

    Attributes:
        int_slider (object):
            An instance of the panel IntSlider widget.
        _component (object):
            The panel IntSlider widget with specific parameters.

    Methods:
        component():
            Gets the stored widget.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the IntSlider object.

        The int_slider attribute is initialized as a panel IntSlider widget.
        The _component attribute is initialized as a panel IntSlider widget with specific parameters.
        """
        self.int_slider = pn.widgets.IntSlider
        self._component = self.int_slider(name='Current Block', start=0, step=1, margin=(15, 20, 25, 20),
        sizing_mode='stretch_width', disabled=True, align='start')

    @property
    def component(self):
        """
        Gets the stored widget.

        Returns:
            _component (object):
                The stored widget.
        """
        return self._component
