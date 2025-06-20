import os
import json
import pytest
from src.Endereco import Endereco

TEST_DB = 'enderecos_test.json'

@pytest.fixture(autouse=True)
def limpar_banco_json():
    # Remove o arquivo antes e depois de cada teste
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    yield
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

def test_cadastrar_endereco():
    e = Endereco(id_endereco=1, logradouro="Rua A", bairro="Centro", n_predial="123", complemento="Casa")
    e.DB_FILE = TEST_DB

    resultado = e.cadastarEndereco()
    assert resultado == "Endereço cadastrado com sucesso."

    with open(TEST_DB, 'r', encoding='utf-8') as f:
        dados = json.load(f)
        assert len(dados) == 1
        assert dados[0]['logradouro'] == "Rua A"

def test_cadastrar_id_duplicado():
    e1 = Endereco(id_endereco=1, logradouro="Rua A", bairro="Centro", n_predial="123", complemento="Casa")
    e2 = Endereco(id_endereco=1, logradouro="Rua B", bairro="Bairro B", n_predial="456", complemento="Ap")

    e1.DB_FILE = TEST_DB
    e2.DB_FILE = TEST_DB

    e1.cadastarEndereco()
    resultado = e2.cadastarEndereco()

    assert "Erro" in resultado

def test_listar_enderecos():
    e = Endereco(id_endereco=1, logradouro="Rua Teste", bairro="Teste", n_predial="1", complemento="")
    e.DB_FILE = TEST_DB
    e.cadastarEndereco()

    lista = e.listarEndereco()
    assert isinstance(lista, list)
    assert lista[0]['logradouro'] == "Rua Teste"

def test_excluir_endereco_existente():
    e = Endereco(id_endereco=1, logradouro="Rua A", bairro="Centro", n_predial="123", complemento="Casa")
    e.DB_FILE = TEST_DB
    e.cadastarEndereco()

    excluir = Endereco(id_endereco=1)
    excluir.DB_FILE = TEST_DB
    resultado = excluir.excluirEndereco()

    assert resultado == "Endereço com id 1 excluído com sucesso."
    assert excluir.listarEndereco() == []

def test_excluir_endereco_inexistente():
    e = Endereco(id_endereco=999)
    e.DB_FILE = TEST_DB
    resultado = e.excluirEndereco()
    assert resultado == "Nenhum endereço encontrado com id 999."

def test_atualizar_endereco_existente():
    e = Endereco(id_endereco=1, logradouro="Rua Antiga", bairro="Velho", n_predial="12", complemento="")
    e.DB_FILE = TEST_DB
    e.cadastarEndereco()

    atualiza = Endereco(id_endereco=1, logradouro="Rua Nova")
    atualiza.DB_FILE = TEST_DB
    resultado = atualiza.atualizarEndereco()

    assert resultado == "Endereço com id 1 atualizado com sucesso."

    dados = atualiza.listarEndereco()
    assert dados[0]['logradouro'] == "Rua Nova"
    assert dados[0]['bairro'] == "Velho"  # campo não alterado continua o mesmo

def test_atualizar_endereco_inexistente():
    e = Endereco(id_endereco=123, logradouro="Nova Rua")
    e.DB_FILE = TEST_DB
    resultado = e.atualizarEndereco()
    assert resultado == "Nenhum endereço encontrado com id 123."
