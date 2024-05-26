import panel as pn

class MainView:
    def __init__(self):
        self.main = pn.Column("", sizing_mode='stretch_width')

    def servable(self):
        self.main.servable(target="main")