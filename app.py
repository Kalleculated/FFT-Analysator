from gui.controllers.app_controller import AppController

class App:
    def __init__(self):
        self.app = AppController()
    
    def run(self):
        self.app.servable()

app = App().run()