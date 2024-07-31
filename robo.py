#Importação da bibliotecas externas necessárias para o funcionamento do código
from chatterbot import ChatBot
import time

#Definição de uma confiança mínima para ser usada como parâmetro devolução das respostas
MINIMUM_TRUST = 0.50

#Função que define as características do Robo
def config_the_bot():
    try:
        bot = ChatBot("MathBot", read_only = True, logic_adapters = [{"import_path": "chatterbot.logic.BestMatch"}])
    except Exception as e:
        print(f"Erro na criação do Robo: {e}")
    return True, bot

#Iniciando uma instância do robo
def init_the_bot(bot):
    while True:
        message = input("digite alguma coisa...\n")
        response = bot.get_response(message.lower())
        if response.confidence >= MINIMUM_TRUST:
            print(f"MathBot >> {response.text} [confiança={response.confidence}]")
        else:
            print(f"Desculpe, ainda sou incapaz de responder este tipo de pergunta [confiança={response.confidence}, resposta={response.text}]")
            print("pergunte outra coisa")

#Iniciando a instância se este arquivo for o principal
if __name__ == "__main__": 
    configured, bot = config_the_bot()

    if configured:
        init_the_bot(bot)