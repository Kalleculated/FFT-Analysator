import numpy as np
import scipy.fft as fft
import scipy.signal as sc
import acoular as ac

class Signal_Process:
    """
    The Signal_Process class handles every signal processing method block-wise and returns its results as a Numpy Array.
    It is initialized by a required the file_path, a window option for the Fourier transformation, a given block_size
    and an Overlap percentage. Possible signal processing are CSM calculation (Cross Spectral Matrix), coherence between
    two signals, frequency and impulse response between input and output data and cross/auto correlation between two
    given signals.

    Args:
        file_path (object): Get the callback to the data object
        window (string): window function for the fourier transformation: Allowed options: 'Rectangular','Hanning',
        'Hamming', 'Bartlett', 'Blackman'
        block_size (int): Length of data block. Allowed values: 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536
        overlap (string): Overlap percentage between two blocks for the Welch-Method. Allowed options: 'None','50%',
        '75%','87.5%'
    """

    def __init__(self, channels, file_path, window='Hanning', block_size=1024, overlap='50%'):
        self.file_path = file_path
        self.window = window
        self.block_size = block_size
        self.overlap = overlap
        self.channels = channels

        if file_path:

            self.source = ac.MaskedTimeSamples(name=self.file_path)
            self.abtastrate = self.source.sample_freq
            self.numchannels_total = self.source.numchannels_total
            #self.invalid_channel_list = []
            #self.powerspectra = None
            
            if channels:
                if len(channels) == 1:
                    self.input_channel = self.channels[0]
                    self.output_channel = self.channels[0]
                else:
                    self.input_channel = self.channels[0]
                    self.output_channel = self.channels[1]
            
                
            self.invalid_channels([self.input_channel, self.output_channel])
            self.powerspectra = ac.PowerSpectra(time_data=self.source, block_size=self.block_size, window=self.window, overlap=self.overlap)
            

    # sort out invalid channels
    def invalid_channels(self, valid_channels):
        """
        The invalid_channels function fills the invalid_channel_list with two valid channels chosen by the user.
        Args:
            valid_channels (list): Contains the two selected channels chosen by the user.
        """

        self.invalid_channel_list = [k for k in range(self.numchannels_total) if k not in valid_channels]
        self.source.invalid_channels = self.invalid_channel_list

    # create a time axis
    def create_time_axis(self, N):
        """
        The create_time_axis function creates a time axis for the x-Axis
        Args:
            N (int): Size of the axis
        """

        time_axis = np.arange(N) / self.abtastrate
        return time_axis

    # create frequency axis
    def create_frequency_axis(self):
        """
        The create_frequency_axis function creates the x-Axis for the frequency function
        """

        return self.powerspectra.fftfreq()

    # create time delay axis
    def create_correlation_axis(self, N):
        """
        The create_correlation_axis function creates the x-Axis for the correlation function
        Args:
            N (int): Size of the axis
        """

        time_delay = np.arange(-N/2,N/2) * 100 / self.abtastrate
        return time_delay

    # create a cross spectral matrix with the two given signals
    #def csm(self, signal_x, signal_y, window='Hanning', block_size=1024, overlap='50%',dB=False):
    def csm(self,csm_dB=False):
        """
        The csm function calculates the csm (Cross Spectral Matrix) of Acoular for the valid signals. It returns a
        three-dimensional array with size (number of frequencies,2,2) where [:, signal1, signal2] is the
        Cross spectral density between signal1 and signal2.

        Args:
            signal_x (numpy array): Input signal defined by the user
            signal_y (numpy array): Output signal defined by the user
            window (string): window function for the fourier transformation: Allowed options: 'Rectangular','Hanning',
            'Hamming', 'Bartlett', 'Blackman'
            block_size (int): Length of data block. Allowed values: 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536
            overlap (string): Overlap percentage between two blocks for the Welch-Method. Allowed options: 'None','50%',
            '75%','87.5%'
            db (boolean): Return the array in dB values.

        """
        # Autopowerspec from signal_x --> self.powerspectra[:,0,0]
        # Autopowerspec from signal_y --> self.powerspectra[:,1,1]
        # Crosspowerspec from x and y --> self.powerspectra[:,0,1]
        #self.invalid_channels([signal_x, signal_y])
        #self.powerspectra = ac.PowerSpectra(time_data=self.source, block_size=block_size, window=window, overlap=overlap)

        if csm_dB:
            return 10*np.log10(self.powerspectra.csm)
        else:
            return self.powerspectra.csm

    # calculate coherence
    def coherence(self):
        """
        The coherence function calculates the coherence between two given signals.

        Args:
            signal_x (numpy array): Input signal defined by the user
            signal_y (numpy array): Output signal defined by the user
        """
        csm_matrix = self.csm()

        if self.input_channel == self.output_channel:
            coherence = np.abs(csm_matrix[:, 0, 0].real)**2 / (csm_matrix[:, 0, 0].real * csm_matrix[:, 0, 0].real)
        else:
            coherence = np.abs(csm_matrix[:, 0, 1])**2 / (csm_matrix[:, 0, 0].real * csm_matrix[:, 1, 1].real)

        return coherence

    # calculate frequency response based on H1 estimator --> H1 = Gxy / Gxx
    def frequency_response(self, frq_rsp_dB=True):
        """
        The frequency_response function calculates the frequency response between the input and output signal.
        It uses the H1 estimator H1 = Gxy / Gxx, where Gxy is the Cross Spectral density between signal x and signal y
        and Gxx is the Power Spectral Density of signal x.

        Args:
            signal_x (numpy array): Input signal defined by the user
            signal_y (numpy array): Output signal defined by the user
            db (boolean): Return the array ian dB values.
        """
        csm_matrix = self.csm()

        if self.input_channel == self.output_channel:
            H = np.divide(csm_matrix[:, 0, 0].real, csm_matrix[:, 0, 0].real, out=np.zeros_like(csm_matrix[:, 0, 0].real), where=(np.abs(csm_matrix[:, 0, 0].real) > 1e-10))
        else:
            H = np.divide(csm_matrix[:, 0, 1], csm_matrix[:, 0, 0].real, out=np.zeros_like(csm_matrix[:, 0, 1]), where=(np.abs(csm_matrix[:, 0, 1]) > 1e-10))
        if frq_rsp_dB:
            return 20*np.log10(abs(np.squeeze(H)))
        else:
            return np.abs(np.squeeze(H))

    # calculate phase response based on H1 estimator --> H1 = Gxy / Gxx
    def phase_response(self, deg=True):
        """
        The phase_response function calculates the phase response between the input and output signal.
        It uses the H1 estimator H1 = Gxy / Gxx, where Gxy is the Cross Spectral Density between signal x and signal y
        and Gxx is the Power Spectral Density of signal x.

        Args:
            signal_x (numpy array): Input signal defined by the user
            signal_y (numpy array): Output signal defined by the user
            deg (boolean): Return the array in degrees
        """
        csm_matrix = self.csm()

        if self.input_channel == self.output_channel:
            H = np.divide(csm_matrix[:, 0, 0].real, csm_matrix[:, 0, 0].real, out=np.zeros_like(csm_matrix[:, 0, 0].real), where=(np.abs(csm_matrix[:, 0, 0].real) > 1e0))
        else:
            H = np.divide(csm_matrix[:, 0, 1], csm_matrix[:, 0, 0].real, out=np.zeros_like(csm_matrix[:, 0, 1]), where=(np.abs(csm_matrix[:, 0, 1]) > 1e-10))

        phase = np.angle(H,deg=deg)
        return phase

    # calculate impulse response based on H1 estimator and inversed fft --> H1 = Gxy / Gxx
    def impuls_response(self):
        """
        The impulse_response function calculates the impulse response between the input and output signal.
        It uses the H1 estimator H1 = Gxy / Gxx, where Gxy is the Spectral density between signal x and signal y
        and Gxx is the Power Spectral Density of signal x.

        Args:
            signal_x (numpy array): Input signal defined by the user
            signal_y (numpy array): Output signal defined by the user
        """
        csm_matrix = self.csm()
        if self.input_channel == self.output_channel:
            H = np.divide(csm_matrix[:, 0, 0].real, csm_matrix[:, 0, 0].real, out=np.zeros_like(csm_matrix[:, 0, 0].real), where=(np.abs(csm_matrix[:, 0, 0].real) > 1e-10))
        else:
            H = np.divide(csm_matrix[:, 0, 1], csm_matrix[:, 0, 0].real, out=np.zeros_like(csm_matrix[:, 0, 1]), where=(np.abs(csm_matrix[:, 0, 1]) > 1e-10))

        N = len(csm_matrix[:, 0, 0])
        #h = fft.irfft(H, n=N)
        h = np.fft.irfft(H, n=N)
        return h

    # calculate auto/cross correlation in time domain
    def correlation(self,type=None):
        """
        The correlation function calculates the correlation response between the two given signals.

        Args:
            signal_x (numpy array): Input signal defined by the user
            signal_y (numpy array): Output signal defined by the user
            type (string): Determines if an auto or cross correlation is being calculated. Allowed options: 'xx', 'yy', 'xy'
        """
        csm_matrix = self.csm()
        N = len(csm_matrix[:, 0, 0])

        if type == 'xx':
            corr = np.fft.fftshift(np.fft.irfft(csm_matrix[:, 0, 0].real, n=N))
        elif type == 'yy':
            if self.input_channel == self.output_channel:
                corr = np.fft.fftshift(np.fft.irfft(csm_matrix[:, 0, 0].real, n=N))
            else:
                corr = np.fft.fftshift(np.fft.irfft(csm_matrix[:, 1, 1].real, n=N))
        elif type == 'xy':
            if self.input_channel == self.output_channel:
                corr = np.fft.fftshift(np.fft.irfft(csm_matrix[:, 0, 0].real, n=N))
            else:
                corr = np.fft.fftshift(np.fft.irfft(csm_matrix[:, 0, 1], n=N))

        #return np.roll(corr / np.max(np.abs(corr)), N//2)
        return corr / np.max(np.abs(corr))
