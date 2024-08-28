perguntas = [
    {
        'Pergunta' : 'Quanto é 2 + 2',
        'Opções' : ['1', '3', '4', '5'],
        'Resposta' : '4',
    },
    {
        'Pergunta' : 'Quanto é 5*5?',
        'Opções' : ['25', '55', '10', '51'],
        'Resposta' : '25',
    },
    {
        'Pergunta' : 'Quanto é 10/2',
        'Opções' : ['4', '5', '2', '1'],
        'Resposta' : '5',
    },
]

for pergunta in perguntas:
    opcao1 = pergunta['Opções']
    print('Pergunta:', pergunta['Pergunta'], end='\n\n')
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})', opcao)

    escolha = input('Digite o indice: ')
    print()
    try:
        if opcao1[int(escolha)] == pergunta['Resposta']:
            print('Acertou:', pergunta['Resposta'])
        else:
            print('Errou')
    except:
        print('Entrada invalida')

# lista = [1, 2, 3]
# faces = {
#     'face1': lista
# }

# print(faces['face1'][2]) 