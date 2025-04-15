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