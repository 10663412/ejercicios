#!/usr/bin/env python3
"""
Autor : Agueda Rico <10663412@iespenyagolosa.es>
Fecha   : 10/11/22
Propósito: programa que pida anchura y altura de un triángulo y lo dibuje
"""

anchura = int(input('Anchura del rectamgulo: '))
altura = int(input('Altura del rectángulo: '))


for i in range (altura):
    for j in range (anchura):
        print('*', end = ' ')
    print ()


    