from calculator import add


def test_add():
    """Adding two positive integers returns their sum."""
    result = add(2, 3)
    assert result == 5


def test_add_zero():
    """Adding zero returns the other number."""
    result = add(5, 0)
    assert result == 5


def test_add_negative():
    """Adding a negative number returns the correct sum."""
    result = add(5, -3)
    assert result == 2