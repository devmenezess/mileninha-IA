from threading import Thread
from config_audio import Fala_Voz
from config_data import DataH
from config_program import Programa
from config_site import Site
from config_wind import Windows
from janela import window
from per_res import Pergunta


class Assis_Sara:
    def __init__(self):
        Thread(target=window).start()
        self.assistente = Fala_Voz()
        self.configurador = Windows()
        self.program = Programa()
        self.web = Site()
        self.dat = DataH()
        self.pergg = Pergunta()
    def iniciar(self):
        self.assistente.falar("Olá! Eu sou a Mileninha.Como posso te ajudar?")

    def ouvir_comandos(self):
        while True:
            user_input = self.assistente.ouvir()
            if 'tchau' in user_input:
                self.assistente.falar("Até logo!")
                break
            self.configurador.ADW(user_input)
            self.program.ADP(user_input)
            self.web.ADS(user_input)
            self.dat.DT(user_input)
            self.pergg.PERG(user_input)
            
if __name__ == "__main__":
    sara = Assis_Sara()
    sara.iniciar()
    sara.ouvir_comandos()


