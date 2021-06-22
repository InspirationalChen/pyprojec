import pytest


def func(x):
    return x + 1

@pytest.mark.login
def test_answer():
    assert func(4) == 5