# -*-coding:Utf-8 -*
#!/usr/bin/python3.7

# Copyright Nyrlathotep 2018

#import os
# WINDOWS UNIQUEMENT, sert à mettre le programme en pause à la fin

# Début du programme :


def compteur(chaine_a_compter) :
	"""Fonction servant à compter le nombre de caractères dans une chaine."""
	str(chaine_a_compter)
	i=0
	for lettre in chaine_a_compter :
		i+=1
	print("Il y a ",(i)," lettres dans cette chaine de caracteres.")

#def compteurNb(nb_a_compter) :
#	int(nb_a_compter)
#	j=0
#	while j<lenght(nb_a_compter):
#		j+=1
#	print("Il y a ",(j)," chiffres dans ce nombre.")


#help(compteur)

chaine=raw_input("Entrez une chaine de caractères SVP :")
#str(chaine)
print(chaine)
compteur(chaine)

nombre=input("Entrez un nombre SVP :")
int(nombre)
print(nombre)



# Fin du programme.

#os.system("pause")
# WINDOWS UNIQUEMENT, affiche un message "appuyez sur une touche pour terminer"
