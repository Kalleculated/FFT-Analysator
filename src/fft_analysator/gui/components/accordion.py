import panel as pn

from fft_analysator.gui.components.file_input_tkinter import FileInputComponent
from fft_analysator.gui.components.switch import Switch
from fft_analysator.gui.components.color_picker import Colorpicker
from fft_analysator.gui.components.calculation_menu import MenuButton
from fft_analysator.gui.components.selector import Selector
from fft_analysator.gui.components.data_selector import DataSelector
from fft_analysator.gui.components.int_slider import IntSlider
from fft_analysator.gui.components.generator_navigator import GeneratorNavigator
from fft_analysator.gui.components.blocksize_selector import BlocksizeSelector
from fft_analysator.gui.components.channel_selector import ChannelSelector
from fft_analysator.gui.components.window_menu import Window_MenuButton
from fft_analysator.gui.components.overlap_menu import Overlap_MenuButton
from fft_analysator.gui.components.exporter import FileExporter
from fft_analysator.gui.components.exporter_menu import Exporter_MenuButton


class Accordion:
    def __init__(self):
        self.file_input = FileInputComponent()
        self.color_picker_ch1 = Colorpicker()
        self.color_picker_ch2 = Colorpicker()
        self.color_picker_result = Colorpicker()
        self.stretching_switch = Switch()
        self.calculation_menu = MenuButton()
        self.selector = Selector()
        self.data_selector = DataSelector()
        self.int_slider= IntSlider()
        self.gen_nav = GeneratorNavigator(self.int_slider)
        self.gen_nav = GeneratorNavigator(self.int_slider)
        self.blocksize_selector = BlocksizeSelector()
        self.channel_selector_input = ChannelSelector()
        self.channel_selector_output = ChannelSelector()
        self.window_menu = Window_MenuButton()
        self.overlap_menu = Overlap_MenuButton()
        self.file_exporter = FileExporter()
        self.exporter_menu = Exporter_MenuButton()
        self.accordion = pn.Accordion

        # Set default colors
        self.color_picker_ch1.component.value = '#D23232' # Red for channel 1
        self.color_picker_ch2.component.value = '#1D1DB9'  # Blue for channel 2
        self.color_picker_result.component.value = '#CB8710'  # Green for result

        # Initially hide the color picker
        self.color_picker_ch1.component.visible = False
        self.color_picker_ch2.component.visible = False
        self.color_picker_result.component.visible = False

        # Set default window
        self.window_menu.window_menu.clicked = 'Hanning'

        # Set default overlap
        self.overlap_menu.overlap_menu.clicked = '50%'

        self._component = self.accordion(('Upload', pn.Column(pn.Row(self.file_input.component, self.data_selector.component), self.selector.component, self.blocksize_selector.component)),
                                          ('Plot', pn.Column(pn.Row(self.channel_selector_input.component, self.channel_selector_output.component),
                                                            pn.Row(self.color_picker_ch1.component,self.color_picker_ch2.component,self.color_picker_result.component),
                                                            pn.layout.Divider(margin=(5, 0, 5, 0)),
                                                            #self.int_slider.component,
                                                            self.gen_nav.component,
                                                            pn.Row(pn.widgets.StaticText(name='Stretch plot', value='', margin=(0, 15)),  # noqa: E501
                                                                     self.stretching_switch.component))),

                                            ('Calculation', pn.Column(pn.Row(self.window_menu.component,
                                                            self.overlap_menu.component),self.calculation_menu.component)),
                                            ('Export', pn.Column(self.exporter_menu.component,self.file_exporter.component)),
                                            sizing_mode='stretch_width')

    @property
    def component(self):
        return self._component
