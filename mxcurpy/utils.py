from string import ascii_letters

LETTERS = set(ascii_letters)
ACCENTED_VOWELS = {"á": "a", "é": "e", "í": "i", "ó": "o", "ü": "u", "ú": "u", "ñ": "x"}
VOWELS = set(("a", "e", "i", "o", "u"))


def cleaned_string(function):
    """Decorador para asegurarnos de que las funciones que procesan cadenas trabajan sobre
    cadenas limpias y formateadas"""

    def wrapper(text):
        return function(clean_and_format_string(text))

    return wrapper


def replace_accented_char(letter):
    """Devuelve un carácter acentuado sin el acento"""
    return ACCENTED_VOWELS.get(letter, letter)


def clean_and_format_string(text):
    """Elimina símbolos, espacios y devuelve la cadena en minúsculas, todas las demás
    cadenas de este paquete dependen de recibir la función
    """
    text = text.lower()
    text = [replace_accented_char(c) for c in text]
    text = "".join([c for c in text if c in LETTERS])
    return text


@cleaned_string
def get_first_consonant(text):
    """Extrae la primera consonate de un texto"""
    for c in text:
        if c not in VOWELS:
            return c
    return ""


@cleaned_string
def get_first_vowel(text):
    """Extrae la primera vocal de una palabra"""
    for c in text:
        if c in VOWELS:
            return c
    return ""


@cleaned_string
def get_first_internal_consonant(text, default=""):
    """Extrae la primera consonante interna de una palabra"""
    for c in text[1:]:
        if c not in VOWELS:
            return c
    return default
