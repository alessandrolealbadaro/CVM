import os
import json
import pytest
from src.Cargo import Cargo

TEST_DB_FILE = 'test_cargos.json'

@pytest.fixture(autouse=True)
def limpar_arquivo_json():
    if os.path.exists(TEST_DB_FILE):
        os.remove(TEST_DB_FILE)
    yield
    if os.path.exists(TEST_DB_FILE):
        os.remove(TEST_DB_FILE)

def test_cadastrar_novo_cargo():
    cargo = Cargo(id_cargo=1, nome_cargo="Cozinheiro")
    cargo.DB_FILE = TEST_DB_FILE

    resultado = cargo.cadastrarCargo()
    assert resultado == "Cargo 'Cozinheiro' cadastrado com sucesso."

    # Verifica se foi salvo no arquivo
    with open(TEST_DB_FILE, 'r', encoding='utf-8') as f:
        dados = json.load(f)
        assert len(dados) == 1
        assert dados[0]['nome_cargo'] == "Cozinheiro"

def test_nao_permitir_id_duplicado():
    cargo1 = Cargo(id_cargo=2, nome_cargo="Garçom")
    cargo2 = Cargo(id_cargo=2, nome_cargo="Atendente")

    cargo1.DB_FILE = TEST_DB_FILE
    cargo2.DB_FILE = TEST_DB_FILE

    assert cargo1.cadastrarCargo() == "Cargo 'Garçom' cadastrado com sucesso."
    assert "Erro" in cargo2.cadastrarCargo()

def test_listar_cargos():
    cargo1 = Cargo(id_cargo=3, nome_cargo="Caixa")
    cargo1.DB_FILE = TEST_DB_FILE
    cargo1.cadastrarCargo()

    cargo2 = Cargo(id_cargo=4, nome_cargo="Gerente")
    cargo2.DB_FILE = TEST_DB_FILE
    cargo2.cadastrarCargo()

    cargos = cargo1.listarCargo()
    assert len(cargos) == 2
    assert cargos[0]['nome_cargo'] == "Caixa"
    assert cargos[1]['nome_cargo'] == "Gerente"

def test_excluir_cargo_existente():
    cargo = Cargo(id_cargo=5, nome_cargo="Auxiliar")
    cargo.DB_FILE = TEST_DB_FILE
    cargo.cadastrarCargo()

    excluir = Cargo(id_cargo=5)
    excluir.DB_FILE = TEST_DB_FILE
    resultado = excluir.excluirCargo()

    assert resultado == "Cargo com id 5 excluído com sucesso."
    assert excluir.listarCargo() == []

def test_excluir_cargo_inexistente():
    cargo = Cargo(id_cargo=99)
    cargo.DB_FILE = TEST_DB_FILE
    resultado = cargo.excluirCargo()

    assert resultado == "Nenhum cargo encontrado com id 99."