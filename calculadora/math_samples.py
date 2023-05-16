class Calculadora:
    
    @staticmethod
    def somar(x,y):
        return x + y

    def subtrair(x,y):
        return x - y

    def multiplicar(x,y):
        return x * y

    def dividir(x,y):
        if y==0:
            return 'undefined'
        return x / y

