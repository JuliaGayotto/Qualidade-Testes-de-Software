import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from employee import Employee


# Verifica se o objeto Employee está sendo inicializado corretamente
def test_person_initialization():
    employee = Employee(id=1, name="Júlia Gayotto", email="julia@gmail.com", base_salary=3001.50, position="DESENVOLVEDOR")
    
    assert employee.id == 1
    assert employee.name == "Júlia Gayotto"
    assert employee.email == "julia@gmail.com"
    assert employee.base_salary == 3001.50
    assert employee.position == "DESENVOLVEDOR"