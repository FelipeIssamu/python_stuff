

class ListNode():
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


lista1 = [8,5,6]
lista2 = [8,4,3,2]

def somalista(l1, l2):
    intervalo = max(len(l1), len(l2))
    lista3 = [l1[i] + l2[i] for i in range(intervalo)]
    print(lista3)


somalista(lista1, lista2)




