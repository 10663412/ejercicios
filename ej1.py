#!/usr/bin/env python3
"""
Autor : Agueda Rico <10663412@iespenyagolosa.es>
Fecha   : 25/10/22
Propósito: Conversión de grados Celsius a Fahranheit
"""

print('Convertidor de grados Celsius a Fahrenheit')
gradosC = float(input('Escribe una temperatura en grados celsius: '))
gradosF = 1.8*gradosC + 32
print(f'{gradosC} celsius son {gradosF} fahrenheit')
