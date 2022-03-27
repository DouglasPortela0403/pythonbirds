class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    def cumprimentar(self):
        return 'Olá'
if __name__ == '__main__':
    p = Pessoa('Mariane')
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
    p.nome = 'Douglas'
    p.idade = 35
    print(p.nome)
    print(p.idade)


