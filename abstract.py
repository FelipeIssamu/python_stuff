from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem


class NotificacaoEmail(Notificacao):
    def enviar(self):
        print(f'email: {self.mensagem}')
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self):
        print(f'email: {self.mensagem}')
        return False

# n = NotificacaoEmail('ola mundo')
# n.enviar()

# d = NotificacaoSMS('ola mundosss')
# d.enviar()


def notificar(notificacao: Notificacao):
    mensagem_enviada = notificacao.enviar()
    if mensagem_enviada:
        print('mensagem enviada')
    else:
        print('mensagem não enviada')


# n = NotificacaoEmail('ola mundo')
# notificar(n)
#
# d = NotificacaoSMS('ola mundosss')
# notificar(d)

for i in range(10):
    print(i)
