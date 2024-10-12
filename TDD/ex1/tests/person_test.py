import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from person import Person
from emails import Email


# Verifica se o objeto Person está sendo inicializado corretamente
def test_person_initialization():
    person = Person(id=1, name="Júlia Gayotto", age=21, emails=[Email(1, "julia@gmail.com")])
    
    assert person.id == 1
    assert person.name == "Júlia Gayotto"
    assert person.age == 21
    assert len(person.emails) == 1
    assert person.emails[0].name == "julia@gmail.com"
