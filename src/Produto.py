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
