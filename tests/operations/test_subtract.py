from calculator import subtract


def test_subtract():
    """Subtraction returns the first number minus the second."""
    result = subtract(5, 3)
    assert result == 2


def test_subtract_negative_result():
    """Subtraction can return a negative result."""
    result = subtract(3, 5)
    assert result == -2


def test_subtract_zero():
    """Subtracting zero returns the original number."""
    result = subtract(7, 0)
    assert result == 7