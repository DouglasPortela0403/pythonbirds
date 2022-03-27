class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos =list(filhos)

    def cumprimentar(self):
        return 'Olá'

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls}, {olhos}'


if __name__ == '__main__':
    p = Pessoa(nome='Mariane')
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
    p.nome = 'Douglas'
    p.idade = 35
    print(p.nome)
    print(p.idade)
    print(Pessoa.olhos)
    print(p.__dict__)
    print(Pessoa.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe())



