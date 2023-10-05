from config_audio import Fala_Voz
import webbrowser
import pyautogui

webbrowser.register('brave', None, webbrowser.BackgroundBrowser(
    "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"))


class Site:
    def __init__(self):
        self.assistente = Fala_Voz()

    def ADS(self, user_input):
        match user_input:

            case 'pesquise no youtube':
                self.assistente.falar('O que você quer procurar?')
                search = self.assistente.ouvir()
                url = 'https://www.youtube.com/results?search_query=' + search
                webbrowser.get('brave').open_new_tab(url)
                self.assistente.falar(
                    'Aqui está o que eu encontrei para ' + search)
                resposta = self.assistente.ouvir()

                if resposta == 'primeira':
                    pyautogui.moveTo(339, 291)
                    pyautogui.click()
                elif resposta == 'segundo':
                    pyautogui.moveTo(336, 514)
                    pyautogui.click()
                elif resposta == 'terceiro':
                    pyautogui.moveTo(339, 729)
                    pyautogui.click()
                else:
                    self.assistente.falar('Opção não reconhecida.')

            case 'pesquise no google':
                self.assistente.falar('O que você quer procurar?')
                search = self.assistente.ouvir()
                url = 'https://www.google.com.br/search?q=' + search
                webbrowser.get('brave').open_new_tab(url)
                self.assistente.falar(
                    'Aqui está o que eu encontrei para ' + search)

            case 'pesquise no chat':
                self.assistente.falar('O que você quer procurar?')
                search = self.assistente.ouvir()
                url = 'https://chat.openai.com/' + search
                webbrowser.get('brave').open_new_tab(url)
                self.assistente.falar(
                    'Aqui está o que eu encontrei para ' + search)

            case "abrir google":
                self.assistente.falar("Abrindo o Google...")
                webbrowser.open("https://www.google.com.br")
                self.assistente.falar('Google aberto')
                

            case "abrir netflix":
                self.assistente.falar("Abrindo Netflix...")
                webbrowser.open("https://www.netflix.com")
                self.assistente.falar("Netflix aberto")

            case "abrir youtube":
                self.assistente.falar("Abrindo youtube...")
                webbrowser.open("https://www.youtube.com")
                self.assistente.falar("Youtube aberto...")

            case "abrir facebook":
                self.assistente.falar("Abrindo Facebook...")
                webbrowser.open("https://www.facebook.com")
                self.assistente.falar("Facebook aberto...")

            case "abrir instagram":
                self.assistente.falar("Abrindo Instagram...")
                webbrowser.open("https://www.instagram.com")
                self.assistente.falar("Instagram aberto...")

            case "abrir twitter":
                self.assistente.falar("Abrindo Twitter...")
                webbrowser.open("https://twitter.com")
                self.assistente.falar("Twitter aberto...")

            case "abrir linkedin":
                self.assistente.falar("Abrindo LinkedIn...")
                webbrowser.open("https://linkedin.com")
                self.assistente.falar("Linkedin aberto...")

            case "abrir wikipédia":
                self.assistente.falar("Abrindo Wikipedia...")
                webbrowser.open("https://pt.wikipedia.org")
                self.assistente.falar("Wikipedia aberto...")

            case "abrir eleven labs":
                self.assistente.falar("Abrindo Eleven Labs...")
                webbrowser.open("https://elevenlabs.io/")
                self.assistente.falar("Eleven labs aberto...")

            case "abrir chat":
                self.assistente.falar("Abrindo chat gpt...")
                webbrowser.open("https://chat.openai.com/")
                self.assistente.falar("Chat gpt aberto...")
