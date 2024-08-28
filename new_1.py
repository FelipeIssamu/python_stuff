from collections import deque

lsitaDeque: deque[int] = deque()

lista = [3, 4, 5]

lsitaDeque.extend(lista)
lsitaDeque.append(3)
print(lsitaDeque)