from common.VoiceRecorder import VoiceRecorder
from common.TextReader import TextReader
from common.VoiceRecognition import VoiceRecognition
import os

def RecordVoice():
    voice = VoiceRecorder()
    voice.StartRecord()

def ReadFile():
    reader = TextReader(os.path.dirname(__file__) + '/input/pdf_file.pdf')
    reader.StartReading()

def RecognizeVoice():
    text = VoiceRecognition()
    value = text.StartRecognition()
    print(value)

if __name__ == '__main__':
    print('*'*5 + ' Options ' + '*'*5)
    print('1. RecordVoice')
    print('2. ReadFile')
    print('3. RecognizeVoice')

    try:
        choice = int(input("Select your option: \n"))
    except:
        choice = 0

    if choice == 1:
        RecordVoice()
    elif choice == 2:
        ReadFile()
    elif choice == 3:
        RecognizeVoice()
    else:
        print(f'Selected choice is not valid')
