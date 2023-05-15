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