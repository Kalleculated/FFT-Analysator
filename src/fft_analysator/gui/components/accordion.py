import panel as pn

from fft_analysator.gui.components.file_input_tkinter import FileInputComponent
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
from fft_analysator.gui.components.exporter_selector import ExporterSelector
from fft_analysator.gui.components.toggle_group import ToggleGroup
from fft_analysator.gui.components.toggle_y_axis import ToggleYAxis
from fft_analysator.gui.components.toggle_x_axis import ToggleXAxis


class Accordion:
    """A class representing an accordion component.

    The Accordion class is used to create an accordion component with various sub-components such as file input, color pickers, switches, menus, and sliders.

    Attributes:
        file_input (FileInputComponent): The file input component.
        color_picker_ch1 (Colorpicker): The color picker for channel 1.
        color_picker_ch2 (Colorpicker): The color picker for channel 2.
        color_picker_result (Colorpicker): The color picker for the result.
        method_selector (MethodSelector): The selector for methods.
        selector (Selector): The selector component.
        data_selector (DataSelector): The data selector component.
        int_slider (IntSlider): The integer slider component.
        gen_nav (GeneratorNavigator): The generator navigator component.
        blocksize_selector (BlocksizeSelector): The blocksize selector component.
        channel_selector_input (ChannelSelector): The channel selector for input.
        channel_selector_output (ChannelSelector): The channel selector for output.
        window_selector (WindowSelector): The selector for the windows.
        overlap_selector (OverlapSelector): The selector for the overlaps.
        exporter_selector (ExporterSelector): The selector for the exporters.
        file_exporter (FileExporter): The file exporter component.
        toggle_group (ToggleGroup): The toggle group component.
        toggle_y_axis (ToggleYAxis): The toggle for the y-axis.
        toggle_x_axis (ToggleXAxis): The toggle for the x-axis.
        accordion (pn.Accordion): The accordion component.

    """

    def __init__(self):
        self.file_input = FileInputComponent()
        self.color_picker_ch1 = Colorpicker()
        self.color_picker_ch2 = Colorpicker()
        self.color_picker_result = Colorpicker()
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
        self.exporter_selector = ExporterSelector()
        self.toggle_group = ToggleGroup()
        self.toggle_x_axis = ToggleXAxis()
        self.toggle_y_axis = ToggleYAxis()
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
                                                            self.toggle_group.component,
                                                            pn.Row(self.toggle_x_axis.component, self.toggle_y_axis.component)
                                                            )),
                                            ('Calculation', pn.Column(pn.Row(self.window_selector.component,
                                                                            self.overlap_selector.component),
                                                                            self.method_selector.component)
                                             ),
                                            ('Export', pn.Column(self.exporter_selector.component,self.file_exporter.component)),
                                            sizing_mode='stretch_width')

    @property
    def component(self):
        """Get the accordion component.

        Returns:
            _component (object):
                The stored widget.
        """
        return self._component
