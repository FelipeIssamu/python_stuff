import json
CAMINHO = 'classePessoa.json'


class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        ...


def ler(caminho):
    pessoa = {}
    try:
        with open(caminho, 'r', encoding='utf8') as arquivo:
            pessoa = json.load(arquivo)
            return pessoa

    except FileNotFoundError:
        print('Arquivo não existe')
        with open(caminho, 'x') as arquivo:

            ...


lista = ler(CAMINHO)

print(lista)
