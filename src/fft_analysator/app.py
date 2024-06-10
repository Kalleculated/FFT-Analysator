import panel as pn

from src.fft_analysator.gui.controllers.app_controller import AppController


class App:
    def __init__(self):
        self.app = AppController()

    def run(self):
        self.app.servable()

    def serve_app(self):
        pn.serve(self.app.template_layout, port=5000, show=True)


app = App().run()
