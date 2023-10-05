import random
import os
from config_audio import Fala_Voz


class Programa:
    def __init__(self):
        self.assistente = Fala_Voz()

    def ADP(self, user_input):
        match user_input:

            case'abrir brave':
                variante = random.choice(
                    ["Tudo bem!"])
                self.assistente.falar(variante)
                os.startfile("C:\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
                self.assistente.falar('Abrindo Brave...')

            case'fechar brave', 'fechar Brave':
                variante = random.choice(
                    ["Mais já? Vou fechar"])
                self.assistente.falar(variante)
                os.system("taskkill /f /im brave.exe")
                self.assistente.falar('Brave fechado')

            case'abrir cpu-z':
                os.startfile("C:\Program Files\CPUID\ASUS CPU-Z\cpuz_tuf.exe")
                self.assistente.falar('Abrindo c-p-u-z...')

            case'fechar cpu-z':
                os.system("taskkill /f /im cpuz_tuf.exe")
                self.assistente.falar('c-p-e-u-z fechada')
