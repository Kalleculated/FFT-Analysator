import panel as pn
pn.extension('tabulator', 'terminal', 'ipywidgets',sizing_mode = 'stretch_width', loading_spinner='dots')

from tkinter import Tk, filedialog

class upload_button:
    def __init__(self):
        self.button = pn.widgets.Button(name="Load file")
        self.button.on_click(self.select_files)
        self.files = None
        
    def select_files(self, *b):
        root = Tk()
        root.withdraw()                                        
        root.call('wm', 'attributes', '.', '-topmost', True)   
        files = filedialog.askopenfilename(multiple=False)    
        self.files = files                                       

    @property
    def component(self):
        # Der Getter gibt das gespeicherte Widget zurück
        return self.button