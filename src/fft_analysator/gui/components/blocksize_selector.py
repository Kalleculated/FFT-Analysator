import panel as pn


class BlocksizeSelector:
    def __init__(self):
        self.blocksize_selector = pn.widgets.Select
        self.sizes = [128, 256, 512, 1024, 2048, 8192, 16384, 32768, 65536]
        self._component = self.blocksize_selector(name='Select Blocksize', options=self.sizes, value=1024)

    @property
    def component(self):
        return self._component
