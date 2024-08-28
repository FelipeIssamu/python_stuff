
class Vec3:
    def __init__(self) -> None:
        pass


class Vec2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # def __add__(self, v):
    #     return self.x + v.x, self.y + v.y
    def pp(self):
        return print(self.x)

    def __add__(self, v):
        return Vec2(self.x + v.x, self.y + v.y)

    def add(self, v):
        self.x += v.x
        self.y += v.y
        return self

    def __repr__(self) -> str:
        return f'{self.x}, {self.y}'


v1 = Vec2(1, 3)
v2 = Vec2(1, 1)
v3 = Vec2(2, 2)
# v4 = v1 + v3
# print(v1 + v2)
# print(v4)
# print(v1)
# print(v3)
print(v1.add(v2).add(v3))


class cls:

    @classmethod
    def introduce(self):
        print(f'i am {self}')

    def introduceYourself(self):
        print(f'i am {self}')


class subCLS(cls):

    ...


cls.introduceYourself(subCLS)

subCLS.introduce()

Vec2.pp(v1)


# class Pessoa:
#     def __init__(self, nome, idade) -> None:
#         self.nome = nome
#         self.idade = idade


#     @property
#     def nome(self):
#         return self._nome

#     @nome.setter
#     def nome(self, nome):
#         self._nome = nome

#     def __repr__(self):
#         # classname = self.__class__.__name__
#         # attr = f'({self.nome=!r}, {self.idade=!r})'
#         # return f'{classname}{attr}'
#         return 'ola'


# p1 = Pessoa('felipe', 26)

# p1.nome = 'miguel'
# p1._nome = 'jandira'

# print(p1)


# lista = [2, 4, 5]
# lista2 = [3]

# lista += lista2

# print(lista)
