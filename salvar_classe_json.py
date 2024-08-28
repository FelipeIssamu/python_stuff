import json
import os
from random import random
from pathlib import Path

desktop = Path.home() / 'Desktop' / 'aaaaa'
desktop.mkdir(exist_ok=True)

for i in range(10):
    file = desktop / f'files{random()}.txt'
    file.touch()



print(desktop)

# CAMINHO = 'classePessoa.json'



# def salvar(pessoa, caminho):
#     with open(caminho, 'w', encoding='utf8') as arquivo:
#         json.dump(pessoa, arquivo, indent=2, ensure_ascii=False)
#         return

# class Pessoa:
#     def __init__(self, nome, sobrenome, idade):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade
#         ... 

# listapessoas = []
# listapessoas.append(vars(Pessoa('felipe issamu', 'Kuratomi', 26)))
# listapessoas.append(vars(Pessoa('miguel', 'kuratomi', 4)))

# salvar(listapessoas, caminho_desktop)




