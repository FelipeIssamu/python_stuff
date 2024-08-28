name = input('Digite seu nome: ')
if " " in name:
    name = name.replace(" ","")
tam_nome = len(name)
curto = (tam_nome >= 1) and (tam_nome <= 4)
normal = (tam_nome >= 5) and (tam_nome <= 6) 
grande = (tam_nome > 6)
if curto:
    print('Seu nome é curto')
elif normal:
    print('Seu nome é normal')
elif grande:
    print('Seu nome é grande')
