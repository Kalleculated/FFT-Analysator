import tkinter as tk

def setup_menu(master, load_signals_callback, example_plot_callback):
    menu_bar = tk.Menu(master)

    # Add "File" menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=load_signals_callback)

    # Add calculation menu
    calculation_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Berechnung", menu=calculation_menu)
    calculation_menu.add_command(label="Kreuzkorrelation", command=example_plot_callback)

    return menu_bar