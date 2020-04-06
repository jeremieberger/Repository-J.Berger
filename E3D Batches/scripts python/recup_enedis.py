#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2020 Jérémie Berger. Tous droits réservés.
# Reproduction, utilisation, commercialisation ou échange sans
# le consentement de l'auteur interdits.

# feuille 5
# colonne 15

"""recup_enedis.py récupère les appuis enedis
dans les tableaux excel où il y a des feuilles
adductabilité des aites"""

from xlrd import *
from xlwt import *


def creer_chaine(feuille, colonne):
    """crée une chaine avec le contenu de la colonne donnée"""
    i = 0
    chaine = ""
    while i < feuille.nrows:
        if feuille.cell_value(i, colonne) != "":
            chaine += feuille.cell_value(i, colonne)
            chaine += "\n"
        i += 1
    return chaine


def trouver_appui(chaine):
    """trouve le premier appui enedis "E00*" trouvé
    dans la chaine"""
    i = chaine.find("E00")
    appui = chaine[i:i + 7]
    chaine = chaine.replace(appui, "")
    return chaine, appui


nom_classeur = ""
nom_classeur = input("Quel est le nom du classeur Excel ?")
classeur = open_workbook(nom_classeur)
feuille = classeur.sheet_by_name("adductabilité des sites")
chaine = creer_chaine(feuille, 15)

appui_courant = "x"
liste = []
while appui_courant != "":
    chaine, appui_courant = trouver_appui(
        chaine)
    if appui_courant != "":
        liste.append(appui_courant)

for appui in liste:
    print(appui)

with open("Appuis ENEDIS.txt", 'a') as fichier:
    for appui in liste:
        fichier.write(appui)
        fichier.write(";")
