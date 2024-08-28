import os 
import json
CAMINHO_ARQUIVO = 'lista_dados.json'
def ler(tarefas, caminho):
    dados = []
    try:
        with open(caminho, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        print('Arquivo não exite') 
        salvar(tarefas, caminho)

def salvar(lista_tarefas, caminho):
    
    with open(caminho, 'w', encoding='utf8') as arquivo:
       json.dump(lista_tarefas, arquivo, indent=2, ensure_ascii=False)
       return 
        

lista_buffer = []
lista_de_tarefas = ler([], CAMINHO_ARQUIVO)
while True:
    print('Lista de Tarefas:')
    print() 
    if lista_de_tarefas:
        for tarefa in lista_de_tarefas:
            print(tarefa)
    print()        
    print('Comandos: listar, undo, redo.')
    print()
    opcao = input('Digite uma tarefa ou comando: ').lower()
    if opcao == 'undo':
        if lista_de_tarefas:
            lista_buffer.append(lista_de_tarefas.pop())
            salvar(lista_de_tarefas, CAMINHO_ARQUIVO)
            os.system('clear')
        else:
            os.system('clear')
            print('Nada a retirar')
            print()
        ...
    elif opcao == 'redo':
        if lista_buffer:
            lista_de_tarefas.append(lista_buffer.pop())
            salvar(lista_de_tarefas, CAMINHO_ARQUIVO)
            os.system('clear')
        else:
            os.system('clear')
            print('Nada a desfazer')
            print()
        ...    
    else: 
        lista_de_tarefas.append(opcao)
        salvar(lista_de_tarefas, CAMINHO_ARQUIVO)
        os.system('clear')      
        ...
