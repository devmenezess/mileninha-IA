import os
import psutil
from config_audio import Fala_Voz
import random
import pyautogui


class Windows:
    def __init__(self):
        self.assistente = Fala_Voz()

    def ADW(self, user_input):
        match user_input:
            case "limpar":
                self.assistente.falar("Limpando arquivos temporários...")
                os.system("del /s /f /q c:\windows\temp\*.*")
                os.system("rd /s /q c:\windows\temp")
                os.system("md c:\windows\temp")
                os.system("del /s /f /q C:\WINDOWS\Prefetch")
                os.system("del /s /f /q %temp%\*.*")
                os.system("rd /s /q %temp%")
                os.system("md %temp%")
                os.system("deltree /y c:\windows\tempor~1")
                os.system("deltree /y c:\windows\temp")
                os.system("deltree /y c:\windows\tmp")
                os.system("deltree /y c:\windows\ff*.tmp")
                os.system("deltree /y c:\windows\history")
                os.system("deltree /y c:\windows\cookies")
                os.system("deltree /y c:\windows\recent")
                os.system("deltree /y c:\windows\spool\printers")
                os.system("del c:\WIN386.SWP")
                self.assistente.falar("Arquivos temporários limpos.")

            case "cpu":
                self.assistente.falar("Buscando uso da CPU...")
                cpu = psutil.cpu_percent()
                self.assistente.falar(f'A CPU está em {cpu:.2f} porcento.')

            case "memória":
                self.assistente.falar("Buscando uso de memória...")
                memoryview = psutil.swap_memory()
                self.assistente.falar(
                    f'Memória livre é {int(memoryview.free)} bytes.')

            case "fechar janela":
                variante = random.choice(
                    ["ok", "tudo bem!", "fechando!",])
                self.assistente.falar(variante)
                pyautogui.hotkey('ctrl', 'w')
                self.assistente.falar('Janela fechada')

            case 'esconder janela':
                variante = random.choice(
                    ["ok", "tudo bem!", "escondendo!",])
                self.assistente.falar(variante)
                pyautogui.hotkey('win', 'down')
                self.assistente.falar('Janela escondida')

            case 'abrir calculadora':
                variante = random.choice(
                    ["ok", "tudo bem!", "abrindo!"])
                self.assistente.falar(variante)
                os.system('calc')
                self.assistente.falar('Calculadora aberta')

            case 'fechar calculadora':
                variante = random.choice(
                    ["ok", "tudo bem!", "fechando!",])
                self.assistente.falar(variante)
                os.system("taskkill /f /im CalculatorApp.exe")
                self.assistente.falar('Calculadora fechada')

            case "desligar o pc em meia hora":
                self.assistente.falar('desligando em meia hora')
                os.system("shutdown -s -t 1800")

            case "desligar o pc em uma hora":
                self.assistente.falar("desligando em uma hora")
                os.system("shutdown -s -t 3600")

            case "desligar o pc agora":
                self.assistente.falar("desligando agora")
                os.system("shutdown -s -t 3")

            case "cancelar desligamento":
                self.assistente.falar("cancelando o desligamento")
                os.system("shutdown -a")

            case "bateria":
                try:
                    bateria = psutil.sensors_battery()
                    carga = bateria.percent
                    bp = str(bateria.percent)
                    bpint = "{:.0f}".format(float(bp))
                    self.assistente.falar("A bateria está em:" + bpint + '%')
                    if carga <= 20:
                        self.assistente.falar('Ela está em nivel crítico')
                        self.assistente.falar(
                            'Por favor, coloque o carregador')
                    elif carga == 100:
                        self.assistente.falar('Ela está totalmente carregada')
                        self.assistente.falar('Retire o carregador da tomada')
                except:
                    self.assistente.falar('Desculpa')
                    self.assistente.falar(
                        'Seu dispositivo atual não está usando bateria')
                    self.assistente.falar(
                        'Por isso é impossivel informar a quantidade de carga')
