#!/usr/bin/env python

'''Divisió entera. Fem la divisio de dos nombres enters i donem sortida del
quocient i el residu'''

# institut icaria
# Programació- 1r Batxillerat- Curs 2023-24

'''L'usuari introdueix dos nombres enters, el programa divideix el dos nombres
i retorna la divisió
i retorna el resultat (quocient) i el seu residu.'''

__author__ = "Adrian Busquets Azzi"
__email__ = "abusquets@instituticaria.cat"
__date__ = "2024/10/21"


Divident = int(input('introdueix el divident'))
Divisor = int(input('introdueix el divisor'))
Quocient = Divident // Divisor
Residu = Divident % Divisor
print(f'Divisió: {Divident}/{Divisor}')
print(f'Quocient: {Quocient}')
print(f'Residu: {Residu}')