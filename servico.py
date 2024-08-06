#Importação da bibliotecas externas necessárias para o funcionamento do código
from flask import Flask, jsonify
from robo import *
from flask_cors import CORS

service = Flask("ifbabot")
CORS(service)

#Iniciando instancia do Robo
configured, bot = config_the_bot()

#Definição de rota que retorna as informações do projeto
@service.get("/mathBot/info")
def get_informacoes():
    return jsonify(
        descricao = "Robô de Auxilio Matematico",
        email = "lfilipevs.contato@gmail.com",
        versao = "1.0",
        robo_online = configured
    )

#Definicao de rota que retorna a resposta para a pergunta do usuário
@service.get("/MathBot/response/<string:message>")
def get_response(message):
    response = bot.get_response(message)

    if response.confidence < 0.5:
        response.text = "Desculpe, não endendi a sua solicitação"
    
    return jsonify(
        response = response.text,
        confidence = response.confidence
    )

#Iniciando a instância se este arquivo for o principal
if __name__ == "__main__":
    from waitress import serve
    serve(service, host="0.0.0.0", port=8080)
