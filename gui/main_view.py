import panel as pn
from gui.components.file_input import FileInputComponent
import analysis.signal_processing as sp
import matplotlib.pyplot as plt
import gui.components.upload_button as ub
import gui.components.file_input as fi
import holoviews as hv
import panel as pn
import numpy as np

hv.extension("bokeh", "plotly")


class MainView:
    def __init__(self):
        pn.extension(sizing_mode="stretch_width", template="fast", theme="dark")
        pn.extension("plotly")
        pn.extension('floatpanel')
        self.file_input = fi.FileInputComponent()
        self.sidebar_upload = pn.Column(self.file_input.component, sizing_mode='stretch_width')
        self.file_input.component.param.watch(self.update_main, 'value')
        self.file_input.component.param.watch(self.update_side, 'value')
        self.accordion = pn.Accordion(('Upload', self.file_input.component),('Autokorrelation', "test"), sizing_mode='stretch_width')
        self.tabs = pn.Tabs(('Signalinput', ''),('Ergebnis', "test"), sizing_mode='stretch_width', dynamic=True)

        # Create a sidebar and main area
        self.sidebar = pn.Column(
            "", sizing_mode='stretch_width'
        )

        self.main = pn.Column("", sizing_mode='stretch_width')

        # Set some template parameters
        pn.state.template.param.update(
            site="FFT-Analysator",
            title="",
            header_background="#E91E63",
            accent_base_color="#E91E63",
        )

        # Update the main area
        self.update_main()

        # Update the sidebar area
        self.update_side()

    def update_main(self, event=None):
        if self.file_input.component.value:
            file_data = self.file_input.component.value
            data = sp.count_channels(file_data)

            # Create a holoviews plot with data and divide kdmis by amound of channels
            fig = hv.Curve((np.linspace(0,1,51200), data[:,1]), kdims="Zeit in Sekunden", vdims="Amplitude").opts(
                height=400
            )

            self.main.objects = [
                self.tabs
            ]
        else:
            self.main.objects = [
                self.tabs
            ]

    def update_side(self, event=None):
        if self.file_input.component.value:
            file_data = self.file_input.component.value
            data = sp.count_channels(file_data)

            self.sidebar.objects = [
                self.accordion,
                pn.pane.Markdown(f"Fileshape: {data.shape}")
            ]
        else:
            self.sidebar.objects = [
                self.accordion
            ]

    def servable(self):
        # Mark main and sidebar as servable
        self.sidebar.servable(target="sidebar")
        self.main.servable(target="main")