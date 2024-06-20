import panel as pn

from fft_analysator.gui.components.file_input_tkinter import FileInputComponent
from fft_analysator.gui.components.multi_choice import MultiChoice
from fft_analysator.gui.components.switch import Switch
from fft_analysator.gui.components.color_picker import Colorpicker
from fft_analysator.gui.components.calculation_menu import MenuButton
from fft_analysator.gui.components.selector import Selector
from fft_analysator.gui.components.data_selector import DataSelector
from fft_analysator.gui.components.int_slider import IntSlider
from fft_analysator.gui.components.generator_navigator import GeneratorNavigator
from fft_analysator.gui.components.blocksize_selector import BlocksizeSelector


class Accordion:
    def __init__(self):
        self.file_input = FileInputComponent()
        self.multi_choice = MultiChoice()
        self.color_picker_ch1 = Colorpicker()
        self.color_picker_ch2 = Colorpicker()
        self.stretching_switch = Switch()
        self.calculation_menu = MenuButton()
        self.selector = Selector()
        self.data_selector = DataSelector()
        self.int_slider= IntSlider()
        self.gen_nav = GeneratorNavigator(self.int_slider)
        self.blocksize_selector = BlocksizeSelector()
        self.accordion = pn.Accordion

        # Initially hide the color picker
        self.color_picker_ch1.component.visible = False
        self.color_picker_ch2.component.visible = False

        self._component = self.accordion(('Upload', pn.Column(pn.Row(self.file_input.component, self.data_selector.component), self.selector.component, self.blocksize_selector.component)),
                                          ('Plot', pn.Column(self.multi_choice.component, pn.Row(self.color_picker_ch1.component,self.color_picker_ch2.component),
                                                              pn.layout.Divider(margin=(5, 0, 5, 0)),
                                                              self.int_slider.component,
                                                              self.gen_nav.component,
                                                              pn.Row(pn.widgets.StaticText(name='Stretch plot', value='', margin=(0,15)),  # noqa: E501
                                                                     self.stretching_switch.component))),
                                            ('Calculation', self.calculation_menu.component),
                                          sizing_mode='stretch_width')


    @property
    def component(self):
        return self._component
