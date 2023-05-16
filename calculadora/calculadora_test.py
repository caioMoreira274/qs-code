import unittest
from math_samples import Calculadora

class TestCalculadora(unittest.TestCase):

    def test_somar_0_0(self):
        saida = Calculadora.somar(x=0,y=0)
        esperado = 0

        self.assertEqual(saida,esperado)

    def test_somar_0_1(self):
        saida = Calculadora.somar(x=0,y=1)
        esperado = 1

        self.assertEqual(saida,esperado)

    def test_somar_1_1(self):
        saida = Calculadora.somar(x=1,y=1)
        esperado = 2

        self.assertEqual(saida,esperado)

    def test_subtrair_0_0(self):
        saida = Calculadora.subtrair(x=0,y=0)
        esperado = 0

        self.assertEqual(saida,esperado)

    def test_subtrair_0_1(self):
        saida = Calculadora.subtrair(x=0,y=1)
        esperado = -1

        self.assertEqual(saida,esperado)

    def test_subtrair_1_1(self):
        saida = Calculadora.subtrair(x=1,y=1)
        esperado = 0

        self.assertEqual(saida,esperado)
        
    def test_multiplicar_0_0(self):
        saida = Calculadora.multiplicar(x=0,y=0)
        esperado = 0

        self.assertEqual(saida,esperado)  

    def test_multiplicar_1_0(self):
        saida = Calculadora.multiplicar(x=1,y=0)
        esperado = 0

        self.assertEqual(saida,esperado) 

    def test_multiplicar_1_1(self):
        saida = Calculadora.multiplicar(x=1,y=1)
        esperado = 1

        self.assertEqual(saida,esperado)

    def test_dividir_0_0(self):
        saida = Calculadora.dividir(x=0,y=0)
        esperado = 'undefined'

        self.assertEqual(saida,esperado) 


 
    


