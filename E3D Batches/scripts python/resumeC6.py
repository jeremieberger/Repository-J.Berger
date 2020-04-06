#!/usr/bin/python
# -*- coding: utf-8 -*-

from xlrd import *

"""Copyright Jérémie Berger 2020. Tous droits réservés.
Reproduction et usage interdits sans le consentement de l'auteur."""

"""Ce script trouve les appuis sur lesquels il y a une intervention
dans une annexe C6 (demandée à l'utilisateur), puis crée un fichier
texte qui liste tous ces appuis et l'intervention nécessaire."""


def ouvrir_classeur(nom):
    classeur = open_workbook(nom)
    return classeur


def ouvrir_feuille(classeur):
    feuille = classeur.sheet_by_index(-1)
    return feuille


def demander_nom_classeur():
    nom = input("Entrez le nom complet de l'annexe C6 à traiter :\n")
    return nom


def chercher_lignes(feuille, index_lignes=8, numero_colonne=31):
    """cherche les lignes où la colonne 32 contient qqch,
    à partir de la ligne 9"""
    dictionnaire = dict()
    while index_lignes < feuille.nrows:
        valeur = str(feuille.cell_value(index_lignes, numero_colonne))
        if valeur != "":
            dictionnaire[index_lignes] = valeur
        index_lignes += 1
    return dictionnaire


def chercher_appuis(feuille, dictionnaire):
    dico_appuis = {}
    for cle, valeur in dictionnaire.items():
        appui = str(feuille.cell_value(cle, 0))
        dico_appuis[appui] = valeur
    return dico_appuis


def sauver_dictionnaire(dictionnaire, nom):
    nom_fichier = "liste_interventions_"
    nom_fichier += nom.replace(".xlsx", "").replace("Annexe C6_", "")
    nom_fichier += ".txt"
    with open(nom_fichier, 'w') as mon_fichier:
        for appui, travaux in dictionnaire.items():
            mon_fichier.write(f"{appui} : {travaux}\n")
    return nom_fichier


print("\n-----------------RÉSUMÉ ANNEXE C6-----------------\n")
print("Copyright Jérémie Berger 2020. Tous droits réservés.\n")
print("Liste tous les appuis sur lesquels une intervention \n\
est nécessaire depuis une annexe C6 puis les\n\
enregistre dans un fichier texte.\n")
print("ATTENTION : pour que le script fonctionne, il doit se\n\
trouver dans le même répertoire que l'annexe C6.\n")
nom = demander_nom_classeur()
classeur = ouvrir_classeur(nom)
feuille = ouvrir_feuille(classeur)
dico_lignes_ok = chercher_lignes(feuille)
dico_appuis = chercher_appuis(feuille, dico_lignes_ok)
fichier = sauver_dictionnaire(dico_appuis, nom)
print(f"\n{fichier}\ncréé avec succès.\n")
print("Traitement terminé, merci d'avoir utilisé resumeC6.py")
