import copy
import os
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
base_dir = os.path.dirname(__file__)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

# novos_produtos = copy.copy(produtos)

# for produto in novos_produtos:
#     produto['preco'] += produto['preco'] * 0.10
novos_produtos = [
    {'nome': produto['nome'], 'preco': produto['preco'] * 1.1}
    for produto in produtos
]

produtos_ordenados_por_nome = sorted(produtos, key=lambda p: p['nome'], reverse=True)
produtos_ordenados_por_preco = sorted(produtos, key=lambda p: p['preco'])
print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')

print(base_dir)
