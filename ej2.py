#!/usr/bin/env python3
"""
Autor : Agueda Rico <10663412@iespenyagolosa.es>
Fecha   : 25/10/22
Propósito: Conversión de segundos a minutos
"""

print('Convertidor de segundos a minutos')
segundos = int(input('Escribe un tiempo en segundos: '))
minutos = segundos//60
segundos_restantes = segundos % 60
print(f'{segundos} segundos son {minutos} minutos y {segundos_restantes} segundos')

