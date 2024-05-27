from gui.controllers.app_controller import AppController

def test_app_initialization():
    """Testet, ob die AppController-Instanz korrekt initialisiert und servable gemacht werden kann."""
    app = AppController()
    app.servable()
    # pytest nimmt standardmäßig an, dass der Test erfolgreich ist, wenn keine Exceptions auftreten.
