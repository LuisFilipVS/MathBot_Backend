import unittest
from robo import *

CONFIANCA_MINIMA = 0.5

class TesteSaudacoes(unittest.TestCase):
    
    def setUp(self):
        self.configured, self.bot = config_the_bot()

    def test_01_bot_configured(self):
        self.assertTrue(self.configured)

    def test_02_basics_greetings(self):
        list_greetings = ["oi","opa","eai","ola","tudo bom?","tudo bem?"]

        for greeting in list_greetings:
            print(f"Realizando teste de saudação: {greeting}")

            response = self.bot.get_response(greeting)
            self.assertGreater(response.confidence,CONFIANCA_MINIMA)
            self.assertIn("Olá, eu me chamo MathBot, Bot tutor de matemática, e estou pronto para te ajudar! Me fale o que deseja!", response.text)

    def test_03_variabilitys_of_basics_greetings(self):
        list_greetings = ["oi, tudo bem", "como vai, tudo bem"]

        for greeting in list_greetings:
            print(f"Realizando teste de saudação: {greeting}")

            response = self.bot.get_response(greeting)

            print(f"Obtendo a confianca: {response.confidence}")
            self.assertGreaterEqual(response.confidence,CONFIANCA_MINIMA)
            self.assertIn("Olá, eu me chamo MathBot, Bot tutor de matemática, e estou pronto para te ajudar! Me fale o que deseja!", response.text)

