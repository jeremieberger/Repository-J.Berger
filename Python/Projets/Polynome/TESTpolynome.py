# -*-coding:utf-8 -*
#!/usr/bin/python3.7

# Copyright Nyrlathotep 2018. All Rights reserved.

from math import sqrt
# remplacable par import math, si on veut toutes les fonctions contenues dans la bibliothèque

# Début du programme

# Initialisation des variables delta et solutions

solution=0
solution1=0
solution2=0
racine_delta=0

# Future docstring de la fonction polynome()
print("Ce programme permet de résoudre un polynôme du second degré de forme ax²+bx+c ")

#Entrées utilisateur :
a=input("Valeur de a ?")
b=input("Valeur de b ?")
c=input("Valeur de c ?")


# On vérifie que ce qui est entré par l'utilisateur est bien un nombre valide
a=float(a)
b=float(b)
c=float(c)

print("Le polynome est ",a,"x²+",b,"x+",c)

# Calcul du discriminant delta, à simplifier en une ligne
d=(b*b)-(4*(a*c))
#e=a*c
#e*=4
#d-=e

print("Delta =",d) # C'est toujours intéréssant de connaitre la valeur de Delta

a*=2 # Ca aussi ca rien a foutre là, il faut le mettre dans les calculs sur les variables plus bas

if d<0 :
	print("Il n'y a pas de solution dans R")
elif d==0 :
	racine_delta = sqrt(d)
	solution = -(b)-racine_delta
	solution/=a # Ca on peut le raccourcir en une ligne
	print("Il y a une solution dans R qui est",solution)
else :
	racine_delta = sqrt(d)
	solution1 = -(b)-racine_delta
	solution1/=a # Ca on peut le raccourcir en une ligne
	solution2 = -(b)+racine_delta
	solution2/=a # Ca on peut le raccourcir en une ligne
	print("Il y a deux solutions dans R qui sont",solution1,"et",solution2)


# algorithme de fin de programme, pour choisir de recommencer ou de quitter


def demanderRecommencer():

	again=True

	while again==True :
		startAgain=input("Voulez-vous recommencer ? O/N")
		if startAgain=="O":
			again=True
		elif startAgain=="N":
			again=False
			recommencer=False
		else:
			again=True
	return recommencer

print("Fin du programme")

# Fin du programme
	

# Tests à faire : vérifier si l'encodage est bon ou si il faut le changer pour Utf-8

# Améliorations :
# Transformer tout ça sous forme de fonction polynome(), de la forme polynome(a=0,b=0,c=0), comme ça a, b et c sont initialisés à 0 par défaut
# Mettre en place des moyens d'entrer des entiers relatifs, et qui pourront être négatifs pour a, b et c, et pourquoi pas des nombres à virgule flottante

