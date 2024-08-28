"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Cliente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numeroconta, saldo):
        self._agencia = agencia
        self._numero_conta = numeroconta
        self.saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia

    @property
    def numeroConta(self):
        return self._numero_conta

    @numeroConta.setter
    def numeroConta(self, numeroconta):
        self._numero_conta = numeroconta

    @abstractmethod
    def sacar(self, valor):
        ...

    @abstractmethod
    def depositar(self, valor):
        ...
    ...


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade
    ...


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta_corrente = [1, 2, 3]
        self._conta_poupança = []
    ...


class ContaCorrente(Conta):

    def __init__(self, agencia, numeroconta, saldo, limite):
        super().__init__(agencia, numeroconta, saldo)
        self.limite = limite

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError('Valor indisponível')
        if self.saldo > 0 and valor <= self.saldo:
            self.saldo -= valor
            return valor
        if self.saldo == 0:
            if self.limite > 0 and valor <= self.limite:
                self.limite -= valor
                return valor

    def depositar(self, valor):
        self.saldo += valor
        return True

    ...


class ContaPoupança(Conta):

    def sacar(self, valor):

        if valor < 0:
            raise ValueError('Valor indisponível')
        if valor > 0 and self.saldo > 0 and valor <= self.saldo:
            self.saldo -= valor
            return valor

    def depositar(self, valor):
        self.saldo += valor
        return True
    ...


class Banco():
    def __init__(self, nome):
        self._nomebanco = nome
        self._clientes = []
        self._contas = []

    @property
    def nomebanco(self):
        return self._nomebanco

    @nomebanco.setter
    def nomebanco(self, nomebanco):
        self._nomebanco = nomebanco

    ...

# cli = Cliente('felipe', 26)
# print(cli._conta_corrente)


conta1 = ContaCorrente('34426', '51560', 10, 5)
conta2 = ContaPoupança('34426', '51560', 0)
valor = conta2.depositar(500)
# conta1.depositar(10)

valor2 = conta1.sacar(6)
print(conta1.saldo, conta1.limite, valor, valor2)