class TesteMath(unittest.TestCase):
    
    def setUp(self):
        self.configured, self.bot = config_the_bot()

    def test_01_bot_configured(self):
        self.assertTrue(self.configured)

    
    def test_02_set(self):
        list_question = ["o que sao conjuntos?", "o que sao conjuntos numericos", "me fala o que é conjuntos numericos" , "explique sobre conjuntos numericos" , "me ajuda com conjuntos numericos"]

        for question in list_question:
            print(f"perguntando: {question}")
            
            response = self.bot.get_response(question)
            self.assertGreaterEqual(response.confidence, CONFIANCA_MINIMA)
            self.assertIn("Vamos lá!Conjuntos numéricos são elementos importantes da matématica no qual é a categorização de numeros que tem a mesma característica, e que surgiram durante o desenvolvimento da humanidade baseando na necessidade de responder certos questionamentos que iam surgindo.Por exemplo, os numeros {1,2,3,4,5} fazem parte conjuntos de números naturais, por outro lado, os numeros {1.2, 2.4, 3.6 , 1.43} fazem parte do conjunto de numeros racionais", response.text)
    
    def test_03_variability_set(self):
        list_question = ["o que sao conjuntos?", "defina conjuntos numericos"]

        for question in list_question:
            print(f"perguntando: {question}")
            
            response = self.bot.get_response(question)
            self.assertGreaterEqual(response.confidence, CONFIANCA_MINIMA)
            self.assertIn("Vamos lá!Conjuntos numéricos são elementos importantes da matématica no qual é a categorização de numeros que tem a mesma característica, e que surgiram durante o desenvolvimento da humanidade baseando na necessidade de responder certos questionamentos que iam surgindo.Por exemplo, os numeros {1,2,3,4,5} fazem parte conjuntos de números naturais, por outro lado, os numeros {1.2, 2.4, 3.6 , 1.43} fazem parte do conjunto de numeros racionais", response.text)
    
    def test_04_complex_number(self):
        list_question = ["o que eh um numero imaginario?","me fala o que sao numeros imaginarios", "me explique que eh numeros imaginarios" ]

        for question in list_question:
            print(f"perguntando: {question}")
            
            response = self.bot.get_response(question)
            self.assertGreaterEqual(response.confidence, CONFIANCA_MINIMA)
            self.assertIn("Números imaginários fazem parte do conjunto de números complexos no qual sua parte real é igual a zero, e representados por 'ib' no qual b é uma unidade real e i é a unidade imaginário. Essa categoria de numeros foi desenvolvida de Renê Decartes e tem aplicação na física quântica.Para exemplicar: sqrt(-1) = i", response.text)
    
    def test_05_variability_complex_number(self):
        list_question = ["o que eh um numero imaginario?","defina numeros imaginarios"]

        for question in list_question:
            print(f"perguntando: {question}")
            
            response = self.bot.get_response(question)
            self.assertGreaterEqual(response.confidence, CONFIANCA_MINIMA)
            self.assertIn("Números imaginários fazem parte do conjunto de números complexos no qual sua parte real é igual a zero, e representados por 'ib' no qual b é uma unidade real e i é a unidade imaginário. Essa categoria de numeros foi desenvolvida de Renê Decartes e tem aplicação na física quântica.Para exemplicar: sqrt(-1) = i", response.text)
    
    
    def test_06_polynomial(self):
        list_question = ["o que sao polinomios?","me explica o que sao polinomios", "defina polinomios"]

        for question in list_question:
            print(f"perguntando: {question}")
            
            response = self.bot.get_response(question)
            self.assertGreaterEqual(response.confidence, CONFIANCA_MINIMA)
            self.assertIn("Polinômios são expressões algébricas de um conjunto de monômios(expressão albébrica constituída por um coeficiente numérico e uma parte literal. Ex. 2x²) distintosEx. 2x² + 3x⁴ => este pode ser categorizado com um polinômio de grau 4.", response.text)
    
    def test_07_variability_polynomial(self):
        list_question = ["fale sobre polinomios", "resuma polinomios"]

        for question in list_question:
            print(f"perguntando: {question}")
            
            response = self.bot.get_response(question)
            self.assertGreaterEqual(response.confidence, CONFIANCA_MINIMA)
            self.assertIn("Polinômios são expressões algébricas de um conjunto de monômios(expressão albébrica constituída por um coeficiente numérico e uma parte literal. Ex. 2x²) distintosEx. 2x² + 3x⁴ => este pode ser categorizado com um polinômio de grau 4.", response.text)
    
    def test_08_polygons(self):
        list_question = ["o que sao poligonos?","defina poligonos", "me de uma breve definicao de poligonos", "me explique o que sao poligonos"]

        for question in list_question:
            print(f"perguntando: {question}")
            
            response = self.bot.get_response(question)
            self.assertGreaterEqual(response.confidence, CONFIANCA_MINIMA)
            self.assertIn("Poligonos fazem parte da área de geometria plana, definidos por uma figura fechada com inúmeros lados(segmentos de reta)", response.text)
    
    def test_09_variabilty_polygons(self):
        list_question = ["resuma poligonos?","fale sobre poligonos"]

        for question in list_question:
            print(f"perguntando: {question}")
            
            response = self.bot.get_response(question)
            self.assertGreaterEqual(response.confidence, CONFIANCA_MINIMA)
            self.assertIn("Poligonos fazem parte da área de geometria plana, definidos por uma figura fechada com inúmeros lados(segmentos de reta)", response.text)
    
    def test_10_golden_ratio(self):
        list_question = ["o que eh a proporcao aurea?", "defina a proporcao aurea","me fala sobre a proporcao aurea"]

        for question in list_question:
            print(f"perguntando: {question}")
            
            response = self.bot.get_response(question)
            self.assertGreaterEqual(response.confidence, CONFIANCA_MINIMA)
            self.assertIn("Proporção Áurea, ou número de Ouro, é uma constante real algébrica irracional utilizada na arquitetura, artes e design gráfico, e comumente associoada à sequência de Fibonacci. Em resumo: dois números estão em proporção áurea se a razão deles é a igual a soma dos mesmos pela divisao do maior número. (a + b)/a = a/b = 1,618033...", response.text)
      
    def test_11_variabilty_golden_ratio(self):
        list_question = ["resuma a proporcao aurea?", "fale sobre a proporcao aurea"]

        for question in list_question:
            print(f"perguntando: {question}")
            
            response = self.bot.get_response(question)
            self.assertGreaterEqual(response.confidence, CONFIANCA_MINIMA)
            self.assertIn("Proporção Áurea, ou número de Ouro, é uma constante real algébrica irracional utilizada na arquitetura, artes e design gráfico, e comumente associoada à sequência de Fibonacci. Em resumo: dois números estão em proporção áurea se a razão deles é a igual a soma dos mesmos pela divisao do maior número. (a + b)/a = a/b = 1,618033...", response.text)
    

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))
    testes.addTest(carregador.loadTestsFromTestCase(TesteMath))

    executor = unittest.TextTestRunner()
    executor.run(testes)