from datetime import datetime, timedelta

parcela = 1_000_000 / 60
fmt = '%d/%m/%Y'
fpp = 2020
for j in range(1, 6):

    for i in range(1, 13):
        foo = i
        data_empr = datetime.strptime(f'20/{foo}/{fpp}', fmt)
        print(f'{data_empr}, {parcela:.2f}')
    fpp += 1

