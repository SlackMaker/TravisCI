import pytest
from principal import somar
from principal import subtrair

def test_somar():
    """docstring for test_somar"""
    assert somar(4,6) == 10
