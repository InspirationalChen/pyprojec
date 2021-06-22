import pytest


def func(x):
    return x + 1

@pytest.mark.search
def test_answer():
    assert func(3) == 4