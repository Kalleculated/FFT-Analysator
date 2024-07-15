import panel as pn


class BlocksizeSelector:
    """
    A class representing a block size selector.

    Attributes:
        blocksize_selector (pn.widgets.Select): The block size selector widget.
        sizes (list): A list of available block sizes.
        _component (pn.widgets.Select): The internal block size selector component.

    """

    def __init__(self):
        """
        The block size selector is initialized as a panel Select widget with specific parameters.
        """
        self.blocksize_selector = pn.widgets.Select
        self.sizes = [128, 256, 512, 1024, 2048,4096, 8192, 16384, 32768, 65536]
        self._component = self.blocksize_selector(name='Select Blocksize', options=self.sizes, value=1024)

    @property
    def component(self):
        """
        Get the block size selector component.

        Returns:
            _component (object):
                The stored widget.

        """
        return self._component
