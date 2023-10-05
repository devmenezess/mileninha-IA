import sys
import pyttsx3
import speech_recognition as sr

lang = 'pt_BR.UTF-8'
sys.stdout = open(sys.stdout.fileno(), mode='w',
                  encoding='utf-8', buffering=1)


class Fala_Voz:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.setProperty('rate', 200)
        self.engine.setProperty('volume', 1)

    def falar(self, texto):
        print("Fala:", texto)
        self.engine.say(texto)
        self.engine.runAndWait()

    def ouvir(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.3)
            print("Aguardando sua fala...")
            audio = r.listen(source)
        try:
            print("Reconhecendo...")
            user_input = r.recognize_google(audio, language='pt-BR').lower()
            print('Usuário disse: %s' % user_input)
            return user_input
        except Exception as e:
            print("Não entendi o que você disse.")
            return self.ouvir()
