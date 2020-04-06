#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2020 Jérémie Berger. Tous droits réservés.
# Reproduction, utilisation, commercialisation ou échange sans
# le consentement de l'auteur interdits.

"""tri_enedis trie les appuis enedis présents dans "appuis ENEDIS.txt"
dans l'ordre croissant et les réécrit dans cet ordre dans
"appuis ENEDIS.txt" """


def trouver_appui(chaine):
    """trouve le premier appui enedis "E00*" trouvé
    dans la chaine"""
    i = chaine.find("E00")
    appui = chaine[i:i + 7]
    chaine = chaine.replace(appui, "")
    return chaine, appui

chaine2 = ""
with open("Appuis ENEDIS.txt", 'r') as fichier:
    chaine = fichier.read()

appui = "x"
liste = []
while appui != "":
    chaine, appui = trouver_appui(
        chaine)
    if appui != "":
        liste.append(appui)
print(liste)
liste.sort()
print(liste)

for elt in liste:
    chaine2 += elt
    chaine2 += "\n"
print(chaine2)

with open("Appuis ENEDIS.txt", 'w') as fichier:
    fichier.write(chaine2)
