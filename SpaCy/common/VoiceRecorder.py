import sounddevice as sd
import soundfile as sf
import os
from datetime import datetime, timezone, timedelta

# References
# https://realpython.com/playing-and-recording-sound-python/
# https://www.geeksforgeeks.org/create-a-voice-recorder-using-python/

class VoiceRecorder():

    def __init__(self, freq=44100, channels=2, duration=5, name='default', format='wav'):
        # Sampling frequency
        self.freq = freq
        # Audio Channels
        self.channels = channels
        # Recording duration
        self.duration = duration
        # File Name
        if name == 'default': 
            name = str(datetime.now().strftime('%Y%m%d_%H%M%S'))
        self.file_name = os.path.dirname(__file__) + '/../results/' + f'{name}.{format}'

    def StartRecord(self):
        print('Starting... Audio Record')
        # Start recorder with the given values of duration and sample frequency
        data = sd.rec(int(self.duration * self.freq),  samplerate=self.freq, channels=self.channels)
        # Record audio for the given number of seconds
        sd.wait()
        # This will convert the NumPy array to an audio file with the given sampling frequency
        sf.write(self.file_name, data, self.freq)
        print('finished.')
