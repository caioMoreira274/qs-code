import unittest
from math_samples import Empregado


class TestEmpregado(unittest.TestCase):

    def test_reajuste(self):
        funcionario = Empregado('João', 'Silva', 'Auxiliar', 930.00)
        saida = funcionario.calcular_reajuste()
        esperado = 930 * 1.05

        self.assertEqual(saida, esperado)

    def test_gerarNomeCompleto(self):
        funcionario = Empregado('João', 'Silva', 'Auxiliar', 930.00)
        saida = funcionario.gerar_nome_completo()
        esperado = 'João Silva'

        self.assertEqual(saida, esperado)
    
    def test_validar_cargo(self):
        funcionario = Empregado('João', 'Silva', 'Auxiliar', 930.00)
        saida = funcionario.cargo
        esperado = 'Auxiliar'

        self.assertEqual(saida, esperado)


        