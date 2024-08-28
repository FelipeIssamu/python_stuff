
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_invertido = nome[::-1]
tam_nome = len(nome)
if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome_invertido}')

    if " " in nome:
        print('Seu nome tem espaços')
    else:
        print('Seu nome não tem espaços')
    print(f'Seu nome tem {tam_nome} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[tam_nome-1]}')
else:
    print('Você deixou campos vazios!!')
    