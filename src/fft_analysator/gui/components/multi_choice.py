import panel as pn


class MultiChoice:
    def __init__(self):
        self.multi_select = pn.widgets.MultiChoice
        self._component = self.multi_select(name='No data chosen!', value=[],
                        options=[], margin=(10, 15))

    @property
    def component(self):
        return self._component
