#!/usr/bin/env python3
"""
Autor : Agueda Rico <10663412@iespenyagolosa.es>
Fecha   : 9/11/22
Propósito: programa que pida números y escriba el mayor, el menor y la media.
"""

numeros = int(input('¿Cuantos valores vas a introducir?: ')) 
minimo = 0
maximo = 0
suma = 0
media = 0

for i in range (1, numeros+1):
    num =int(input(f'Dime el número {i}: '))
    suma+=num
    if num < minimo:
        minimo = num
    if num > maximo:
        maximo = num
media = suma / numeros
print(f'El número más pequeño de los introducidos es: {minimo}')
print(f'El número más grande de los introducidos es: {maximo}')
print(f'La media de los números introducidos es: {media}')
