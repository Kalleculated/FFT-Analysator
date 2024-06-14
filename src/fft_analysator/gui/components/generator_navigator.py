import panel as pn


class GeneratorNavigator:
    def __init__(self, int_slider_callback):
        self.button_back = pn.widgets.Button(name='\u25c0', button_type='default', margin=(2, 5, 5, 5), disabled=True)
        self.button_forward = pn.widgets.Button(name='\u25b6', button_type='default', margin=(2, 5, 5, 5), disabled=True)
        self.reset_button = pn.widgets.Button(name='\u21ba', button_type='default', margin=(2, 5, 5, 5), disabled=True)
        self.index_box = pn.widgets.IntInput(name='Block index:', value=0, margin=(-20, 20, 0, 10), disabled=True, width=80)
        self.goto_button = pn.widgets.Button(name='Go', button_type='default', margin=(2, 5, 5, 5), disabled=True)
        self._component = pn.Row(self.goto_button, self.index_box, self.button_back, self.reset_button, self.button_forward,
                                 margin=(5, 5, 10, 5))

        self.int_slider_callback = int_slider_callback

        pn.bind(self.int_slider_next, self.button_forward, watch=True)
        pn.bind(self.int_slider_previous, self.button_back, watch=True)
        pn.bind(self.int_slider_reset, self.reset_button, watch=True)
        pn.bind(self.int_slider_goto, self.goto_button, watch=True)

    def int_slider_next(self, event):
        if (self.int_slider_callback.component.value < self.int_slider_callback.component.end):
            self.int_slider_callback.component.value += 1

    def int_slider_previous(self, event):
        if (self.int_slider_callback.component.value > self.int_slider_callback.component.start):
            self.int_slider_callback.component.value -= 1

    def int_slider_reset(self, event):
        if self.int_slider_callback:
            self.int_slider_callback.component.value = 0

    def int_slider_goto(self, event):
        if (self.index_box.value <= self.int_slider_callback.component.end
            and self.index_box.value >= self.int_slider_callback.component.start):
            self.int_slider_callback.component.value = self.index_box.value

    @property
    def component(self):
        return self._component
