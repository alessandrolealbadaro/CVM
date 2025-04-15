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

