# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 1, 1, 5]
# def zipper(lista1, lista2):
#     intervalo = min(len(lista1), len(lista2))
#     return [(lista1[i], lista2[i]) for i in range(intervalo)]

# print(zipper(l1, l2))

def soma_lista(lista1, lista2):
    intervalo = min(len(lista1), len(lista2))
    return [lista1[i] + lista2[i] for i in range(intervalo)]


print(soma_lista(l1,l2))
