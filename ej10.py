#!/usr/bin/env python3
"""
Autor : Agueda Rico <10663412@iespenyagolosa.es>
Fecha   : 8/11/22
Propósito: programa que pida un número y calcule su factorial.
"""

num = int(input('Dime un número: '))
factorial = 1

for i in range (1,num+1):
    factorial = factorial*i

print (f'El factorial del número {num} es {factorial}')