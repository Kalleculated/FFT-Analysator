import panel as pn


class Tabs:
    """
    A class used to represent a Tabs widget.

    This class encapsulates a panel Tabs widget and provides an interface for interacting with it.

    Attributes:
        tabs (object):
            An instance of the panel Tabs widget.
        str_signal_tab (str):
            The title of the signal tab.
        str_frequency_response_tab (str):
            The title of the frequency response tab.
        str_impulse_response_tab (str):
            The title of the impulse response tab.
        str_analysis_function_tab (str):
            The title of the analysis function tab.
        _component (object):
            The panel Tabs widget with specific parameters.

    Methods:
        component():
            Gets the stored widget.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the Tabs object.

        The tabs attribute is initialized as a panel Tabs widget.
        The str_signal_tab, str_frequency_response_tab, str_impulse_response_tab, and str_analysis_function_tab attributes are initialized with specific string values.
        The _component attribute is initialized as a panel Tabs widget with specific parameters.
        """
        self.tabs = pn.Tabs
        self.str_signal_tab = "Input/Output"
        self.str_frequency_response_tab = "Frequency Response"
        self.str_impulse_response_tab = "Impulse Response"
        self.str_analysis_function_tab = "Analysis Functions"
        self._component = self.tabs(
            (self.str_signal_tab, 'No data chosen!'),
            (self.str_frequency_response_tab, 'No data chosen!'),
            (self.str_impulse_response_tab, 'No data chosen!'),
            (self.str_analysis_function_tab, 'No data chosen!'),
            sizing_mode='stretch_width', dynamic=True)

    @property
    def component(self):
        """
        Gets the stored widget.

        This method returns the panel Tabs widget stored in the _component attribute.

        Returns:
            _component (object):
                The stored widget.
        """
        return self._component
