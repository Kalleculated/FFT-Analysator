import panel as pn
from gui.components.file_input import FileInputComponent

class MainView:
    def __init__(self):
        pn.extension(sizing_mode="stretch_width", template="fast", theme="dark")
        self.file_input = FileInputComponent()

        # Erstelle den Seitenbereich mit dem Datei-Input-Widget
        self.sidebar = pn.Column(
            self.file_input.component,
            sizing_mode='stretch_width'
        )

        # Erstelle den Hauptbereich mit einem einfachen Willkommenstext
        self.main = pn.Column(
            "Willkommen beim FFT-Analysator",
            sizing_mode='stretch_width'
        )

        # Setze einige zusätzliche Design- und Template-Parameter
        pn.state.template.param.update(
            site="FFT-Analysator",
            title="FFT-Analysator",
            header_background="#E91E63",
            accent_base_color="#E91E63",
        )

    def servable(self):
        # Markiere nur die Haupt- und Seitenbereiche als servable
        self.sidebar.servable(target="sidebar")
        self.main.servable(target="main")

if __name__ == "__main__":
    main_view = MainView()
    main_view.servable()
