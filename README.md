# MXCurpy

Generación de Clave Única de Registro de Población y el Registro Federal de Contibuyentes de México en Python.

Documentos en los que está basado este paquete:

**CURP**: [INSTRUCTIVO NORMATIVO PARA LA ASIGNACIÓN DE LA CLAVE ÚNICA DE REGISTRO DE
POBLACIÓN](/docs/dof18102021.pdf)

**RFC**: [Instructivo RFC-2006](/docs/RFC-2006.pdf). Este es un instructivo antiguo, del 2006, ya que no he encontrado documentos más recientes públicos, pero estoy investigando si hay algún documento normativo que se pueda conseguir. Digamos que el método oficial para conseguir el RFC es siempre preguntándole al Sistema de Administración Tributaria (SAT), también según los documentos oficiales.

## Estado actual del proyecto

Se puede generar tanto CURP como RFC, pero no se ha probado mucho, por lo que no se puede garantizar que funcione en todos los casos.

## Uso

Generación de CURP:

```python
from mxcurpy.curp import curp

my_curp = curp(names="Juan José", lastname="Martínez", second_lastname="Pérez", birth_date="12-08-1989", birth_state="Durango", sex="h")

# MAPJ890812HDGRRN00

```

Generación de RFC:

```python
from mxcurpy.rfc import rfc

my_rfc = rfc(
                "Emma",
                "Gómez",
                "Díaz",
                "31-12-1956"
            )
# GODE561231GR8
```

## Casos excepcionales

Si la persona es nacida en el extranjero, mandar la cadena `"NACIDO EN EL EXTRANJERO"` como estado de nacimiento.

## Limitaciones

Aquí describimos algunas limitaciones que tenemos y que probablemente no se arreglen en un futuro cercano (ni lejano).

### CURP

Los dod últimos carácteres al final de la CURP oficial son generados por la entidad de gobierno encargada de asignación de las curps al momento de genrarla, con el objetivo de
evitar duplicados, por lo que no podemos generarlos con seguridad, por eso estos dos carácteres siempre serán `00`.

## Lista de estados válidos

Estados:

* "AGUASCALIENTES"
* "BAJA CALIFORNIA"
* "BAJA CALIFORNIA SUR"
* "CAMPECHE"
* "COAHUILA"
* "COLIMA"
* "CHIAPAS"
* "CHIHUAHUA"
* "DISTRITO FEDERAL"
* "CDMX"
* "CIUDAD DE MEXICO"
* "DURANGO"
* "GUANAJUATO"
* "GUERRERO"
* "HIDALGO"
* "JALISCO"
* "MEXICO"
* "MICHOACAN"
* "MORELOS"
* "NAYARIT"
* "NUEVO LEON"
* "OAXACA"
* "PUEBLA"
* "QUERETARO"
* "QUINTANA ROO"
* "SAN LUIS POTOSI"
* "SINALOA"
* "SONORA"
* "TABASCO"
* "TAMAULIPAS"
* "TLAXCALA"
* "VERACRUZ"
* "YUCATAN"
* "ZACATECAS"
* "NACIDO EN EL EXTRANJERO"
* "NE"

## LICENCIA

MIT
