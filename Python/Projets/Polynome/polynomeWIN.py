# -*-coding:utf-8 -*
#!/usr/bin/python3.7

# Copyright Nyrlathotep 2018. All Rights reserved.

# Importation des bibliothèques ou de leurs fonctions

import os
from math import sqrt # Importation de la fonction racine carrée depuis la bibliothèque math

# Initialisation des variables

solution=0
solution1=0
solution2=0
start_again=True

#Initialisation des fonctions

def resolutionPolynome(a=0,b=0,c=0):
	"""Fonction servant à résoudre un polynôme du second degré"""

	carre=lambda nb: nb*nb

	d=(carre(b))-(a*c*4)

	print("\nDelta =",d) # C'est toujours intéréssant de connaitre la valeur de Delta

	if d<0 :
		print("\nIl n'y a pas de solution dans R")
	elif d==0:
		solution=(-b-sqrt(d))/(a*2)
		print("\nIl y a une solution dans R qui est", solution)
	else:
		solution1=(-b-sqrt(d))/(a*2)
		solution2=(-b+sqrt(d))/(a*2)
		print("\nIl y a deux solutions dans R qui sont",solution1,"et",solution2)

def ResolutionUtilisateur(continuer=False):
	"""Fonction permettant à un utilisateur de résoudre un polynôme du second degré en entrant les valeurs de son choix pour a, b et c"""

	print("\nCe programme permet de résoudre un polynôme du second degré de forme ax²+bx+c\n")
	x=input("\nValeur de a ? ")
	y=input("\nValeur de b ? ")
	z=input("\nValeur de c ? ")

	# On vérifie que ce qui est entré par l'utilisateur est bien un entier naturel (à changer pour relatifs voire flottants)

	x=int(x)
	y=int(y)
	z=int(z)

	print("\nLe polynome est (",x,"x² ) + (",y,"x ) + (",z,")")


	resolutionPolynome(x,y,z)

def demanderRecommencer():
	"""Fonction servant à demander à l'utilisateur si il veut recommencer une action.
	Il peut répondre par o ou n et la fonction se répétera si il répond autre chose.
	Elle renvoie un booléen."""

	redemander=True

	while redemander==True :
		startAgain=input("\nVoulez-vous recommencer ? o/n")
		if startAgain=="n":
			redemander=False
			recommencer=False
		elif startAgain=="o":
			redemander=False
			recommencer=True
		else:
			redemander=True

	return recommencer

# Début du programme côté utilisateur

while start_again==True:
	ResolutionUtilisateur()
	start_again=demanderRecommencer()

print("\nFin du programme.")

os.system("pause")

# Améliorations :
# Pouvoir entrer des flottants