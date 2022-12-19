"""MXCURPY

Esta biblioteca te ayudará a calcular el CURP (Clave Única de Registro de
Población de México) y el RFC (Registro Federal de Conritbuyente).

Notas
----
Los únicos datos que no podemos calcular son el dígito
verificador del CURP porque es asignado durante la primera creación del CURP en
la entidad encargada de ello.

El cálculo de la homoclave sigue el algoritmo oficial pero en algunas ocasiones
este dato puede ser diferente al oficial.

"""

from utilities import (
    cleaned_string,
    get_first_consonant,
    get_first_vowel,
    clean_and_format_string,
)


def _generate_first_part(names, lastname, second_lastname=""):

    # Puede que algunos usuarios no tengan segundo apellido, y se tiene que usar una X
    # Ponemos la "x" para extraerla como primera letra

    if not second_lastname:
        second_lastname = "x"
    return clean_and_format_string(
        f"{lastname[0]}{get_first_vowel(lastname)}{second_lastname[0]}{names[0]}"
    )


def _generate_numeric_part(birth_date):
    """Recibe la fecha de nacimiento como cadena y la transforma en la
    parte numérica del CURP o RFC (en este caso son idénticas)"""
    birth_date = birth_date.strip()
    parts = birth_date.split("-")
    day, month, year = parts[0], parts[1], parts[2]
    if len(day) < 2:
        day = "0" + day
    if len(month) < 2:
        month = "0" + month
    return f"{year[2:]}{month}{day}"


def _generate_common_part(names, lastname, second_lastname="", birth_date=""):
    """Genera la parte común del CURP y del RFC es decir, la compuesta por el nombre
    completo y la fecha de nacimiento"""
    return f"{_generate_first_part(names, lastname, second_lastname)}{_generate_numeric_part(birth_date)}"


def curp(
    names: str,
    lastname: str,
    second_lastname: str,
    brith_date: str,
    birth_state: str,
    sex: str,
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
        Es el código del estado de nacimiento de la persona. La lista de códigos aceptados la
        puedes sacar de aquí: TODO: Falta la lista oficial de códigos de estados.
    sex
        Es el sexo de la persona, acepta 'H' o 'h' para hombres y 'M' o 'm' para mujeres.
    Returns
    -------
    bool
        True if successful, False otherwise.
    """
    first_half = _generate_common_part(names, lastname, second_lastname, birth_date)
    if sex not in ("h", "H", "m", "n"):
        raise "Sex formatting is incorrect, must be an 'h' form men or a 'm' for women"
    second_half = f"{sex}"
