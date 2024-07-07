import numpy as np
import scipy.fft as fft
import scipy.signal as sc
import acoular as ac

class Signal_Process:

    def __init__(self, file_path, window='Hanning', block_size=1024, overlap='50%'):
        self.file_path = file_path
        self.window = window
        self.block_size = block_size
        self.overlap = overlap

        if file_path:

            self.source = ac.MaskedTimeSamples(name=self.file_path)
            self.abtastrate = self.source.sample_freq
            self.numchannels_total = self.source.numchannels_total
            self.invalid_channel_list = []
            self.powerspectra = None

    
    # sort out invalid channels
    def invalid_channels(self, valid_channels):
        self.invalid_channel_list = [k for k in range(self.numchannels_total) if k not in valid_channels] 
        self.source.invalid_channels = self.invalid_channel_list
    
    # create a time axis
    def create_time_axis(self,N):    
        time_axis = np.arange(N) / self.abtastrate
        return time_axis
    
    # create frequency axis
    def create_frequency_axis(self):
        return self.powerspectra.fftfreq()
    
    # create time delay axis
    def create_correlation_axis(self,N):
        time_delay = np.arange(-N/2,N/2) * 100 / self.abtastrate
        return time_delay

    # create a cross spectral matrix with the two given signals
    def csm(self, signal_x, signal_y, window='Hanning', block_size=1024, overlap='50%',dB=False):
        # Autopowerspec from signal_x --> self.powerspectra[:,0,0]
        # Autopowerspec from signal_y --> self.powerspectra[:,1,1]
        # Crosspowerspec from x and y --> self.powerspectra[:,0,1]
        self.invalid_channels([signal_x, signal_y])
        self.powerspectra = ac.PowerSpectra(time_data=self.source, block_size=block_size, window=window, overlap=overlap)
        
        if dB:
            return 10*np.log10(self.powerspectra.csm)
        else:
            return self.powerspectra.csm

    # calculate coherence
    def coherence(self, signal_x, signal_y):
        csm_matrix = self.csm(signal_x, signal_y)
        
        if signal_x == signal_y:
            coherence = np.abs(csm_matrix[:, 0, 0])**2 / (csm_matrix[:, 0, 0].real * csm_matrix[:, 0, 0].real)
        else:
            coherence = np.abs(csm_matrix[:, 0, 1])**2 / (csm_matrix[:, 0, 0].real * csm_matrix[:, 1, 1].real)
            
        return coherence
    
    # calculate frequency response based on H1 estimator --> H1 = Gxy / Gxx
    def frequency_response(self, signal_x, signal_y, dB=True):
        
        csm_matrix = self.csm(signal_x, signal_y)
        
        if signal_x == signal_y:
            H = np.divide(np.abs(csm_matrix[:, 0, 0]), np.abs(csm_matrix[:, 0, 0]), out=np.zeros_like(csm_matrix[:, 0, 0]), where=(np.abs(csm_matrix[:, 0, 0]) > 1e-10))
        else:    
            H = np.divide(csm_matrix[:, 0, 1], csm_matrix[:, 0, 0], out=np.zeros_like(csm_matrix[:, 0, 0]), where=(np.abs(csm_matrix[:, 0, 1]) > 1e-10))
        if dB:
            return 20*np.log10(abs(np.squeeze(H)))
        else:
            return np.abs(np.squeeze(H))
        
    # calculate phase response based on H1 estimator --> H1 = Gxy / Gxx
    def phase_response(self, signal_x, signal_y, deg=True):
        csm_matrix = self.csm(signal_x, signal_y)
        
        if signal_x == signal_y:
            H = np.divide(csm_matrix[:, 0, 0], csm_matrix[:, 0, 0], out=np.zeros_like(csm_matrix[:, 0, 0]), where=(np.abs(csm_matrix[:, 0, 0]) > 1e0))
        else:
            H = np.divide(csm_matrix[:, 0, 1], csm_matrix[:, 0, 0], out=np.zeros_like(csm_matrix[:, 0, 0]), where=(np.abs(csm_matrix[:, 0, 1]) > 1e-10))
            
        phase = np.angle(H,deg=deg)
        return phase
    
    # calculate impulse response based on H1 estimator and inversed fft --> H1 = Gxy / Gxx
    def impuls_response(self, signal_x, signal_y):
        csm_matrix = self.csm(signal_x, signal_y)
        if signal_x == signal_y:
            H = np.divide(csm_matrix[:, 0, 0], csm_matrix[:, 0, 0], out=np.zeros_like(csm_matrix[:, 0, 0]), where=(np.abs(csm_matrix[:, 0, 0]) > 1e-10))
        else:
            H = np.divide(csm_matrix[:, 0, 1], csm_matrix[:, 0, 0], out=np.zeros_like(csm_matrix[:, 0, 0]), where=(np.abs(csm_matrix[:, 0, 1]) > 1e-10))
            
        N = len(csm_matrix[:, 0, 0])
        #h = fft.irfft(H, n=N)
        h = np.fft.irfft(H, n=N)
        return h
        
    # calculate auto/cross correlation in time domain
    def correlation(self, signal_x, signal_y,type=None):
        csm_matrix = self.csm(signal_x, signal_y)
        N = len(csm_matrix[:, 0, 0])

        if type == 'xx':
            corr = np.fft.fftshift(np.fft.irfft(csm_matrix[:, 0, 0], n=N))
        elif type == 'yy':
            if signal_x == signal_y:
                corr = np.fft.fftshift(np.fft.irfft(csm_matrix[:, 0, 0], n=N))
            else:
                corr = np.fft.fftshift(np.fft.irfft(csm_matrix[:, 1, 1], n=N))
        elif type == 'xy':
            if signal_x == signal_y:
                corr = np.fft.fftshift(np.fft.irfft(csm_matrix[:, 0, 0], n=N))
            else:
                corr = np.fft.fftshift(np.fft.irfft(csm_matrix[:, 0, 1], n=N))
              
        #return np.roll(corr / np.max(np.abs(corr)), N//2)
        return corr / np.max(np.abs(corr))
