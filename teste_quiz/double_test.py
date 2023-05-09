import unittest
from math_samples import MathSamples

class DoubleTest(unittest.TestCase):

    def teste_doub01(self):
        """Testando caso para a entrada = 0"""
        self.assertEqual(
            MathSamples.double(0),
            0
        )



