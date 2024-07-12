The FFT Analysator API consist of two classes. 

*Preprocessing:* Handles preprocessing 

*Signal_processing:* Handles calculation

An example of those classes can be seen below. For more Information please refer to the User Manual and Documentation. 

``` py title="Initializing Preprocessing"
import fft_analysator.analysis.preprocessing as pp

my_file_path = 'path/to/file/myFile.h5' # Path to h5-File
my_block_size = 2048 # Choose block size

preproc = pp.(my_file_path, block_size = my_block_size)
```



``` py title="Calculating with Signal Processing"
import fft_analysator.analysis.signal_processing as sp

my_channels = [1,4] # Define your channles
my_window = 'Hanning' # Select a window. 
my_overlap = '75%' # Select overlap

signal_proc = sp.Signal_Processing(channels=[], file_path=my_file_path, block_size=my_block_size)

# One is able to change the parameters by using the method "set_parameters"

signal_proc.set_parameters(my_channles, my_window, my_overlap)

# Calculating now for example the CSM (Cross spectral Matrix). The CSM is a three dimensional array 
# with dimensions [Frequencies, Input channel, Output Channel], where in our case the Input channel is 1 and
# Output channel is 4. The data is complex valued. 

csm_data = signal_proc.csm

csm_data[:,0,1] # Cross spectral density between channel 1 and 4
csm_data[:,0,0] # Auto spectral density of channel 1
csm_data[:,1,1] # Cross spectral density of channel 4
```

