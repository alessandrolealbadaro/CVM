import pyecore.ecore as Ecore
from pyecore.ecore import *
from types import String, Integer

class Pedido(EObject, metaclass=MetaEClass):

    hora_pedido = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    id_pedido = EAttribute(eType=Integer, unique=True, derived=False, changeable=True)
    valor_total = EAttribute(eType=EFloat, unique=True, derived=False, changeable=True)
    cliente = EReference(ordered=False, unique=True, containment=False, derived=False)
    endereco = EReference(ordered=False, unique=True, containment=False, derived=False)
    produto = EReference(ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, hora_pedido=None, id_pedido=None, cliente=None, endereco=None, valor_total=None, produto=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if hora_pedido is not None:
            self.hora_pedido = hora_pedido

        if id_pedido is not None:
            self.id_pedido = id_pedido

        if valor_total is not None:
            self.valor_total = valor_total

        if cliente is not None:
            self.cliente = cliente

        if endereco is not None:
            self.endereco = endereco

        if produto is not None:
            self.produto = produto

    def cadastrarPedido(self):

        raise NotImplementedError('operation cadastrarPedido(...) not yet implemented')

    def listarPedido(self):

        raise NotImplementedError('operation listarPedido(...) not yet implemented')

    def cancelarPedido(self):

        raise NotImplementedError('operation cancelarPedido(...) not yet implemented')

    def realizarEntrega(self):

        raise NotImplementedError('operation realizarEntrega(...) not yet implemented')

    def realizarPagamento(self):

        raise NotImplementedError('operation realizarPagamento(...) not yet implemented')

    def calcularTotal(self):

        raise NotImplementedError('operation calcularTotal(...) not yet implemented')