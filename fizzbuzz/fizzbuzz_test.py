import unittest
from math_samples import MathSamples

class TestFizzbuzz(unittest.TestCase):

    def test_fizzbuzz(self):
        saida = MathSamples.fizzbuzz(n = 1)
        esperado = 1

        self.assertEqual(saida, esperado)