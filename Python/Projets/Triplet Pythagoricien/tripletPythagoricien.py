# -*-coding:utf-8 -*
#!/usr/bin/python3.7

# Copyright Nyrlathotep 2018. All Rights reserved.

import math

def tripletPythagoricien(val):
	x = val
	resultat2 = x*(sqrt(3)/2)
	resultat3 = x/2

print("\(", x, resultat2, resultat3, "\)")

# début du programme

valeur = input("Entrez un nombre entier positif :")
tripletPythagoricien(valeur)