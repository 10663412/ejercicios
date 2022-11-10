#!/usr/bin/env python3
"""
Autor : Agueda Rico <10663412@iespenyagolosa.es>
Fecha   : 7/11/22
Propósito: escribir varias listas de números consecutivos
"""

n =int(input('Dime un número positivo: '))

while n <= 0:
    print (f'Te he pedidiun número positivo!')
    n = int(input('Dime un número positivo: '))

for i in range (0, n+1):
    print (i,end = ', ')

print()
for i in range (n,0-1, -1):
    print(i,end=', ')

print()
for i in range (1,n):
     print(i,end=', ')

print()
for i in range (n-1,0,-1):
     print(i,end=', ')

print()

for i in range (0, n+1):
    print (i,end = ', ')
for i in range (n-1,0-1, -1):
    print(i,end=', ')

print()





   

