import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from personDAO import PersonDAO
from person import Person
from emails import Email


@pytest.fixture
def dao():
    return PersonDAO()

def test_valid_person(dao):
    person = Person(id=1, name="Júlia Gayotto", age=21, emails=[Email(1, "julia@gmail.com")])
    errors = dao.isValidToInclude(person)
    assert len(errors) == 0

def test_invalid_name(dao):
    person = Person(id=1, name="Júlia", age=21, emails=[Email(1, "julia@gmail.com")])
    errors = dao.isValidToInclude(person)
    assert "O nome deve ser composto por ao menos 2 partes e deve possuir apenas letras." in errors

def test_invalid_name2(dao):
    person = Person(id=1, name="Júlia@", age=21, emails=[Email(1, "julia@gmail.com")])
    errors = dao.isValidToInclude(person)
    assert "O nome deve ser composto por ao menos 2 partes e deve possuir apenas letras." in errors

def test_invalid_age(dao):
    person = Person(id=1, name="Júlia Gayotto", age=300, emails=[Email(1, "julia@gmail.com")])
    errors = dao.isValidToInclude(person)
    assert "A idade deve estar entre 1 e 200." in errors

def test_missing_email(dao):
    person = Person(id=1, name="Júlia Gayotto", age=21, emails=[])
    errors = dao.isValidToInclude(person)
    assert "A pessoa deve ter pelo menos um email associado a ela." in errors

def test_invalid_email_format(dao):
    person = Person(id=1, name="Júlia Gayotto", age=21, emails=[Email(1, "juliagmail.com")])
    errors = dao.isValidToInclude(person)
    assert "O email juliagmail.com não está no formato válido ____@____.____." in errors

def test_totally_invalid_person(dao):
    person = Person(id=1, name="Júlia 1", age=300, emails=[Email(1, "juliagmail.com")])
    errors = dao.isValidToInclude(person)
    assert 'O nome deve ser composto por ao menos 2 partes e deve possuir apenas letras.' in errors
    assert 'A idade deve estar entre 1 e 200.' in errors
    assert 'O email juliagmail.com não está no formato válido ____@____.____.' in errors
