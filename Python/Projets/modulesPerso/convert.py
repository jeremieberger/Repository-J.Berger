#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

# Copyright Nyrlathotep 2018

# Fonctions de conversions

# Conversions de types :

def strToList(chaine = ""):
    """Convertir une chaine de caractères en liste"""

    liste = []
    for elt in chaine:
        liste += elt

    return liste


def listToStr(liste = []):
    """Convertir une liste en chaine de caractères"""

    chaine = ""
    for elt in liste:
        chaine += str(elt)

    return chaine
