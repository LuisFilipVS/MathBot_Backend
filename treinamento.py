from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import json

CONVERSATIONS = [
    "conversas/saudacoes.json",
    "conversas/matematica.json",
]

#Retorna um treinador para o robo
def define_the_trainer():

    bot = ChatBot("MathBot")
    trainer = ListTrainer(bot)

    return True, trainer


#Carrega as conversas a partir dos arquivos .json
def load_conversations():
    loaded, conversations = True, []

    for doc_of_conversations in CONVERSATIONS:
        try:
            with open(doc_of_conversations, "r", encoding="utf-8") as archive:
                to_train = json.load(archive)
                conversations.append(to_train["conversas"])

                archive.close()
        except Exception as e:
            loaded = False
            print(f"Erro ao carregar arquivos .json: {e}")

    return loaded, conversations

#Recebe o treinador e o conjunto de conversas para realizar o treinamento
def to_train(trainer, conversations):
    for conversation in conversations:
        for response_messages in conversation:
            message = response_messages["mensagens"]
            response = response_messages["resposta"]

            print(f"treinando o robô, mensagens: {message}, resposta: {response}")
            for msg in message:
                trainer.train([msg, response])

#Iniciando a instância se este arquivo for o principal
if __name__ == "__main__":
    configured, trainer = define_the_trainer()

    if configured:
        loaded, conversations = load_conversations()
        if loaded:
            to_train(trainer, conversations)