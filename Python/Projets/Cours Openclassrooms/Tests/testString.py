# -*-coding:utf-8 -*
#!/usr/bin/python3.7

# Copyright Nyrlathotep 2018. All Rights reserved.

# Variables

#chaine = "    CHAINE EN MAJUSCULES !   "

# Importation des modules

import os
from userInterface import userInt

# Fonctions

# Programme

chaine = "abcdefghijklmnopqrstuvwxyz"
chaine1 = "chaine de test"

chaine1 += chaine[:len(chaine)]

print(chaine1)

"""
i = 0
chaine1 = str()

while i < len(chaine):
	chaine1 += (chaine[i])
	i += 1

print(chaine1)

nom = "Berger"
prenom = "Jérémie"
age = 31

print("Je m'appelle {2} {1} et j'ai {0} ans.".\
format(nom, prenom, age))

chaine2 = "Je m'appelle {nom} {prenom} et j'ai\
 {age} ans."\
 .format(nom = input("Entrez votre nom : ").upper(), prenom = input("Entrez votre prénom : ").capitalize(),\
 age = userInt("Entrez votre âge : "))
print(chaine2)

chaine3 = input("Entrez une chaine de caractères : ")
chaine4 = input("Entrez une chaine de caractères : ")
chaine5 = input("Entrez une chaine de caractères : ")
chaine6 = input("Entrez une chaine de caractères : ")
sep = " "

chaine_concatenée = chaine3 + sep + str(age) + chaine4 + sep + chaine5 + chaine6

print(chaine_concatenée)


print(chaine.lower().capitalize().center(64).strip())
print(chaine)
print(len(chaine))

chaine = chaine.lower().capitalize().center(64).strip()
print(chaine)
print(len(chaine))

reponse = str()


while reponse.lower() != "q":
	print("Tapez 'Q' pour quitter...")
	reponse = input()

print("Merci !")
"""

os.system("pause")