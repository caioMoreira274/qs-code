class Empregado:
    def __init__(self, primeiro_nome, sobrenome, cargo, salario):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.cargo = cargo
        self.salario = salario
        self.taxa_reajuste = 1.05

    def calcular_reajuste(self):
        return self.salario * self.taxa_reajuste

    def gerar_nome_completo(self):
        return self.primeiro_nome + " " + self.sobrenome

    def validar_cargo(self):
        cargos = ['Presidente', 'Diretor', 'Gerente', 'Analista', 'Auxiliar']
        if self.cargo in cargos:
            return self.cargo
        else:
            return 'Cargo não existente'
        





