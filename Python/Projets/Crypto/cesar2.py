#!/usr/lib/python3.6
# -*-coding:utf-8 -*

# Copyright Jérémie Berger 2019. All rights reserved.

# Ce programme sert à chiffrer une chaine de caractères selon l'algorithme de césar


alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&é\"'(-è_çà)=ù*,;:!"


def translation(chaine, x):
    """
     Effectue une translation de x caractères vers la droite:
     >>> translation('abcde', 2)
     'cdeab'
    """
    return chaine[x:] + chaine[:x]


def index(lettre, chaine):
    """
     Trouve l'index de lettre dans la chaine:
     >>> index('n', 'bonjour')
     2
    """
    for i in range(len(chaine)):
        if (lettre == chaine[i]):
            return i
    return -1


def chiffre(chaine, x):
    """
     Chiffre une chaîne quelconque
     >>> chiffre('Bonjour les amis!', 3)
     'Erqmrxu ohv dplv!'
    """
    r_min = translation(alphabet, x)
    resultat = ''
    for lettre in chaine:
        if lettre in alphabet:
            resultat = resultat + r_min[index(lettre, alphabet)]
        else:
            resultat = resultat + lettre
    return resultat


chaine = input(
    "entrez une chaine sans majuscules ni " +
    "chiffres ni ponctuation seulement des espaces :")

decalage = input("entrez un entier pour le décalage :")
decalage = int(decalage)
decalage = decalage % 27

print(decalage)

resultat = chiffre(chaine, decalage)
print(resultat)
