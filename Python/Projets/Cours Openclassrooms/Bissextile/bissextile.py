#!/usr/bin/python3.7
# -*-coding:Utf-8 -*
# import os

bissextile=False

# Saisie de l'année et transformation en nombre

annee = input("Saisissez une année : ")
annee = int(annee)

print('\n') # Saut de ligne
print(annee) # Affiche de de l'année saisie
print('\n') # Saut de ligne


# NOTE : il faudrait ajouter un controle pour etre sur que c'est bien un nombre


# Recherche pour savoir si l'année est bien bissextile

if annee%4==0:
	bissextile=True
 	if annee%100==0:
		if annee%400!=0:
			bissextile=False
		elif annee%400==0:
			bissextile=True
if bissextile==True:
	print ("Cette année est bissextile.")
if bissextile==False:
	print ("Cette annee n'est pas bissextile.")
	
# os.system("pause")