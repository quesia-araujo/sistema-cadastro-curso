from datetime import date
from model_bakery import baker
from cursos.models import Curso
from base.models import Cadastro
import pytest

@pytest.fixture
def curso():
    curso = baker.make(
        Curso,
        titulo = 'Java',
        data_do_curso = date.today(),
        carga_horaria = '40'
    )
    return curso

@pytest.fixture
def cadastro():
    cadastro = baker.make(
        Cadastro,
        nome = 'Quesia',
        email= 'email@gmail.com',
        senha = '123456',
        data = date.today()
    )
    return cadastro


@pytest.mark.django_db # acesso ao banco de dados
def test_str_deve_retornar_string(curso):
    assert str(curso) == 'Java: 2024-03-12 - 40' # Data do dia atual


@pytest.mark.django_db # acesso ao banco de dados
def test_cadastro_str_deve_retornar_string(cadastro):
    assert str(cadastro) == 'Quesia [email@gmail.com]'
#def test_config():
#   assert 1==1
