#ChatBot em Python

Este é um projeto de chatbot em Python com integração Web e backend em Flask
entitulado MathBot, pois o mesmo é focado em auxiliar usuários com conceitos matemáticos.

## Funcionamento

* O programa se inicia por meio de um chat web que aguarda perguntas e retorna respostas para a mesmas.
* O chat é capaz de responder:
 - O que são conjuntos numéricos?
 - O que um número Imaginário?
 - O que são polinômios?
 - O que são polígonos?
 - O que é a proporção Áurea?

## Inicialização
* Primeiramente, instale as dependências necessárias contidos no arquivo requirements

~~~bash
pip install -r requirements.txt
~~~

* Inicialize o backend executando o arquivo service.py

~~~bash
python service.py
~~~

* Inicialize o backend por meio do arquivo index.js, contido na pasta chat

~~~bash
node index.js
~~~

* Após realização dos processos acima, acesse o navegador e digite o seguinte endereço:
**http://localhost:3000**
