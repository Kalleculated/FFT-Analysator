import acoular as ac
import numpy as np


class Signal_Process:
    """
    The Signal_Process class handles every signal processing method block-wise and returns its results as a Numpy Array.
    It is initialized by a required the file_path, a window option for the Fourier transformation, a given block_size
    and an Overlap percentage. Possible signal processing are CSM calculation (Cross Spectral Matrix), coherence between
    two signals, frequency and impulse response between input and output data and cross/auto correlation between two
    given signals.


    Attributes:
        file_path (string): A Path to import.
        window (string): Window name for the FFT
        block_size (int): Block size for processing.
        overlap (string): Overlap percentage
        channels (list): List of channels
        current_data (Numpy Array): Current Data for the Signal tab
        impulse_response_data (Numpy Array): Data for the Impulse response
        amplitude_response_data (Numpy Array): Data for the Amplitude response
        phase_response_data (Numpy Array): Data for the Phase
        data_callback (object):
        p0 (int): Is equal to 20*10**-6. Auditory threshold
        source (MaskedTimeSamples): MaskedTimeSamples class to filter out channles
        abtastrate (int): Sample frequency
        numchannels_total (int): Total numbers of channels
        invalid_channel_list (list): Invalid channel list
        powerspectra (PowerSpectra): Acoular Powerspectra class for calculation
        input_channel (int): Input channel
        output_channel (int): Output channel


    Methods:
        set_parameters(int, str, str): Sets Parameters
        invalid_channels(list): Filters all invalid channels
        create_time_axis(int): Creates time axis
        create_frequency_axis(): Creates frequncy axis
        create_correlation_axis(int): Create correlation axis
        SPL(channel): Calculates Sound Pressure Level
        csm(csm_dB=False): Calculates Cross spectral Matrix
        coherence(): Calculates Coherence
        frequency_response( frq_rsp_dB=True): Calculates frequency response
        phase_response(deg=True): Calculates phase response
        impuls_response(imp_dB=False): Calculates impulse response
        correlation(type=None): Calculates correlation
    """

    def __init__(self, channels=[], file_path=None, window='Hanning', block_size=1024, overlap='50%', data_callback=None):
        """
        Constructs all the necessary attributes for the Signal_Process object.


        Args:
            file_path (object): Get the callback to the data object
            window (string): window function for the fourier transformation: Allowed options: 'Rectangular', 'Hanning', 'Hamming', 'Bartlett', 'Blackman'
            block_size (int): Length of data block. Allowed values: 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536
            overlap (string): Overlap percentage between two blocks for the Welch-Method. Allowed options: 'None', '50%', '75%', '87.5%'
        """
        self.file_path = file_path
        self.window = window
        self.block_size = block_size
        self.overlap = overlap
        self.channels = channels
        self.current_data = None
        self.impulse_response_data = None
        self.amplitude_response_data = None
        self.phase_response_data = None
        self.data_callback = data_callback
        self.p0 = 20*10**-6 #auditory threshold

        if file_path:

            self.source = ac.MaskedTimeSamples(name=self.file_path)
            self.abtastrate = self.source.sample_freq
            self.numchannels_total = self.source.numchannels_total
            self.invalid_channel_list = []
            self.powerspectra = None

            if channels:
                if len(channels) == 1:
                    self.input_channel = self.channels[0]
                    self.output_channel = self.channels[0]
                else:
                    self.input_channel = self.channels[0]
                    self.output_channel = self.channels[1]

    def set_parameters(self, channels, window, overlap):
        if channels:
            self.channels = channels

            if len(channels) == 1:
                self.input_channel = self.channels[0]
                self.output_channel = self.channels[0]
            else:
                self.input_channel = self.channels[0]
                self.output_channel = self.channels[1]

        self.window = window
        self.overlap = overlap

        self.invalid_channels([self.input_channel, self.output_channel])
        self.powerspectra = ac.PowerSpectra(time_data=self.source, block_size=self.block_size,
                                                    window=self.window, overlap=self.overlap)

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

        Returns:
            time_axis (np.array): The time axis.
        """

        time_axis = np.arange(N) / self.abtastrate

        return time_axis

    # create frequency axis
    def create_frequency_axis(self):
        """
        The create_frequency_axis function creates the x-Axis for the frequency function

        Returns:
            powerspectra.fftfreq (np.array): The frequency axis
        """

        return self.powerspectra.fftfreq()

    # create time delay axis
    def create_correlation_axis(self, N):
        """
        The create_correlation_axis function creates the x-Axis for the correlation function

        Args:
            N (int): Size of the axis

        Returns:
            tau (np.array): The correlation axis
        """

        block_size_factor = self.data_callback.source.numsamples / self.block_size
        if N % 2 == 0:
            tau = np.arange(-N//2,N//2-1) * 4 * block_size_factor / self.abtastrate
        else:
            tau = np.arange(-N//2,N//2) * 4 * block_size_factor / self.abtastrate

        return tau

    def SPL(self, channel):
        """
        The SPL function calculates the Sound Pressure Level of the current signal.

        Args:
            channel (int): Channel number.

        Returns:
            SPL (int): Sound Pressure Level of a channel
        """

        return 20*np.log10(np.abs(self.data_callback.set_channel_on_data_block(channel))/self.p0)


    # create a cross spectral matrix with the two given signals
    #def csm(self, signal_x, signal_y, window='Hanning', block_size=1024, overlap='50%',dB=False):
    def csm(self,csm_dB=False):
        """
        The csm function calculates the csm (Cross Spectral Matrix) of Acoular for the valid signals. It returns a
        three-dimensional array with size (number of frequencies, 2, 2) where [:, signal1, signal2] is the
        Cross spectral density between signal1 and signal2.

        Args:
            csm_dB (Boolean): Return the array in dB values.

        Returns:
            current_data (np.array): The Cross Spectral Matrix
        """

        if csm_dB:
            self.current_data = 10*np.log10(np.divide(self.powerspectra.csm, 10**-12))
            return self.current_data
        else:
            self.current_data = self.powerspectra.csm
            return self.current_data

    # calculate coherence
    def coherence(self):
        """
        The coherence function calculates the coherence between two given signals.

        Args:
            None

        Returns:
            current_data (np.array): The coherence
        """
        csm_matrix = self.csm()

        if self.input_channel == self.output_channel:
            coherence = np.abs(csm_matrix[:, 0, 0].real)**2 / (csm_matrix[:, 0, 0].real * csm_matrix[:, 0, 0].real)
        else:
            coherence = np.abs(csm_matrix[:, 0, 1])**2 / (csm_matrix[:, 0, 0].real * csm_matrix[:, 1, 1].real)

        self.current_data = coherence

        return self.current_data

    # calculate frequency response based on H1 estimator --> H1 = Gxy / Gxx
    def frequency_response(self, frq_rsp_dB=True):
        """
        The frequency_response function calculates the frequency response between the input and output signal.
        It uses the H1 estimator H1 = Gxy / Gxx, where Gxy is the Cross Spectral density between signal x and signal y
        and Gxx is the Power Spectral Density of signal x.

        Args:
            frq_rsp_dB (boolean): Return the array in dB values.

        Returns:
            amplitude_response_data (np.array): The frequency response
        """
        csm_matrix = self.csm()

        if self.input_channel == self.output_channel:
            H = np.divide(csm_matrix[:, 0, 0].real, csm_matrix[:, 0, 0].real, out=np.zeros_like(csm_matrix[:, 0, 0].real), where=(np.abs(csm_matrix[:, 0, 0].real) > 1e-10))
        else:
            H = np.divide(csm_matrix[:, 0, 1], csm_matrix[:, 0, 0].real, out=np.zeros_like(csm_matrix[:, 0, 1]), where=(np.abs(csm_matrix[:, 0, 1]) > 1e-10))

        if frq_rsp_dB:
            # return SPL(f) based on H1 estimator
            self.amplitude_response_data = 20*np.log10(abs(np.squeeze(H)/self.p0))

        else:
            # absoulte value of H1 estimator
            self.amplitude_response_data = np.abs(np.squeeze(H))

        return self.amplitude_response_data

    # calculate phase response based on H1 estimator --> H1 = Gxy / Gxx
    def phase_response(self, deg=True):
        """
        The phase_response function calculates the phase response between the input and output signal.
        It uses the H1 estimator H1 = Gxy / Gxx, where Gxy is the Cross Spectral Density between signal x and signal y
        and Gxx is the Power Spectral Density of signal x.

        Args:
            deg (boolean): Return the array in degrees

        Returns:
            phase_response_data (np.array): The phase response
        """
        csm_matrix = self.csm()

        if self.input_channel == self.output_channel:
            H = np.divide(csm_matrix[:, 0, 0].real, csm_matrix[:, 0, 0].real, out=np.zeros_like(csm_matrix[:, 0, 0].real), where=(np.abs(csm_matrix[:, 0, 0].real) > 1e0))
        else:
            H = np.divide(csm_matrix[:, 0, 1], csm_matrix[:, 0, 0].real, out=np.zeros_like(csm_matrix[:, 0, 1]), where=(np.abs(csm_matrix[:, 0, 1]) > 1e-10))

        phase = np.angle(H,deg=deg)
        self.phase_response_data = phase

        return self.phase_response_data

    # calculate impulse response based on H1 estimator and inversed fft --> H1 = Gxy / Gxx
    def impuls_response(self,imp_dB=False):
        """
        The impulse_response function calculates the impulse response between the input and output signal.
        It uses the H1 estimator H1 = Gxy / Gxx, where Gxy is the Spectral density between signal x and signal y
        and Gxx is the Power Spectral Density of signal x.

        Args:
            imp_dB (boolean): Return the array in dB values.
        Returns:
            impulse_response_data (np.array): The impulse response
        """
        csm_matrix = self.csm()
        if self.input_channel == self.output_channel:
            H = np.divide(csm_matrix[:, 0, 0].real, csm_matrix[:, 0, 0].real, out=np.zeros_like(csm_matrix[:, 0, 0].real), where=(np.abs(csm_matrix[:, 0, 0].real) > 1e-10))
        else:
            H = np.divide(csm_matrix[:, 0, 1], csm_matrix[:, 0, 0].real, out=np.zeros_like(csm_matrix[:, 0, 1]), where=(np.abs(csm_matrix[:, 0, 1]) > 1e-10))

        N = len(csm_matrix[:, 0, 0])
        self.impulse_response_data = np.fft.irfft(H, n=N)
        shifted_signal = np.fft.fftshift(self.impulse_response_data)
        peak_index = np.argmax(shifted_signal)
        signal_up_to_peak = shifted_signal[:peak_index + 1]
        self.impulse_response_data = np.flip(signal_up_to_peak)


        if imp_dB:
            if self.input_channel != self.output_channel:
                self.impulse_response_data = 20*np.log10(abs(self.impulse_response_data)/self.p0)
            else:
                self.impulse_response_data = np.ones(N)
                self.impulse_response_data = 20*np.log10(abs(self.impulse_response_data)/self.p0)
        else:
            self.impulse_response_data = self.impulse_response_data

        return self.impulse_response_data

    # calculate auto/cross correlation in time domain
    def correlation(self,type=None):
        """
        The correlation function calculates the correlation response between the two given signals.

        Args:
            type (string): Determines if an auto or cross correlation is being calculated. Allowed options: 'xx', 'yy', 'xy'
        Returns:
            current_data (np.array): The correlation data
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

        self.current_data = corr / np.max(np.abs(corr)) # normalize the correlation to max_value

        return self.current_data
