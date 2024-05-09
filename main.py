import tkinter as tk
from gui.app import FFTAnalyzerApp

def main():
    root = tk.Tk()
    app = FFTAnalyzerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
