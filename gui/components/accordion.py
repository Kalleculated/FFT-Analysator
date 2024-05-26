import panel as pn
from gui.components.file_input import FileInputComponent
from gui.components.multi_choice import MultiChoice

class Accordion:
    def __init__(self, file_input, multi_choice):
        self.file_input = file_input
        self.multi_choice = multi_choice
        self.accordion = pn.Accordion
        self._component = self.accordion(('Upload', self.file_input.component),
                                          ('Plot', self.multi_choice._component), 
                                          sizing_mode='stretch_width')

    @property
    def component(self):
        # Der Getter gibt das gespeicherte Widget zurück
        return self._component