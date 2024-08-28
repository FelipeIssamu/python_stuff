def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar2 = criar_multiplicador(2)
duplicar3 = criar_multiplicador(3)
duplicar4 = criar_multiplicador(4)
duplicar5 = criar_multiplicador(5)
duplicar6 = criar_multiplicador(6)


print(duplicar2(7))