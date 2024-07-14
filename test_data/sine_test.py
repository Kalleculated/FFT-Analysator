from os import getcwd, path
from acoular import __file__ as bpath, MicGeom, SineGenerator, PointSource, Mixer, WriteH5

folder_name = "test_data"
current_directory = getcwd()
full_path = path.join(current_directory, folder_name)
sfreq = 51200  # Sampling frequency
duration = 1  # Duration in seconds
nsamples = duration * sfreq
micgeofile = path.join(path.split(bpath)[0], 'xml', 'array_64.xml')
h5savefile = path.join(full_path, 'three_sources_sine.h5')

# Microphone geometry
m = MicGeom(from_file=micgeofile)

# Sine wave generators
s1 = SineGenerator(sample_freq=sfreq, numsamples=nsamples, freq=1000, rms=1.0)  # 1000 Hz
s2 = SineGenerator(sample_freq=sfreq, numsamples=nsamples, freq=1500, rms=0.7)  # 1500 Hz
s3 = SineGenerator(sample_freq=sfreq, numsamples=nsamples, freq=2000, rms=0.5)  # 2000 Hz

# Point sources with sine wave signals
p1 = PointSource(signal=s1, mics=m, loc=(-0.1, -0.1, 0.3))
p2 = PointSource(signal=s2, mics=m, loc=(0.15, 0, 0.3))
p3 = PointSource(signal=s3, mics=m, loc=(0, 0.1, 0.3))

# Mixer to combine signals
p = Mixer(source=p1, sources=[p2, p3])

# Saving to HDF5 file
wh5 = WriteH5(source=p, name=h5savefile)
wh5.save()
