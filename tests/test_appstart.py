from fft_analysator.app import App


def test_app_initialization():
    """Testet, ob die AppController-Instanz korrekt initialisiert und servable gemacht werden kann."""
    App().run()
    # pytest nimmt standardmäßig an, dass der Test erfolgreich ist, wenn keine Exceptions auftreten.
