#!/usr/bin/env python3
"""
Autor : Agueda Rico <10663412@iespenyagolosa.es>
Fecha   : 7/11/22
Propósito: escribir lista de números consecutivos del 0 al valor dado
"""


numero = int(input('Dime un número: '))
if numero>=0:
    for i in range (0,numero+1):
        print (i,end=',')
else: 
    for i in range (0,numero-1,-1):
        print (i, end=', ')

print()


