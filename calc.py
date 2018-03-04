#!/usr/bin/python3
"""
Servidor de calculadora que hereda de webapp.py para crear socket y atarlo a un
puerto, y de calculadora.py para las funciones propias de una calculadora.
"""

import calculadora
import webapp

class Calculadora(webapp.webApp):

    def parse(self, request):
        return request.split()[1].split('/')[1:] #['1', 'suma', '2']

    def process(self, parsedRequest):
        op1, operacion, op2 = parsedRequest
        
        num1 = int(op1)
        num2 = int(op2)

        resultado = calculadora.funciones[operacion](num1, num2)

        return("200 OK", "<html><body><h1>" + str(resultado) + "</h1></body></html>")

if __name__ == "__main__":
    appCalc = Calculadora("localhost", 1234) #instancio la clase Calculadora
