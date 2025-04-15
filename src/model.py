"""Definition of meta model 'model'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from types import String, Integer


name = 'model'
nsURI = 'http:///model.ecore'
nsPrefix = 'model'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class Pessoa(EObject, metaclass=MetaEClass):

    nome_completo = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    cpf = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    email = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    endereco = EReference(ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, nome_completo=None, cpf=None, email=None, endereco=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if nome_completo is not None:
            self.nome_completo = nome_completo

        if cpf is not None:
            self.cpf = cpf

        if email is not None:
            self.email = email

        if endereco is not None:
            self.endereco = endereco

    def cadastrarPessoa(self):

        raise NotImplementedError('operation cadastrarPessoa(...) not yet implemented')

    def excluirPessoa(self):

        raise NotImplementedError('operation excluirPessoa(...) not yet implemented')

    def atualizarPessoa(self):

        raise NotImplementedError('operation atualizarPessoa(...) not yet implemented')


class Endereco(EObject, metaclass=MetaEClass):

    id_endereco = EAttribute(eType=Integer, unique=True, derived=False, changeable=True)
    logradouro = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    bairro = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    n_predial = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    complemento = EAttribute(eType=String, unique=True, derived=False, changeable=True)

    def __init__(self, *, id_endereco=None, logradouro=None, bairro=None, n_predial=None, complemento=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id_endereco is not None:
            self.id_endereco = id_endereco

        if logradouro is not None:
            self.logradouro = logradouro

        if bairro is not None:
            self.bairro = bairro

        if n_predial is not None:
            self.n_predial = n_predial

        if complemento is not None:
            self.complemento = complemento

    def cadastarEndereco(self):

        raise NotImplementedError('operation cadastarEndereco(...) not yet implemented')

    def listarEndereco(self):

        raise NotImplementedError('operation listarEndereco(...) not yet implemented')

    def excluirEndereco(self):

        raise NotImplementedError('operation excluirEndereco(...) not yet implemented')

    def atualizarEndereco(self):

        raise NotImplementedError('operation atualizarEndereco(...) not yet implemented')


class Cargo(EObject, metaclass=MetaEClass):

    id_cargo = EAttribute(eType=Integer, unique=True, derived=False, changeable=True)
    nome_cargo = EAttribute(eType=String, unique=True, derived=False, changeable=True)

    def __init__(self, *, id_cargo=None, nome_cargo=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id_cargo is not None:
            self.id_cargo = id_cargo

        if nome_cargo is not None:
            self.nome_cargo = nome_cargo

    def cadastrarCargo(self):

        raise NotImplementedError('operation cadastrarCargo(...) not yet implemented')

    def listarCargo(self):

        raise NotImplementedError('operation listarCargo(...) not yet implemented')

    def excluirCargo(self):

        raise NotImplementedError('operation excluirCargo(...) not yet implemented')


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


class Produto(EObject, metaclass=MetaEClass):

    nome = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    id_produto = EAttribute(eType=Integer, unique=True, derived=False, changeable=True)
    preco = EAttribute(eType=EFloat, unique=True, derived=False, changeable=True)
    data_validade = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    data_entrada = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    quantidade = EAttribute(eType=Integer, unique=True, derived=False, changeable=True)
    fornecedor = EReference(ordered=False, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, nome=None, id_produto=None, preco=None, data_validade=None, data_entrada=None, quantidade=None, fornecedor=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if nome is not None:
            self.nome = nome

        if id_produto is not None:
            self.id_produto = id_produto

        if preco is not None:
            self.preco = preco

        if data_validade is not None:
            self.data_validade = data_validade

        if data_entrada is not None:
            self.data_entrada = data_entrada

        if quantidade is not None:
            self.quantidade = quantidade

        if fornecedor:
            self.fornecedor.extend(fornecedor)

    def cadastrarProduto(self):

        raise NotImplementedError('operation cadastrarProduto(...) not yet implemented')

    def listarProduto(self):

        raise NotImplementedError('operation listarProduto(...) not yet implemented')

    def excluirProduto(self):

        raise NotImplementedError('operation excluirProduto(...) not yet implemented')


class Fornecedor(EObject, metaclass=MetaEClass):

    razao_social = EAttribute(eType=String, unique=True, derived=False, changeable=True)
    cnpj = EAttribute(eType=Integer, unique=True, derived=False, changeable=True)

    def __init__(self, *, razao_social=None, cnpj=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if razao_social is not None:
            self.razao_social = razao_social

        if cnpj is not None:
            self.cnpj = cnpj

    def cadastrarFornecedor(self):

        raise NotImplementedError('operation cadastrarFornecedor(...) not yet implemented')

    def excluirFornecedor(self):

        raise NotImplementedError('operation excluirFornecedor(...) not yet implemented')

    def atualizarFornecedor(self):

        raise NotImplementedError('operation atualizarFornecedor(...) not yet implemented')


class Reserva(EObject, metaclass=MetaEClass):

    id_reserva = EAttribute(eType=Integer, unique=True, derived=False, changeable=True)
    cliente = EReference(ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, id_reserva=None, cliente=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id_reserva is not None:
            self.id_reserva = id_reserva

        if cliente is not None:
            self.cliente = cliente

    def realizarReserva(self):

        raise NotImplementedError('operation realizarReserva(...) not yet implemented')

    def cancelarReserva(self):

        raise NotImplementedError('operation cancelarReserva(...) not yet implemented')

    def atualizarDisponibilidade(self):

        raise NotImplementedError('operation atualizarDisponibilidade(...) not yet implemented')

    def confirmarReserva(self):

        raise NotImplementedError('operation confirmarReserva(...) not yet implemented')


class Pagamento(EObject, metaclass=MetaEClass):

    id_pagamento = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    forma_pagamento = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    valor_total = EReference(ordered=False, unique=True, containment=False, derived=False)
    id_pedido = EReference(ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, id_pagamento=None, valor_total=None, forma_pagamento=None, id_pedido=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id_pagamento is not None:
            self.id_pagamento = id_pagamento

        if forma_pagamento is not None:
            self.forma_pagamento = forma_pagamento

        if valor_total is not None:
            self.valor_total = valor_total

        if id_pedido is not None:
            self.id_pedido = id_pedido

    def finalizar_pagamento(self):

        raise NotImplementedError('operation finalizar_pagamento(...) not yet implemented')

    def fechar_pedido(self):

        raise NotImplementedError('operation fechar_pedido(...) not yet implemented')


class Funcionario(Pessoa):

    data_nascimento = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    data_admissao = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    cargo = EReference(ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, data_nascimento=None, cargo=None, data_admissao=None, **kwargs):

        super().__init__(**kwargs)

        if data_nascimento is not None:
            self.data_nascimento = data_nascimento

        if data_admissao is not None:
            self.data_admissao = data_admissao

        if cargo is not None:
            self.cargo = cargo

    def cadastrarFuncionario(self, nome_completo=None, cpf=None, email=None, logradouro=None, bairro=None, n_predial=None, complemento=None, data_nascimento=None):

        raise NotImplementedError('operation cadastrarFuncionario(...) not yet implemented')

    def listarFuncionario(self):

        raise NotImplementedError('operation listarFuncionario(...) not yet implemented')

    def excluirFuncionario(self):

        raise NotImplementedError('operation excluirFuncionario(...) not yet implemented')

    def atualizarFuncionario(self):

        raise NotImplementedError('operation atualizarFuncionario(...) not yet implemented')


class Cliente(Pessoa):

    id_cliente = EAttribute(eType=Integer, unique=True, derived=False, changeable=True)
    pedido = EReference(ordered=False, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, id_cliente=None, pedido=None, **kwargs):

        super().__init__(**kwargs)

        if id_cliente is not None:
            self.id_cliente = id_cliente

        if pedido:
            self.pedido.extend(pedido)

    def cadastrarCliente(self):

        raise NotImplementedError('operation cadastrarCliente(...) not yet implemented')

    def listarCliente(self):

        raise NotImplementedError('operation listarCliente(...) not yet implemented')

    def excluirCliente(self):

        raise NotImplementedError('operation excluirCliente(...) not yet implemented')
