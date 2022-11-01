# Importing  the necessary packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
# reading the file data
frequency_sampling, audio_signal = wavfile.read("//home/saidimu/4.1/Artificial intelligence/mixkit-close-"
                                                "sea-waves-loop-1195.wav")
# Here, we'll use the below instructions to provide information about the audio signal,
# including its sampling frequency, data type, and duration.
print('\nSignal shape:', audio_signal.shape)
print('Signal Datatype:', audio_signal.dtype)
print('Signal duration:', round(audio_signal.shape[0] /
float(frequency_sampling), 2), 'seconds')
# Here, we'll normalize the signal with the following line of code
audio_signal = audio_signal / np.power(2, 15)
length_signal = len(audio_signal)
half_length = np.ceil((length_signal + 1) / 2.0).astype(int)
# This code calculates the Fast Fourier Transform of the audio signal.
signal_frequency = np.fft.fft(audio_signal)
#Now, do the normalization of frequency domain signal and square it:
signal_frequency = abs(signal_frequency[0:half_length]) / length_signal
signal_frequency **= 2
# Next, extract the length and half-length of the frequency transformed signal:
len_fts = len(signal_frequency)
# Note that the Fourier transformed signal must be adjusted for even as well as odd case.
if length_signal % 2:
 signal_frequency[1:len_fts] *= 2
else:
 signal_frequency[1:len_fts-1] *= 2
 # Now, extract the power in decibal(dB):
signal_power = 10 * np.log10(signal_frequency)
x_axis = np.arange(0, half_length, 1) * (frequency_sampling / length_signal) / 1000.0
plt.figure()
plt.plot(x_axis, signal_power, color='blue')
plt.xlabel('Frequency (kHz)')
plt.ylabel('Signal power (dB)')
plt.show()