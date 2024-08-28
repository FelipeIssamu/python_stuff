# Exercício - Adiando execução de funções
def criar_funcao(funcao):
    def interna(*args, **kwargs):
        return funcao(*args, **kwargs)
    return interna


@criar_funcao
def soma(x, y):
    return x + y


@criar_funcao
def multiplica(x, y):
    return x * y


# soma_com_cinco = criar_funcao(soma, 5)
# multiplica_por_dez = criar_funcao(multiplica, 10)

print(multiplica(10, 5))
