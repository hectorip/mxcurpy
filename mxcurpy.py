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


def curp(names: str, lastname: str, second_lastname: str, brith_date: str, birth_state: str, sex: str) -> str:
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
    pass
