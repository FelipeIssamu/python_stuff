

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)


def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)


dict = {
    'odd': is_odd,
    'flti': 59,
    'felipee': 34,
}

# print('hello world')
# print(dict)

list = [1, 3, 5, 67, 5]

lista2 = [
        i*0.5 for i in list
        if i > 50
    ]

print(dict['odd'](2))
