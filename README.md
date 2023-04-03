# MXCurpy

Generación de Clave Única de Registro de Población y el Registro Federal de Contibuyentes de México en Python.

Documentos en los que está basado este paquete:

CURP: (/docs/dof18102021.pdf)[INSTRUCTIVO NORMATIVO PARA LA ASIGNACIÓN DE LA CLAVE ÚNICA DE REGISTRO DE
POBLACIÓN]

RFC:

## Estado actual del proyecto

Por el momento está funcionando la creación de CURP, por lo que he decidido liberarlo para poder usarlo.

## Uso

```python
from mxcurpy.curp import curp

my_curp = curp(names="Juan José", lastname="Martínez", second_lastname="Pérez", birth_date="12-08-1989", birth_state="Durango", sex="h")

# MAPJ890812HDGRRN00

```

## Limitaciones

## CURP

Los dod últimos carácteres al final de la CURP oficial son generados por la entidad de gobierno encargada de asignación de las curps al momento de genrarla, con el objetivo de
evitar duplicados, por lo que no podemos generarlos con seguridad, por eso estos dos carácteres siempre serán "00".

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

## LICENCIA

MIT
