import tkinter as tk

def setup_menu(master, file_callback, cross_corr_callback):
    menu_bar = tk.Menu(master)

    # Add "File" menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=file_callback)

    # Add calculation menu
    calculation_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Berechnung", menu=calculation_menu)
    calculation_menu.add_command(label="Kreuzkorrelation", command=cross_corr_callback)

    return menu_bar