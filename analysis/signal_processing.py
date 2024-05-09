import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def example_plot(master):
    figure = plt.Figure(figsize=(5, 4), dpi=100)
    ax = figure.add_subplot(111)
    t = np.linspace(0, 2 * np.pi, 100)
    s = np.sin(t)
    ax.plot(t, s)
    ax.set_title("Example Plot: Sine Wave")
    canvas = FigureCanvasTkAgg(figure, master=master)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    return ax, canvas
