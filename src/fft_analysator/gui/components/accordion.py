import panel as pn

from fft_analysator.gui.components.file_input_tkinter import FileInputComponent
from fft_analysator.gui.components.switch import Switch
from fft_analysator.gui.components.color_picker import Colorpicker
from fft_analysator.gui.components.method_selector import MethodSelector
from fft_analysator.gui.components.selector import Selector
from fft_analysator.gui.components.data_selector import DataSelector
from fft_analysator.gui.components.int_slider import IntSlider
from fft_analysator.gui.components.generator_navigator import GeneratorNavigator
from fft_analysator.gui.components.blocksize_selector import BlocksizeSelector
from fft_analysator.gui.components.channel_selector import ChannelSelector
from fft_analysator.gui.components.window_selector import WindowSelector
from fft_analysator.gui.components.overlap_selector import OverlapSelector
from fft_analysator.gui.components.exporter import FileExporter
from fft_analysator.gui.components.exporter_menu import Exporter


class Accordion:
    """A class representing an accordion component.

    The Accordion class is used to create an accordion component with various sub-components such as file input, color pickers, switches, menus, and sliders.

    Attributes:
        file_input (FileInputComponent): The file input component.
        color_picker_ch1 (Colorpicker): The color picker for channel 1.
        color_picker_ch2 (Colorpicker): The color picker for channel 2.
        color_picker_result (Colorpicker): The color picker for the result.
        stretching_switch (Switch): The switch for stretching.
        calculation_selector (CalculationSelector): The selector for calculations.
        selector (Selector): The selector component.
        data_selector (DataSelector): The data selector component.
        int_slider (IntSlider): The integer slider component.
        gen_nav (GeneratorNavigator): The generator navigator component.
        blocksize_selector (BlocksizeSelector): The blocksize selector component.
        channel_selector_input (ChannelSelector): The channel selector for input.
        channel_selector_output (ChannelSelector): The channel selector for output.
        window_selector (WindowSelector): The selector for the windows.
        overlap_selectgor (OverlapSelector): The selector for the overlaps.
        accordion (pn.Accordion): The accordion component.

    """

    def __init__(self):
        self.file_input = FileInputComponent()
        self.color_picker_ch1 = Colorpicker()
        self.color_picker_ch2 = Colorpicker()
        self.color_picker_result = Colorpicker()
        self.stretching_switch = Switch()
        self.method_selector = MethodSelector()
        self.selector = Selector()
        self.data_selector = DataSelector()
        self.int_slider= IntSlider()
        self.gen_nav = GeneratorNavigator(self.int_slider)
        self.gen_nav = GeneratorNavigator(self.int_slider)
        self.blocksize_selector = BlocksizeSelector()
        self.channel_selector_input = ChannelSelector()
        self.channel_selector_output = ChannelSelector()
        self.window_selector = WindowSelector()
        self.overlap_selector = OverlapSelector()
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

        self._component = self.accordion(('Upload', pn.Column(pn.Row(self.file_input.component, self.data_selector.component), self.selector.component, self.blocksize_selector.component)),
                                          ('Plot', pn.Column(pn.Row(self.channel_selector_input.component, self.channel_selector_output.component),
                                                            pn.Row(self.color_picker_ch1.component,self.color_picker_ch2.component,self.color_picker_result.component),
                                                            pn.layout.Divider(margin=(5, 0, 5, 0)),
                                                            #self.int_slider.component,
                                                            self.gen_nav.component,
                                                            pn.Row(pn.widgets.StaticText(name='Stretch plot', value='', margin=(0, 15)),  # noqa: E501
                                                                     self.stretching_switch.component))),

                                            ('Calculation', pn.Column(pn.Row(self.window_selector.component,
                                                                            self.overlap_selector.component),
                                                                            self.method_selector.component)
                                             ),
                                            ('Export', pn.Column(self.exporter_menu.component,self.file_exporter.component)),
                                            sizing_mode='stretch_width')

    @property
    def component(self):
        """Get the accordion component.

        Returns:
            pn.Accordion: The accordion component.
        """
        return self._component
