# Observe the following example to understand about recognition of spoken words:
# Import the necessary packages as shown:
import speech_recognition as sr

# Create an object as shown below:
recording = sr.Recognizer()

# Now, the Microphone() module will take the voice as input:
with sr.Microphone() as source: recording.adjust_for_ambient_noise(source)
print("Please Say something:")
audio = recording.listen(source)

# Now google API would recognize the voice and gives the output.
try:
 print("You said: \n" + recording.recognize_google(audio))
except Exception as e:
 print(e)


