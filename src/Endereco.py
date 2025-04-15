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