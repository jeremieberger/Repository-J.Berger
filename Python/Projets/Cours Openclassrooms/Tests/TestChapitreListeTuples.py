#!/usr/bin/python3.7
# -*-coding:utf-8 -*

# Copyright Jérémie Berger 2019


def afficher_flottant(flottant):
    """Fonction prenant en paramètre un flottant et renvoyant
    une chaîne de caractères représentant la troncature de ce nombre.
    La partie flottante doit avoir une longueur maximum de 3 caractères.

    De plus, on va remplacer le point décimal par la virgule"""

    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entière n'est pas à modifier
    # Seule la partie flottante doit être tronquée
    return ",".join([partie_entiere, partie_flottante[:3]])


resultat = afficher_flottant(3.99999999999998)

print(resultat)


def afficher(*parametres, sep=" ", fin="\n"):
    """Fonction servant à afficher imitant la fonction print."""

    parametres = list(parametres)  # Je transforme en liste le tuple de base

    for i, parametre in enumerate(parametres):  # tuple (indice, parametre)
        parametres[i] = str(parametre)  # On transforme chaque param en chaine

    chaine = sep.join(parametres)  # On lie les params avec sep en séparateur
    chaine += fin  # On ajoute le saut de ligne à la fin

    print(chaine, end='')  # et on print la chaine finale
                           # On met end = '' pour pas avoir
                           # deux sauts de ligne :
                           # celui du print et celui
                           # de notre fonction afficher


afficher("Ceci n'est pas un exercice !")
