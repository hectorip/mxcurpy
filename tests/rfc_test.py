import pytest

from mxcurpy.rfc import rfc


@pytest.mark.parametrize(
    "t_input,expected",
    (
        (
            (
                "Héctor Iván",
                "Patricio",
                "Moreno",
                "12-08-1989",
                "distrito federal",
                "h",
            ),
            "PAMH8908123G6",
        ),
        (
            (
                "Emma",
                "Gómez",
                "Díaz",
                "31-12-1956",
                "distrito federal",
                "h",
            ),
            "GODE561231GR8",
        ),
    ),
)
def test_rfc(t_input, expected):
    names, lastname, second_lastname, birth_date, state, sex = t_input
    assert rfc(names, lastname, second_lastname, birth_date) == expected
