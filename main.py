# importing the necessary packages for use in the project
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
# Reading the sound wave file from the directory
frequency_sampling, audio_signal = wavfile.read("//home/saidimu/4.1/Artificial intelligence/mixkit-close-"
                                                "sea-waves-loop-1195.wav")
# Use the code below to show the audio stream's parameters, such as its sampling rate, data type, and length.
print('\nSignal shape:', audio_signal.shape)
print('Signal Datatype:', audio_signal.dtype)
print('Signal duration:', round(audio_signal.shape[0] /
float(frequency_sampling), 2), 'seconds')
# normalizing the signal
audio_signal = audio_signal / np.power(2, 15)
audio_signal = audio_signal [:100]
time_axis = 1000 * np.arange(0, len(audio_signal), 1) / float(frequency_sampling)
# plotting the graph for visualization
plt.plot(time_axis, audio_signal, color='blue')
plt.xlabel('Time (milliseconds)')
plt.ylabel('Amplitude')
plt.title('Input audio signal')
plt.show()