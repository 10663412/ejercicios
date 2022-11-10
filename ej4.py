#!/usr/bin/env python3
"""
Autor : Agueda Rico <10663412@iespenyagolosa.es>
Fecha   : 26/10/22
Propósito: Dar solución a equaciones de segundo grado.
"""

print ('Ecuación  ax² + bx + c = 0')

a = int(input('Escribe el valor del coeficiente a: '))
b = int(input('Escribe el valor del coeficiente b: '))
c = int(input('Escribe el valor del coeficiente c: '))
solucion1 = (-b + ((b**2 -4*a*c)**(1/2)))/(2*a)
solucion2 = (-b - ((b**2 -4*a*c)**(1/2)))/(2*a)
print (f'las soluciones de la equación son {solucion1} y {solucion2}')