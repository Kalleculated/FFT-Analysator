import panel as pn
from gui.components.file_input import FileInputComponent
import analysis.signal_processing as sp

class MainView:
    def __init__(self):
        pn.extension(sizing_mode="stretch_width", template="fast", theme="dark")
        self.file_input = FileInputComponent()
        self.file_input.component.param.watch(self.update_main, 'value')

        # Erstelle den Seitenbereich mit dem Datei-Input-Widget
        self.sidebar = pn.Column(
            self.file_input.component,
            sizing_mode='stretch_width'
        )

        self.main = pn.Column("Willkommen beim FFT-Analysators", sizing_mode='stretch_width')

        # Setze einige zusätzliche Design- und Template-Parameter
        pn.state.template.param.update(
            site="FFT-Analysator",
            title="",
            header_background="#E91E63",
            accent_base_color="#E91E63",
        )

        self.update_main()

    def update_main(self, event=None):
        # Überprüfen, ob Dateidaten vorhanden sind
        if self.file_input.component.value:
            file_data = self.file_input.component.value
            num_channels = sp.count_channels(file_data)
            self.main.objects = [  # Korrektur hier
                "Willkommen beim FFT-Analysators",
                f"Anzahl der Kanäle: {num_channels}"
            ]

    def servable(self):
        # Markiere nur die Haupt- und Seitenbereiche als servable
        self.sidebar.servable(target="sidebar")
        self.main.servable(target="main")

if __name__ == "__main__":
    main_view = MainView()
    main_view.servable()
