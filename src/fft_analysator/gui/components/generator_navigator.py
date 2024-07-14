import panel as pn


class GeneratorNavigator:
    """
    A class used to represent a Generator Navigator.

    Attributes:
        button_back (object):
            An instance of the panel Button widget for navigating backwards.
        button_forward (object):
            An instance of the panel Button widget for navigating forwards.
        reset_button (object):
            An instance of the panel Button widget for resetting.
        index_box (object):
            An instance of the panel IntInput widget for inputting index.
        goto_button (object):
            An instance of the panel Button widget for going to a specific index.
        _component (object):
            The panel Row widget with specific parameters.
        int_slider_callback (object):
            The callback function for the integer slider.

    Methods:
        int_slider_next(event):
            Increments the value of the integer slider.
        int_slider_previous(event):
            Decrements the value of the integer slider.
        int_slider_reset(event):
            Resets the value of the integer slider.
        int_slider_goto(event):
            Sets the value of the integer slider to the value of the index box.
        component():
            Gets the stored widget.
    """

    def __init__(self, int_slider_callback):
        """
        Constructs all the necessary attributes for the GeneratorNavigator object.

        The button_back, button_forward, reset_button, index_box, and goto_button attributes are initialized as panel Button widgets.
        The _component attribute is initialized as a panel Row widget with specific parameters.
        The int_slider_callback attribute is set to the provided callback function.
        """
        self.button_back = pn.widgets.Button(name='\u25c0', button_type='default', margin=(10, 5, 5, 5), disabled=True)
        self.button_forward = pn.widgets.Button(name='\u25b6', button_type='default', margin=(10, 5, 5, 5), disabled=True)
        self.reset_button = pn.widgets.Button(name='\u21ba', button_type='default', margin=(10, 5, 5, 5), disabled=True)
        self.index_box = pn.widgets.IntInput(name='Index:', value=0, margin=(-10, 20, 0, 10), disabled=True, width=80)
        self.goto_button = pn.widgets.Button(name='Go', button_type='default', margin=(10, 5, 5, 5), disabled=True)
        self._component = pn.Row(self.goto_button, self.index_box, self.button_back, self.reset_button, self.button_forward,
                                 margin=(5, 5, 10, 5))

        self.int_slider_callback = int_slider_callback

        pn.bind(self.int_slider_next, self.button_forward, watch=True)
        pn.bind(self.int_slider_previous, self.button_back, watch=True)
        pn.bind(self.int_slider_reset, self.reset_button, watch=True)
        pn.bind(self.int_slider_goto, self.goto_button, watch=True)

    def int_slider_next(self, event):
        """
        Increments the value of the integer slider.

        Args:
            event (object): The event object passed by the panel Button widget.
        """
        if (self.int_slider_callback.component.value < self.int_slider_callback.component.end):
            self.int_slider_callback.component.value += 1

    def int_slider_previous(self, event):
        """
        Decrements the value of the integer slider.

        Args:
            event (object): The event object passed by the panel Button widget.
        """
        if (self.int_slider_callback.component.value > self.int_slider_callback.component.start):
            self.int_slider_callback.component.value -= 1

    def int_slider_reset(self, event):
        """
        Resets the value of the integer slider.

        Args:
            event (object): The event object passed by the panel Button widget.
        """
        if self.int_slider_callback:
            self.int_slider_callback.component.value = 0

    def int_slider_goto(self, event):
        """
        Sets the value of the integer slider to the value of the index box.

        Args:
            event (object): The event object passed by the panel Button widget.
        """
        if (self.index_box.value <= self.int_slider_callback.component.end
            and self.index_box.value >= self.int_slider_callback.component.start):
            self.int_slider_callback.component.value = self.index_box.value

    @property
    def component(self):
        """
        Gets the stored widget.

        Returns:
            _component (object):
                The stored widget.
        """
        return self._component
