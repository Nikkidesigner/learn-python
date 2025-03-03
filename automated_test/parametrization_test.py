import pytest
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (5, 5, 10),
    (-1, 1, 0),
    (1, 2, 3)
])
def test_add(a, b, expected):
    assert a + b == expected  # Runs the test with different values
