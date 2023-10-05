from config_audio import Fala_Voz
from datetime import date
from datetime import datetime


class DataH:
    def __init__(self):
        self.assistente = Fala_Voz()

    def DT(self, user_input):
        match user_input:

            case "horário":
                hora = datetime.now()
                horas = hora.strftime('%H horas e %M minutos')
                self.assistente.falar(f'Agora são {horas}')

            case "que dia é hoje":
                dataatual = date.today()
                diassemana = ('Segunda-feira', 'Terça-feira', 'Quarta-feira',
                              'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
                meses = ('Zero', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
                self.assistente.falar(
                    f"Hoje é {diassemana[dataatual.weekday()]}")
                diatexto = f'{dataatual.day} de '
                mesatual = (meses[dataatual.month])
                datatexto = dataatual.strftime(" de %Y")
                self.assistente.falar(f'Dia {diatexto} {mesatual} {datatexto}')
