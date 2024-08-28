from datetime import datetime
hora_atual = datetime.now()
bom_dia = (hora_atual.hour >= 0) and (hora_atual.hour <= 11)
boa_tarde = (hora_atual.hour >= 12) and (hora_atual.hour <= 17)
boa_noite = (hora_atual.hour >= 18) and (hora_atual.hour <= 23)
if bom_dia:
    print('Bom dia!')
elif boa_tarde:
    print('Boa tarde!')
elif boa_noite:
    print('Boa noite!')
