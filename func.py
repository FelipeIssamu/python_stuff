def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def parimpar(x):
    return 'par' if x % 2 == 0 else 'impar'

