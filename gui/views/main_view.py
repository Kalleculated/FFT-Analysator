import panel as pn

class MainView:
    def __init__(self):
        self.tabs = pn.Tabs(('Signalinput',"test"),('Ergebnis', "test"), sizing_mode='stretch_width', dynamic=True)

        self.main = pn.Column(self.tabs, sizing_mode='stretch_width')

    def servable(self):
        self.main.servable(target="main")