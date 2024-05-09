import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from analysis.signal_processing import example_plot
from .components import menu_bar as mb

class FFTAnalyzerApp:
    def __init__(self, master):
        self.master = master
        self.master.title('FFT Analyzer')

        # Scale the window to 80% of the screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)
        # Center the window
        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)
        self.master.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

        self.setup_gui()

    def setup_gui(self):
        # Create a menu bar
        self.menu_bar = mb.setup_menu(self.master, self.load_signals, self.show_example_plot)
        self.master.config(menu=self.menu_bar)

        # Placeholder for storing the signal files
        self.signal_files = []

    def load_signals(self):
        """ Load two measuring signals from files """
        try:
            # Ask the user to select files
            file_paths = filedialog.askopenfilenames(title="Select two signal files", filetypes=[("All files", "*.*")])
            
            if len(file_paths) != 2:
                messagebox.showerror("Error", "Please select exactly two files.")
                return

            self.signal_files = file_paths
            messagebox.showinfo("Files Loaded", f"Successfully loaded files:\n{file_paths[0]}\n{file_paths[1]}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load files: {e}")

    def show_example_plot(self):
        """ Generate and show an example plot using the analysis module """
        ax, canvas = example_plot(self.master)
        canvas.draw()
