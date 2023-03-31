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

from .utils import (
    get_first_vowel,
    clean_and_format_string,
    get_first_internal_consonant,
)
from .states import States
from .non_convenient_words import CURP_NON_CONVENIENT_WORDS


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
    parte numérica del CURP o RFC (son idénticas).

    ¿Deberíamos recibir la fecha en otro fomato o como fecha de Python?
    Este es un gran ejemplo de un lugar en el que no son necesarias las fechas
    con hora y mucho menos con zona horaria.
    """
    birth_date = birth_date.strip()
    parts = birth_date.split("-")
    day, month, year = parts[0], parts[1], parts[2]
    if len(day) < 2:
        day = "0" + day
    if len(month) < 2:
        month = "0" + month
    return f"{year[2:]}{month}{day}"


def _replace_exceptions_curp(curp):
    """Reemplaza las exceptiones de palabras no convenientes formadas
    por combinaciones de letras en el CURP"""
    return CURP_NON_CONVENIENT_WORDS.get(curp.upper(), curp)


def curp(
    names: str,
    lastname: str,
    second_lastname: str,
    birth_date: str,
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
        El nombre del estado como cadena, puedes ver una lista completa en la documentación.
    sex
        Es el sexo de la persona, acepta 'H' o 'h' para hombres y 'M' o 'm' para mujeres.
    Returns
    -------
    bool
        True if successful, False otherwise.
    """
    print(clean_and_format_string(lastname))
    alphabetic_chars = _generate_first_part(names, lastname, second_lastname)
    first_part = f"{_replace_exceptions_curp(alphabetic_chars)}{_generate_numeric_part(birth_date)}"

    if sex not in ("h", "H", "m", "M"):
        raise "Sex formatting is incorrect, must be an 'h' form men or a 'm' for women"

    # 1. Primera Consonante interna del apellido paterno
    # 2. Primera Consonante interna del apellido materno
    # 3. Primera Consonante interna del nombre
    state_code = States.get_code(birth_state)
    fic_last_name = get_first_internal_consonant(lastname)
    fic_second_last_name = get_first_internal_consonant(second_lastname)
    fic_name = get_first_internal_consonant(names)

    # Los últimos 2 caracteres son el dígito verificador, generados más o menos aleatoriamente al momento de la creación del CURP
    # por la entidad encargada de ello. No podemos calcularlos, por lo que devolvemos 00.

    return f"{first_part}{sex}{state_code}{fic_last_name}{fic_second_last_name}{fic_name}00".upper()
