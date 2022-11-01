import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features import mfcc, logfbank
# Now, read the stored audio file. It will return two values: the sampling frequency and the
# audio signal. Provide the path of the audio file where it is stored.
frequency_sampling, audio_signal = wavfile.read("//home/saidimu/4.1/Artificial intelligence/mixkit-close-"
                                                "sea-waves-loop-1195.wav")
# Note that here we are taking first 15000 samples for analysis.
audio_signal = audio_signal[:15000]
# Use the MFCC techniques and execute the following command to extract the MFCC features:
features_mfcc = mfcc(audio_signal, frequency_sampling)
# Now, print the MFCC parameters, as shown:
print('\nMFCC:\nNumber of windows =', features_mfcc.shape[0])
print('Length of each feature =', features_mfcc.shape[1])
# Now, plot and visualize the MFCC features using the commands given below:
features_mfcc = features_mfcc.T
plt.matshow(features_mfcc)
plt.title('MFCC')
# In this step, we work with the filter bank features as shown: Extract the filter bank features:
filterbank_features = logfbank(audio_signal, frequency_sampling)
# Now, print the filterbank parameters.
print('\nFilter bank:\nNumber of windows =', filterbank_features.shape[0])
print('Length of each feature =', filterbank_features.shape[1])
# Now, plot and visualize the filterbank features.
filterbank_features = filterbank_features.T
plt.matshow(filterbank_features)
plt.title('Filter bank')
plt.show()