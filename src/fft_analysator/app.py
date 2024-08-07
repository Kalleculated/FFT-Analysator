import panel as pn

from fft_analysator.gui.controllers.app_controller import AppController


class App:
    """
    A class used to represent the main application.

    This class is responsible for initializing and running the application.

    Attributes:
        app (AppController):
            An instance of the AppController class.

    Methods:
    run():
        Makes the application servable.
    serve_app():
        Serves the application on a specific port and opens it in a web browser.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the App object.

        The app attribute is initialized as an AppController instance.
        """
        self.app = AppController()

    def run(self):
        """
        Makes the application servable.

        This method calls the servable method of the app attribute, which makes the application ready to be served.

        Returns:
            None
        """
        self.app.servable()

    def serve_app(self):
        """
        Serves the application on a specific port and opens it in a web browser.

        This method calls the serve method of the app attribute, which starts a server and opens the application in a web browser.

        Returns:
            None
        """
        pn.serve(self.app.template_layout, port=5000, show=True)


app = App().run()
