import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from employee import Employee
from calculator import Calculator

# Developer
def test_high_salary_developer():
    employee = Employee(id=1, name="Júlia Gayotto", email="julia@gmail.com", base_salary=3001.50, position='DESENVOLVEDOR')
    calculator = Calculator()
    net_salary = calculator.calculate(employee)
    assert net_salary == 3001.50 * 0.8

def test_developer_salary_equal_to_3000():
    employee = Employee(id=2, name="João Sousa", email="joao@gmail.com", base_salary=3000, position='DESENVOLVEDOR')
    calculator = Calculator()
    net_salary = calculator.calculate(employee)
    assert net_salary == 3000 * 0.8

def test_low_salary_developer():
    employee = Employee(id=3, name="Lucas Silva", email="lucas@gmail.com", base_salary=2000, position='DESENVOLVEDOR')
    calculator = Calculator()
    net_salary = calculator.calculate(employee)
    assert net_salary == 2000 * 0.9

#--------------------------------------------------------------

# DBA
def test_high_salary_DBA():
    employee = Employee(id=4, name="Lara Santos", email="lara@gmail.com", base_salary=2005.50, position='DBA')
    calculator = Calculator()
    net_salary = calculator.calculate(employee)
    assert net_salary == 2005.50 * 0.75

def test_DBA_salary_equal_to_2000():
    employee = Employee(id=5, name="Bruno Alves", email="bruno@gmail.com", base_salary=2000, position='DBA')
    calculator = Calculator()
    net_salary = calculator.calculate(employee)
    assert net_salary == 2000 * 0.75

def test_low_salary_DBA():
    employee = Employee(id=6, name="Leonardo Oliveira", email="leornardo@gmail.com", base_salary=1900.50, position='DBA')
    calculator = Calculator()
    net_salary = calculator.calculate(employee)
    assert net_salary == 1900.50 * 0.85

#--------------------------------------------------------------

# TESTADOR
def test_high_salary_testador():
    employee = Employee(id=7, name="Mariana Costa", email="mariana@gmail.com", base_salary=2003, position='TESTADOR')
    calculator = Calculator()
    net_salary = calculator.calculate(employee)
    assert net_salary == 2003 * 0.75

def test_testador_salary_equal_to_2000():
    employee = Employee(id=8, name="Pedro Almeida", email="pedro@gmail.com", base_salary=2000.00, position='TESTADOR')
    calculator = Calculator()
    net_salary = calculator.calculate(employee)
    assert net_salary == 2000 * 0.75

def test_low_salary_testador():
    employee = Employee(id=9, name="Ana Martins", email="ana@gmail.com", base_salary=1950.30, position='TESTADOR')
    calculator = Calculator()
    net_salary = calculator.calculate(employee)
    assert net_salary == 1950.30 * 0.85

#-------------------------------------------------------------

# GERENTE
def test_high_salary_gerente():
    employee = Employee(id=10, name="Bruna Carvalho", email="bruna@gmail.com", base_salary=5100.20, position='GERENTE')
    calculator = Calculator()
    net_salary = calculator.calculate(employee)
    assert net_salary == 5100.20 * 0.70

def test_gerente_salary_equal_to_5000():
    employee = Employee(id=11, name="Felipe Mendes", email="felipe@gmail.com", base_salary=5000.00, position='GERENTE')
    calculator = Calculator()
    net_salary = calculator.calculate(employee)
    assert net_salary == 5000 * 0.70

def test_low_salary_gerente():
    employee = Employee(id=12, name="Isabela Ferreira", email="isabela@gmail.com", base_salary=4850.30, position='GERENTE')
    calculator = Calculator()
    net_salary = calculator.calculate(employee)
    assert net_salary == 4850.30 * 0.80
