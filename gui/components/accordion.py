import panel as pn

from gui.components.file_input import FileInputComponent
from gui.components.multi_choice import MultiChoice
from gui.components.switch import Switch


class Accordion:
    def __init__(self):
        self.file_input = FileInputComponent()
        self.multi_choice = MultiChoice()
        self.stretching_switch = Switch()
        self.accordion = pn.Accordion
        self._component = self.accordion(('Upload', self.file_input.component),
                                          ('Plot', pn.Column(self.multi_choice._component,
                                                              pn.layout.Divider(margin=(5, 0, 5, 0)),
                                                              pn.Row(pn.widgets.StaticText(name='Stretch plot', value=''),  # noqa: E501
                                                                     self.stretching_switch._component))),
                                          sizing_mode='stretch_width')

    @property
    def component(self):
        return self._component
