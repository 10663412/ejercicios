#!/usr/bin/env python3
"""
Autor : Agueda Rico <10663412@iespenyagolosa.es>
Fecha   : 10/11/22
Propósito: programa que pide frase y vocal y cambia todas las vocales de la frase por la vocal.
"""

frase = 'tengo una hormiguita en la barriga'
vocal = input('Dime una vocal: ')
VOCALES = 'aeiou'
frase_nueva = []

for i in range (len(frase)):
    if frase [i] in VOCALES:
        frase_nueva.append (vocal)
    else:  
        frase_nueva.append (frase[i])

print (f'La frase es ahora: {frase_nueva}')