# Hier kommen unsere Funktionen wie Leistungsdichtespektrum, Korrelation etc.
import os

import numpy
import numpy as np
import fft_analysator.analysis.preprocessing as pp
import scipy as sc
import matplotlib.pyplot as plt
import acoular as ac
class Signal_process:
    def __init__(self,data):
        self.current_data = data
    def FFT(self):
        #plt.plot(data_fft2.fftfreq(),ft[:,0])
        #plt.show()
        ac.spectra
        return sc.fft(self.current_data)



