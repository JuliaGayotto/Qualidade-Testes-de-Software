import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from emails import Email


# Verifica se o objeto Email está sendo inicializado corretamente
def test_email_initialization():
    email = Email(id=1, name="julia@gmail.com")
    
    assert email.id == 1
    assert email.name == "julia@gmail.com"
