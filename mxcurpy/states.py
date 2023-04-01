from .utils import replace_accented_char


class States:
    """A class to store all States of the country and help retrieve the code easily"""

    STATES = {
        "AGUASCALIENTES": ("AS",),
        "BAJA CALIFORNIA": ("BC",),
        "BAJA CALIFORNIA SUR": ("BS",),
        "CAMPECHE": ("CC",),
        "COAHUILA": ("CS",),
        "COLIMA": ("CL",),
        "CHIAPAS": ("CM",),
        "CHIHUAHUA": ("CH",),
        "DISTRITO FEDERAL": ("DF",),
        "CDMX": ("DF",),
        "CIUDAD DE MEXICO": ("DF",),
        "DURANGO": ("DG",),
        "GUANAJUATO": ("GT",),
        "GUERRERO": ("GR",),
        "HIDALGO": ("HG",),
        "JALISCO": ("JC",),
        "MEXICO": ("MC",),
        "MICHOACAN": ("MN",),
        "MORELOS": ("MS",),
        "NAYARIT": ("NT",),
        "NUEVO LEON": ("NL",),
        "OAXACA": ("OC",),
        "PUEBLA": ("PL",),
        "QUERETARO": ("QT",),
        "QUINTANA ROO": ("QR",),
        "SAN LUIS POTOSI": ("SP",),
        "SINALOA": ("SL",),
        "SONORA": ("SR",),
        "TABASCO": ("TC",),
        "TAMAULIPAS": ("TS",),
        "TLAXCALA": ("TL",),
        "VERACRUZ": ("VZ",),
        "YUCATAN": ("YN",),
        "ZACATECAS": ("ZS",),
        "NACIDO EN EL EXTRANJERO": ("NE",),
    }

    @staticmethod
    def get_code(state):
        """Get the code of a state"""
        state = state.lower().strip()
        state = [replace_accented_char(c) for c in state]
        state = "".join(state).upper()
        return States.STATES[state][0]

    @staticmethod
    def get_state(code):
        """Get the state from a code"""
        for state, codes in States.STATES.items():
            if code in codes:
                return state
