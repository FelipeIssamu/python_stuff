import os

item = ''
lista_de_compras = []
indice = ''
indice_int = 0

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir, [a]pagar, [l]istar ').lower()
    if len(opcao) > 1:
        os.system('clear')
        print('Digite apenas uma letra!')
    if opcao == '' or opcao == " ":
        os.system('clear')
        print('Digite alguma coisa')
    if opcao == 'i':
        item = input('Digite o item: ')
        lista_de_compras.append(item)
        os.system('clear')
        print(f'Item {item} inserido!')
    elif opcao == 'a':
        try:
            indice = input('Digite o indice para apagar: ')
            indice_int = int(indice)
            indice_removido = lista_de_compras[indice_int]
            lista_de_compras.pop(indice_int)
            os.system('clear')
            print(f'O item {indice_removido} foi removido!')
        except:
            print('Digite um indice válido')          
    elif opcao == 'l':
        if not lista_de_compras:
            print("Lista vazia!")
        for itens in enumerate(lista_de_compras):
            print(itens)
            



