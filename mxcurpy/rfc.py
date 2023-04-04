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

from .utils import (
    get_first_internal_consonant,
)
from .states import States
from .non_convenient_words import CURP_NON_CONVENIENT_WORDS
from curp import _generate_first_part, _generate_numeric_part


def _replace_exceptions_rfc(curp):
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

    # Los últimos 2 caracteres son el dígito verificador, generados
    # más o menos aleatoriamente al momento de la creación del CURP
    # por la entidad encargada de ello. No podemos calcularlos,
    # por lo que devolvemos 00.

    return f"{first_part}{sex}{state_code}{fic_last_name}{fic_second_last_name}{fic_name}00".upper()
