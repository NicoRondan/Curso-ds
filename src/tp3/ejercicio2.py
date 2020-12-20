"""Dadas las longitudes de los 2 catetos de un triángulo rectángulo, hallar la longitud de la
hipotenusa"""
import math

def hipotenusa(cateto_1, cateto_2):
    exponente = 2
    return math.sqrt( math.pow(cateto_1, exponente) + math.pow(cateto_2, exponente))

print('La hipotenusa es: ', hipotenusa(7, 5))