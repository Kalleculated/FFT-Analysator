import panel as pn


class ExporterSelector:
    """
    A class used to select the export format.

    Attributes:
        export_selector (pn.widgets.Select):
            An instance of the Panel Select widget.
        options (list):
            A list of available export formats.
        _component (pn.widgets.Select):
            The Panel Select widget with specific parameters.
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the ExporterSelector object.

        Attributes:
            export_selector (pn.widgets.Select):
                An instance of the Panel Select widget.
            options (list):
                A list of available export formats.
            _component (pn.widgets.Select):
                The Panel Select widget with specific parameters.
        """
        self.export_selector = pn.widgets.Select
        self.options = ['Numpy Array', 'Binary']
        self._component = self.export_selector(name='Choose export extension:', options=self.options, width=300,
                                               value='Numpy Array', disabled=True)
    @property
    def component(self):
        """
        Gets the stored widget.

        Returns:
            _component (object):
                The stored widget.
        """
        return self._component
