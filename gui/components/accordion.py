import panel as pn

class Accordion:
    def __init__(self, file_input, multi_choice, stretching_switch):
        self.file_input = file_input
        self.multi_choice = multi_choice
        self.stretching_switch = stretching_switch
        self.accordion = pn.Accordion
        self._component = self.accordion(('Upload', self.file_input.component),
                                          ('Plot', pn.Column(self.multi_choice._component, pn.Row(pn.widgets.StaticText(name='Stretch plot', value=''), self.stretching_switch._component))), 
                                          sizing_mode='stretch_width')

    @property
    def component(self):
        return self._component