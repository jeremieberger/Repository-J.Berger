#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

# Copyright Jérémie Berger 2019.

# Récapitulaatif du chapitre sur les fichiers d'Openclassrooms

import os

os.chdir("/home/babe/Git/perso/Python/Projets/Cours Openclassrooms/Tests")
# Change le répertoire courantdu programme

os.getcwd()  # Renvoie le répertoire courant
print(os.getcwd())

fichier = open("fichier.txt", "r")
# les modes d'ouverture sont :
# (r)ead,
# (w)rite, ATTENTION : efface le contenu du fichier, et crée le fichier si inexistant
# (a)ppend crée le fichier si inexistant, sinon ajout à la fin),
# (b)inary ouverture en mode binaire
print(fichier)
print(type(fichier))

contenu = fichier.read()  # "Lit" intégralement le fichier ouvert en mode read
# read est une méthode de la classe TextIoWrapper

fichier.close()  # IMPORTANT : ferme le fichier après utilisation

fichier = open("fichier.txt", "w")  # Ouvre le fichier et efface tout son contenu
fichier.write("Chaine à ajouter au fichier\n")  # Ecrit dans le fichier
fichier.close()

fichier = open("fichier.txt", "a")  # Ouvre le fichier en mode append
fichier.write("Nouvelle chaine ajoutée\n")  # Ajoute la chaine en fin de fichier
fichier.close()

# ATTENTION : la méthode write n'accepte que des chaines en paramètre

with open("fichier.txt", "r") as fichier:  # autre moyen d'ouvrir un fichier, plus safe
    contenu = fichier.read()
    print(contenu)
# C'est plus safe car si une exception se produit, le fichier sera fermé quand même
# automatiquement à la fin du bloc d'instructions

if fichier.closed:
    print("le fichier est bien fermé")

# la méthode closed renvoie True si le fichier est fermé et False sinon
# ATTENTION ELLE NE PREND PAS DE PARENTHESES !!!!

fichier = open("fichier.txt", "a")
fichier.write("Nouvelle chaine ajoutée\n")
fichier.close()

if fichier.closed:
    print("le fichier est bien fermé")

with open("fichier.txt", "r") as fichier:
    print(contenu)

if fichier.closed:
    print("le fichier est bien fermé")
