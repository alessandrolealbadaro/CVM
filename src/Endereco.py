import json
import os

class Endereco:
    DB_FILE = 'enderecos.json'

    def __init__(self, *, id_endereco=None, logradouro=None, bairro=None, n_predial=None, complemento=None):
        self.id_endereco = id_endereco
        self.logradouro = logradouro
        self.bairro = bairro
        self.n_predial = n_predial
        self.complemento = complemento

    def CarregarDados(self):
        if not os.path.exists(self.DB_FILE):
            return []

        with open(self.DB_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def SalvarDados(self, dados):
        with open(self.DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def cadastarEndereco(self):

        dados = self.CarregarDados()

        for end in dados:
            if end['id_endereco'] == self.id_endereco:
                return f"Erro: Já existe um endereço com id {self.id_endereco}."

        novo_endereco = {
            "id_endereco": self.id_endereco,
            "logradouro": self.logradouro,
            "bairro": self.bairro,
            "n_predial": self.n_predial,
            "complemento": self.complemento
        }

        dados.append(novo_endereco)
        self.SalvarDados(dados)
        return f"Endereço cadastrado com sucesso."

    def listarEndereco(self):

        dados = self.CarregarDados()
        return dados

    def excluirEndereco(self):

        dados = self.CarregarDados()
        novo_dados = [end for end in dados if end['id_endereco'] != self.id_endereco]

        if len(novo_dados) == len(dados):
            return f"Nenhum endereço encontrado com id {self.id_endereco}."

        self.SalvarDados(novo_dados)
        return f"Endereço com id {self.id_endereco} excluído com sucesso."

    def atualizarEndereco(self):

        dados = self.CarregarDados()
        atualizado = False

        for end in dados:
            if end['id_endereco'] == self.id_endereco:
                end['logradouro'] = self.logradouro or end['logradouro']
                end['bairro'] = self.bairro or end['bairro']
                end['n_predial'] = self.n_predial or end['n_predial']
                end['complemento'] = self.complemento or end['complemento']
                atualizado = True
                break

        if not atualizado:
            return f"Nenhum endereço encontrado com id {self.id_endereco}."

        self.SalvarDados(dados)
        return f"Endereço com id {self.id_endereco} atualizado com sucesso."