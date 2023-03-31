import pytest
from mxcurpy.states import States


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("aguascalientes", "AS"),
    ],
)
def test_get_code(test_input, expected):
    assert States.get_code(test_input) == expected
