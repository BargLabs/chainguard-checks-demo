import pytest

from calc import add, mean


def test_add():
    assert add(2, 3) == 5


def test_mean():
    assert mean([1.0, 2.0, 3.0]) == 2.0


def test_mean_empty():
    with pytest.raises(ValueError):
        mean([])
