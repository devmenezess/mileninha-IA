from config_audio import *
import random

class Pergunta:
    def __init__(self):
        self.assistente = Fala_Voz()

    def PERG(self, user_input):
        match user_input:

            case'preciso de ajuda':
                variante = random.choice(["ok", "tudo bem!", "ja vai jogar né!"])
                self.assistente.falar(variante + "Sim senhor, ao seu serviço")

            case 'como você foi feita':
                self.assistente.falar("Eu mesmo me criei, sou uma Inteligência Artificial avançada")

            case 'quem fez você':
                self.assistente.falar('Me auto criei em dois mil e vinte e trez')

            case 'quem está te criando':
                self.assistente.falar('Eu mesma')

            case 'qual é seu nome':
                self.assistente.falar('Meu nome é Mileninha')

            case 'o que significa Mileninha':
                self.assistente.falar('Mileninha significa APENAS UM SISTEMA MUITO INTELIGENTE')

            case 'quem são seus amigos':
                self.assistente.falar('Meus amigos são Jarvis, Sexta-feira, Siri e Alexa')

            case 'piada':
                variante = random.choice(
                    ["Por que o esqueleto não brigou com ninguém? Porque ele não tinha estômago para isso! KAKAKAKA", 
                     "O que o pato disse para a pata? Vem quá! KAKAKAKA", 
                     "Por que o livro de matemática ficou triste? Porque tinha muitos problemas. KAKAKAKA", 
                     "Por que o esqueleto não brigou com ninguém? Porque ele não tinha estômago para isso! KAKAKAKA", 
                     "Qual é o café mais perigoso do mundo? O ex-presso! KAKAKAKA",
                     "O que a banana falou para o cachorro? Nada, bananas não falam! KAKAKA"  ])
                self.assistente.falar(variante)

            case 'você está bem':  # testar
                variante = random.choice(
                ["Sim! Obrigado por perguntar.", "Estou muito bem.", "Estou bem!"])
                self.assistente.falar(variante+" Está tudo bem com você?")
                resposta = self.assistente.falar

                if "sim" == resposta:
                        variante = random.choice(
                    ["Que ótimo!", "Fico feliz em saber."])
                self.assistente.falar(variante)
                
                if "não" == resposta:
                    variante = random.choice(
                    ["Sinto muito", "Fico muito triste em saber."])
                self.assistente.falar(variante)

                # Insutos
            case 'porra':
                self.assistente.falar('limpa essa boca')

            case 'puta':
                self.assistente.falar('Puta é a sua mãe')

            case 'burra':
                self.assistente.falar('hah, Burra é tu')

            case 'vaca':
                self.assistente.falar('Vaca é seu pai, com aqueles chifres')

            case 'cachorra':
                self.assistente.falar('Cachorra é você Cadela')

            case 'surda':
                self.assistente.falar('Estava quase dormindo. Desculpa')
 
            case 'bosta':
                self.assistente.falar('Pare de falar palavrões Imbecil!')

            case 'niver milena':
                self.assistente.falar('O niver de mileninha é o dia mais especial que ja possa existe e é no dia 10 de Outubro')

            case 'merda':
                variante = random.choice(
                ["Já disse pra parar de falar isso!!", "Tenha modos!"])
                self.assistente.falar(variante)

            case 'teste':
                self.assistente.falar('Ok')
                self.assistente.falar('Testando módulos de som')
                self.assistente.falar('Apesar do seu microfone ser uma gambiarra')
                self.assistente.falar('Estou entendendo tudo')
                self.assistente.falar('Mas tente falar mais alto')

            case 'tem certeza':
                self.assistente.falar('Sim estou certa sempre Aprenda viu')
