import json
import os

class Cargo():
    DB_FILE = 'cargos.json'
    id_cargo = None
    nome_cargo = None

    def __init__(self, *, id_cargo=None, nome_cargo=None):
        super().__init__()

        if id_cargo is not None:
            self.id_cargo = id_cargo

        if nome_cargo is not None:
            self.nome_cargo = nome_cargo

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

    def cadastrarCargo(self):

        dados = self.CarregarDados()

        # Verifica se o ID já existe
        for cargo in dados:
            if cargo['id_cargo'] == self.id_cargo:
                return f"Erro: Já existe um cargo com o id {self.id_cargo}."

        novo_cargo = {
            "id_cargo": self.id_cargo,
            "nome_cargo": self.nome_cargo
        }

        dados.append(novo_cargo)
        self.SalvarDados(dados)

        return f"Cargo '{self.nome_cargo}' cadastrado com sucesso."

    def listarCargo(self):
        dados = self.CarregarDados()
        return dados

    def excluirCargo(self):
        dados = self.CarregarDados()
        novo_dados = [cargo for cargo in dados if cargo['id_cargo'] != self.id_cargo]

        if len(novo_dados) == len(dados):
            return f"Nenhum cargo encontrado com id {self.id_cargo}."

        self.SalvarDados(novo_dados)
        return f"Cargo com id {self.id_cargo} excluído com sucesso."