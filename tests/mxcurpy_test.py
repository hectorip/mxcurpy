import pytest
from utilities import (
    clean_and_format_string,
    replace_accented_char,
    get_first_consonant,
    get_first_vowel,
)
from mxcurpy import _generate_first_part, _generate_numeric_part, _generate_common_part


@pytest.mark.parametrize("t_input,expected", (("á", "a"), ("é", "e"), ("ü", "u")))
def test_remove_accent(t_input, expected):
    assert replace_accented_char(t_input) == expected


def test_clean_string():
    names = ["Héctor", "Iván", " Patricio ", "Moreno3"]
    results = ["hector", "ivan", "patricio", "moreno"]
    for n, r in zip(names, results):
        assert clean_and_format_string(n) == r


@pytest.mark.parametrize(
    "t_input, expected",
    (
        ("Héctor", "h"),
        ("Iván", "v"),
        ("aei", ""),
        ("", ""),
    ),
)
def test_extract_first_consonant(t_input, expected):
    assert get_first_consonant(t_input) == expected


@pytest.mark.parametrize(
    "t_input, expected",
    (
        ("Héctor", "e"),
        ("Iván", "i"),
        ("CDFG", ""),
        ("", ""),
    ),
)
def test_extract_first_vowel(t_input, expected):
    assert get_first_vowel(t_input) == expected


@pytest.mark.parametrize(
    "t_input,expected",
    (
        (("Héctor Iván", "Patricio", "Moreno"), "pamh"),
        (("Armando", "Palermo", "Torres"), "pata"),
        (("Héctor Iván", "Patricio", ""), "paxh"),
    ),
)
def test_generate_first_part(t_input, expected):
    names, lastname, second_lastname = t_input
    assert _generate_first_part(names, lastname, second_lastname) == expected


@pytest.mark.parametrize(
    "t_input,expected",
    (
        ("12-08-1989", "890812"),
        ("25-11-1988", "881125"),
        ("05-05-1986", "860505"),
    ),
)
def test_generate_numeric_part(t_input, expected):
    assert _generate_numeric_part(t_input) == expected


@pytest.mark.parametrize(
    "t_input,expected",
    (
        (("Héctor Iván", "Patricio", "Moreno", "12-08-1989"), "pamh890812"),
        (("Armando", "Palermo", "Torres", "12-12-1936"), "pata361212"),
    ),
)
def test_generate_common_part(t_input, expected):
    names, lastname, second_lastname, birth_date = t_input
    assert (
        _generate_common_part(names, lastname, second_lastname, birth_date) == expected
    )
