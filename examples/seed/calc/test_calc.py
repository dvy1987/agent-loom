from calc import add, divide
import pytest


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5.0


def test_divide_by_zero_raises_explicit_message():
    """Fails until divide() adds an explicit guard with this message."""
    with pytest.raises(ZeroDivisionError, match="divisor must be non-zero"):
        divide(1, 0)
