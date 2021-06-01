import speech_recognition as sr

# References:
# https://cloud.google.com/speech-to-text/docs/languages
# https://stackoverflow.com/questions/49732536/how-to-change-the-language-of-google-speech-recognition
# https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14

class VoiceRecognition():

    def __init__(self):
        self.listener = sr.Recognizer()

    def StartRecognition(self):
        try:
            text = ''
            with sr.Microphone() as source:
                print('Listening...')
                voice = self.listener.listen(source)
                text = self.listener.recognize_google(voice, language="es-US") # en-US
            print('finished.')
            return text
        except Exception as e:
            return str(e)
