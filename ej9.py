#!/usr/bin/env python3
"""
Autor : Agueda Rico <10663412@iespenyagolosa.es>
Fecha   : 8/11/22
Propósito: escribir lista de números pares que hay entre dos números
"""

n1 = int(input('Dime el vaolor inicial: '))
n2 =int(input('Dime el valor final: '))

for i in range (n1, n2+1):
    if i % 2 ==0:
        print(i,end=', ')
print()