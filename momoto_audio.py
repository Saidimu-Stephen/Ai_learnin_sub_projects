import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
# Provide the file where the output file should be saved:
output_file = 'audio_signal_generated.wav'
# Now, specify the parameters of your choice, as shown:
duration = 4 # in seconds
frequency_sampling = 44100 # in Hz
frequency_tone = 784
min_val = -4 * np.pi
max_val = 4 * np.pi
# In this step, we can generate the audio signal, as shown:
t = np.linspace(min_val, max_val, duration * frequency_sampling)
audio_signal = np.sin(2 * np.pi * frequency_tone  * t)
# Now, save the audio file in the output file:
# write(output_file, frequency_sampling, signal_scaled)
# Extract the first 100 values for our graph, as shown:
audio_signal = audio_signal[:100]
time_axis = 1000 * np.arange(0, len(audio_signal), 1) / float(frequency_sampling )
# Now, visualize the generated audio signal as follows:
plt.plot(time_axis, audio_signal, color='blue')
plt.xlabel('Time in milliseconds')
plt.ylabel('Amplitude')
plt.title('Generated audio signal')
plt.show()