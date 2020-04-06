#!/usr/bin/python
# -*- coding: utf-8 -*-

from xlrd import *
from xlwt import *
import time
from xlutils.copy import copy

"""Copyright Jérémie Berger 2020. Tous droits réservés.
Reproduction et usage interdits sans le consentement de l'auteur."""

"""Génère une Annexe C3 préremplie à partir des informations
présentes dans une Annexe C6."""

generer_log = False


def recup_temps():
    """renvoie la date et l'heure actuels sous forme de chaine formatée"""
    temps = time.localtime()
    format_temps = str()
    format_temps += str(temps.tm_mday)
    format_temps += "/"
    format_temps += str(temps.tm_mon)
    format_temps += "/"
    format_temps += str(temps.tm_year)
    format_temps += " à "
    format_temps += str(temps.tm_hour)
    format_temps += ":"
    format_temps += str(temps.tm_min)
    format_temps += ":"
    format_temps += str(temps.tm_sec)
    return format_temps


def log(chaine):
    """Écrit la chaine donnée dans le fichier log."""
    temps = recup_temps()
    global generer_log
    if generer_log:
        with open("C6oC3.log", 'a') as log:
            log.write(temps)
            log.write(" : ")
            log.write(chaine)
            log.write("\n")


def demander_nom_c6():
    """demande le nom de l'annexe C6"""
    nom = input("Entrez le nom complet de l'Annexe C6 à traiter :\n")
    log("nom de classeur C6 récupéré correctement \
(demander_nom_c3)")
    return nom


def demander_nom_c3():
    """demande le nom de l'annexe C3"""
    nom = input("Entrez le nom complet de l'Annexe C3 à traiter :\n")
    log("nom de classeur C3 récupéré correctement \
(demander_nom_c3)")
    return nom


def ouvrir_classeur(nom):
    """ouvre en écriture le classeur dont on donne le nom"""
    classeur = open_workbook(nom)  # formatting_info=True > NotImplementedYet
    log(f"classeur {nom} ouvert correctement (ouvrir_classeur)")
    return classeur


def ouvrir_feuille_c6(classeur):
    """ouvre la dernière feuille de l'annexe C6,
    classeur qui est en lecture"""
    feuille = classeur.sheet_by_index(-1)
    log("dernière feuille de l'annexe C6 ouverte correctement \
(ouvrir_feuille_c6")
    return feuille


def ouvrir_feuille_c3(classeur):
    """ouvre la deuxième feuille de l'annexe C6,
    classeur qui est en écriture"""
    feuille = classeur.get_sheet(1)
    log("deuxième feuille de l'annexe C3 ouverte correctement \
(ouvrir_feuille_c3)")
    return feuille


def recuperer_appuis(feuille):
    """récupère les numéros présents dans la première colonne d'une feuille,
    à partir de la ligne 8, et les travaux correspondant dans la colonne 31"""
    index_lignes = 8
    dict_appuis = dict()
    while index_lignes < feuille.nrows:
        valeur = str(feuille.cell_value(index_lignes, 0))
        travaux = str(feuille.cell_value(index_lignes, 31))
        if valeur != "":
            dict_appuis[valeur] = travaux
        index_lignes += 1
    log("appuis et travaux récupérés correctement (recuperer_appuis)")
    return dict_appuis


def ecrire_c3(feuille, dictionnaire):
    """écrit dans l'annexe c3 les appuis et travaux,
    dans les deux colonnes A et B"""
    ligne = 12
    for appui, travaux in dictionnaire.items():
        if ligne - 12 != len(dictionnaire) - 1:
            feuille.write(ligne, 3, appui)
            feuille.write(ligne, 12, travaux)
            feuille.write(ligne, 2, "A")
            feuille.write(ligne, 4, "A")
        if ligne > 12:
            feuille.write(ligne - 1, 5, appui)
            feuille.write(ligne - 1, 13, travaux)
        ligne += 1
    log("feuille 2 de l'annexe c3 écrite (ecrire_c3)")


print("\n---------------PRÉREMPLISSAGE ANNEXE C3---------------")
print("Génère une Annexe C3 préremplie à partir d'une Annexe C6")
print("ATTENTION : pour que le script fonctionne, original_C3A.XLSX")
print("et l'Annexe C6 à traiter doivent être dans son répertoire.\n")
nom_c6 = demander_nom_c6()
# nom_c3 = demander_nom_c3()
classeur_c6 = ouvrir_classeur(nom_c6)
classeur_c3 = copy(ouvrir_classeur("original_C3A.XLSX"))  # en écriture
feuille_C6 = ouvrir_feuille_c6(classeur_c6)
feuille_c3 = ouvrir_feuille_c3(classeur_c3)
appuis_travaux = recuperer_appuis(feuille_C6)
ecrire_c3(feuille_c3, appuis_travaux)
classeur_c3.save("C3.xls")
log("nouveau classeur annexe C3 (.xls) créé et sauvegardé")
print("Traitement terminé.\n\
Les infos préremplies sont dans C3.xls")
