import pyttsx3
import PyPDF2

class TextReader():

    def __init__(self, file):
        self.file = open(file, 'rb')
        self.reader = PyPDF2.PdfFileReader(self.file)
        self.pages = self.reader.numPages
        self.speaker = pyttsx3.init()

    def StartReading(self):
        print('Starting... Text Reading')
        for num in range(self.pages):
            page = self.reader.getPage(num)
            text = page.extractText()
            self.speaker.say(text)
            self.speaker.runAndWait()
        print('finished.')
