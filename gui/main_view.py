import panel as pn
from gui.components.file_input import FileInputComponent
import analysis.signal_processing as sp
import matplotlib.pyplot as plt
import gui.components.upload_button as ub
import gui.components.file_input as fi

class MainView:
    def __init__(self):
        pn.extension(sizing_mode="stretch_width", template="fast", theme="dark")
        self.file_input = fi.FileInputComponent()
        self.file_input.component.param.watch(self.update_main, 'value')

        # Erstelle den Seitenbereich mit dem Datei-Input-Widget
        self.sidebar = pn.Column(
            self.file_input.component,
            sizing_mode='stretch_width'
        )

        self.main = pn.Column("Dashboard", sizing_mode='stretch_width')

        # Setze einige zusätzliche Design- und Template-Parameter
        pn.state.template.param.update(
            site="FFT-Analysator",
            title="",
            header_background="#E91E63",
            accent_base_color="#E91E63",
        )

        self.update_main()

    def update_main(self, event=None):
        if self.file_input.component.value:
            file_data = self.file_input.component.value
            data = sp.count_channels(file_data)
            self.main.objects = [
                pn.pane.Markdown("Willkommen beim FFT-Analysator"),
                pn.pane.Markdown(f"Anzahl der Kanäle: {data.shape}")
            ]
        else:
            self.main.objects = [pn.pane.Markdown("Dashboard")]

    def servable(self):
        # Markiere nur die Haupt- und Seitenbereiche als servable
        self.sidebar.servable(target="sidebar")
        self.main.servable(target="main")