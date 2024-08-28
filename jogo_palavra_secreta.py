import os

palavra_secreta = 'felipe'
jogo = True
letra_certa = ''
contador = 0

while jogo:
    letra = input('Digite uma letra: ')
    contador += 1
    if len(letra) > 1:
        print('digite somente uma letra!')
        continue
    if letra in palavra_secreta:
        letra_certa += letra

    palavra_formada = ''

    for i in palavra_secreta:
        if i in letra_certa:
            palavra_formada += i
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Parabéns você ganhou!')
        print(f'numeros de tentativas {contador}')
        print(f'A palavra secreta era: {palavra_secreta}')
