import unittest
from math_samples import Calculadora

class TestCalculadora(unittest.TestCase):

    def test_somar_0_0(self):
        saida = Calculadora.somar(x=0,y=0)
        esperado = 0

        self.assertEqual(saida,esperado)