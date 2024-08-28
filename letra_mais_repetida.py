frase = 'O Python é uma linguagem deprogramação multiparadigma. Python foi criado por Guido Van Rossum'
frase_lower = frase.lower()
if " " in frase_lower:
    frase_lower = frase_lower.replace(" ", "")
i = 0
contador = 0
letra_final =''
while i < len(frase_lower):
    letra = frase_lower[i]
    if contador < frase_lower.count(letra):
        contador = (frase_lower.count(letra))
        letra_final = letra
    i += 1
print(f'A letra que apareceu mais veses foi "{letra_final}" com "{contador}" duplicatas!')


