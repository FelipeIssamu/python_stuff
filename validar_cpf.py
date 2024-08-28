cpf = input('Digite seu cpf: ')

if '-' in cpf:
    cpf = cpf.replace('-', '')
if '.' in cpf:
    cpf = cpf.replace('.', '')
somatoria = 0
somatoria2 = 0
digito1 = 0

for i, num in enumerate(cpf,-10):
    if i <= -2:
        somatoria += int(num)*-i
        print(i, num)
        print()
    
digito1 = ((somatoria*10)%11)
digito1 = 0 if digito1 > 9 else digito1
print(digito1)

cpf1 = cpf[:9]
cpf1 += str(digito1)
for i, num in enumerate(cpf1,-11):
    if i <= -2:
        somatoria2 += int(num)*-i
        print(i, num)
        print()

digito2 = (somatoria2*10)%11
digito2 = 0 if digito2 > 9 else digito2
cpf1 += str(digito2)
print(digito2)
print(cpf)
print(cpf1)

if cpf == cpf1:
    print('cpf valido')
else:
    print('cpf invalido')
# if (str(digito1) == cpf[9]) and (str(digito2) == cpf[10]):
#     print('Cpf valido!')
# else:
#     print('Cpf invalido!')


