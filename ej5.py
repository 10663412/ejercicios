#!/usr/bin/env python3
"""
Autor : Agueda Rico <10663412@iespenyagolosa.es>
Fecha   : 31/10/22
Propósito: Calcular el área de un triángulo o de un círculo.
"""

print ('Cálculo de áreas.­ Elige una figura geométrica:')
print ('a) Triángulo')
print ('b) Círculo')
eleccion = input('¿Qué figura quieres calcular (escribe T o C)?')
if eleccion == 'T':
   base = float(input('Escribe la base: '))
   altura = float(input('Escribe la altura: '))
   area = base*altura/2
   print (f'Un triángulo de base {base} y altura {altura} tiene un área de {area}')
elif eleccion == 'C':
    radio = float(input('Escribe el radio: '))
    area = 3.14*radio**2
    print(f'Un círculo de radio {radio} tiene un área de {area}')
else:
    print    