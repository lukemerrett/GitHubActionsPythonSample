import pytest


def add(x, y):
    return x + y


def divide(x, y):
    if y == 0:
        raise Exception("Cannot divide by zero")
    return x / y


def test_should_pass():
    assert add(1, 2) == 3


def test_should_throw():
    with pytest.raises(Exception):
        divide(1, 0)


class TestClass:
    def test_addition(self):
        assert add(3, 4) == 7
