"""RFC

Esta biblioteca te ayudará a calcular el CURP (Clave Única de Registro de
Población de México) y el RFC (Registro Federal de Conritbuyente).

Notas
----
El cálculo de la homclave sigue un algoritmo que se encontró en un documento de 2006,
ya que no se encontró un documento oficial más reciente y todas las
fuentes mencionan que la forma de obtner la homoclave es consultar al Servicio de
Administración Tributaria (SAT).


"""

from .curp import _generate_first_part, _generate_numeric_part
from .non_convenient_words import RFC_NON_CONVENIENT_WORDS
from .utils import clean_and_format_string

_mapping_table = {
    " ": "00",
    "0": "00",
    "1": "01",
    "2": "02",
    "3": "03",
    "4": "04",
    "5": "05",
    "6": "06",
    "7": "07",
    "8": "08",
    "9": "09",
    "&": "10",
    "A": "11",
    "B": "12",
    "C": "13",
    "D": "14",
    "E": "15",
    "F": "16",
    "G": "17",
    "H": "18",
    "I": "19",
    "J": "21",
    "K": "22",
    "L": "23",
    "M": "24",
    "N": "25",
    "O": "26",
    "P": "27",
    "Q": "28",
    "R": "29",
    "S": "32",
    "T": "33",
    "U": "34",
    "V": "35",
    "W": "36",
    "X": "37",
    "Y": "38",
    "Z": "39",
    "Ñ": "40",
}

_verification_number_mapping = {
    "0": "00",
    "1": "01",
    "2": "02",
    "3": "03",
    "4": "04",
    "5": "05",
    "6": "06",
    "7": "07",
    "8": "08",
    "9": "09",
    "A": "10",
    "B": "11",
    "C": "12",
    "D": "13",
    "E": "14",
    "F": "15",
    "G": "16",
    "H": "17",
    "I": "18",
    "J": "19",
    "K": "20",
    "L": "21",
    "M": "22",
    "N": "23",
    "&": "24",
    "O": "25",
    "P": "26",
    "Q": "27",
    "R": "28",
    "S": "29",
    "T": "30",
    "U": "31",
    "V": "32",
    "W": "33",
    "X": "34",
    "Y": "35",
    "Z": "36",
    " ": "37",
    "Ñ": "38",
}


def _replace_exceptions_rfc(rfc):
    """Reemplaza las exceptiones de palabras no convenientes formadas
    por combinaciones de letras en el CURP"""
    return RFC_NON_CONVENIENT_WORDS.get(rfc.upper(), rfc)


def _get_diff_key(name, lastname, second_lastname, mapping_table=_mapping_table):
    """Calcula las letras de la homoclave del RFC"""
    name = name.upper()
    lastname = lastname.upper()
    second_lastname = second_lastname.upper()
    print("NAME", " ".join([name, lastname, second_lastname]))
    calc_string = "0"
    for letter in " ".join([name, lastname, second_lastname]):
        calc_string += mapping_table[letter]
    # Operando por pares
    from itertools import pairwise

    pairwise_sum = 0
    for pair in pairwise(calc_string):
        pairwise_sum += int("".join(pair)) * int(pair[1])
        print("pair", pair, "mult", int("".join(pair)) * int(pair[1]))
    print("pairwise_sum", pairwise_sum)

    three_last_digits = pairwise_sum % 1000
    magic_factor = 34
    quotient = three_last_digits // magic_factor
    modulus = three_last_digits % magic_factor
    homo_keys = "123456789ABCDEFGHIJKLMNPQRSTUVWXYZ"
    return f"{homo_keys[quotient]}{homo_keys[modulus]}"


def _get_verification_digit(rfc, mapping_table=_verification_number_mapping):
    """
    Calcula el tercer dígito de la homoclave
    """
    rfc = rfc.upper()
    total = 0
    position = 13

    for letter in rfc:
        total += int(mapping_table[letter]) * position
        print("mult", (mapping_table[letter]), position)
        position -= 1
    print("Verification digit", total)
    modulus = total % 11
    if modulus == 0:
        return modulus
    else:
        result = 11 - modulus
        return result if result < 10 else "A"


def rfc(
    names: str,
    lastname: str,
    second_lastname: str,
    birth_date: str,
):
    """Devuelve el CURP bien formado usando los datos básicos.
    Nota: el dígito verificador no es correcto porque es asignado al momento de
    creación y registro del curp por una entidad nacional.

    Parámetros
    ----------
    names
        Es el nombre o nombres de pila de la persona.
    lastname
        Es el primer apellido (apellido paterno) de la persona.
    second_lastname
        Es el segundo apellido (apellido materno) de la persona.
    birth_date
        Es la fecha de nacimiento de la persona en formato "dd-MM-yyyy", por ejemplo "27-01-1980"
    birth_state
        El nombre del estado como cadena, puedes ver una lista completa en la documentación.
    sex
        Es el sexo de la persona, acepta 'H' o 'h' para hombres y 'M' o 'm' para mujeres.
    Returns
    -------
    bool
        True if successful, False otherwise.
    """
    names = clean_and_format_string(names, preserve_spaces=True)
    lastname = clean_and_format_string(lastname, preserve_spaces=True)
    second_lastname = clean_and_format_string(second_lastname, preserve_spaces=True)

    alphabetic_chars = _generate_first_part(names, lastname, second_lastname)
    first_part = f"{_replace_exceptions_rfc(alphabetic_chars)}{_generate_numeric_part(birth_date)}"

    diff_key = _get_diff_key(names, lastname, second_lastname)
    verification_number = _get_verification_digit(first_part + diff_key)
    return f"{first_part}{diff_key}{verification_number}".upper()
