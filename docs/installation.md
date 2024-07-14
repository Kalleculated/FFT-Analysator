# Installation

There are two different ways to install the FFT-Analyzer:

1. Download the source code, install the packages from the `requirement.txt` by navigating to the root directory and using the command `pip install -r requirements.txt`, afterwards to start the app use `panel serve src\fft_analysator\app.py --autoreload` and navigate to the url given to you inside of the console in the browser of your choice.
2. Alternatively, you can download the source code and install the package by navigating to the root and using the command `pip install .` or `pip install setup.py`. Afterwards you can start the app by importing it by doing:
```
from fft_analysator.app import App

App().serve_app()
```
If you only want to use the API and are not interested in using the GUI, you can refer to the API documentation and should preferably choose option 2.
