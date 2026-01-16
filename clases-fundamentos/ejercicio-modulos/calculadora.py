

class Calculadora:
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            return "Error: Div/0"
        return a / b