#!/usr/lib/python3.6
# -*-coding:utf-8 -*

# Copyright Jérémie Berger 2019. All rights reserved.

"""Ce programme servira à coder un message selon la méthode de Jules César:
Pour un message donné, on transmet également un chiffre
Ce chiffre permet de coder et décoder le message.
En effet, le principe est de décaler les lettres de l'alphabet selon
le chiffre en question.
Exemple : a est la première lettre de l'alphabet
si je veux transformer a avec la méthode de César
avec le chiffre 3 en paramètre,
j'obtiendrai la lettre d, en effet,
césar décalait de trois lettres vers la gauche
donc a = d, b = e, c = f, d = g, etc
Mais on voudrait une fonction ou on puise choisir le décalage,
même si le décalage par défaut sera de 3."""

lettre_initiale = ""
decalage = 3  # défaut
nouvelle_lettre = ""

# On va faire une fonction qui permet de changer une lettre
# En une autre selon un int en paramètre, et bien sur la lettre

# def cesarLettre(chaine_initiale = "", chaine_codee = "", decalage = 3):

# une première fonction servira à transformer juste une lettre

"""Je  voudrais avoir une fonction pour le codage de césar.
cesar("une chaine", int(un_décalage)) et obtenir ainsi
une chaine décalée dans l'alphabet de la valeur de décalage
Exemple : cesar("abc", 3) = "def".
"""

chaine = "message a coder"  # ATTENTION à bien mettre l'espace dans l'alphabet
chaine_codee = ""
alphabet = ""


def cesar(chaine="chaine par defaut", decalage=0):

    alphabet_liste = ["a", "b", "c", "d", "e", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "y", "v", "w", "x", "y", "z", " "]
    alphabet_chaine = "abcdefghijklmnopqrstuvwxyz "
    
    alphabet = alphabet_chaine

    print(alphabet)

    place_lettre = chaine.index(lettre)

    for lettre in chaine:
        lettre = alphabet[place_lettre]

print()


def translation(chaine, x):
    """
     Effectue une translation de x caractères vers la droite:
     >>> translation('abcde', 2)
     'cdeab'
    """
    return chaine[x:] + chaine[:x]


def index(c, chaine):
    """
     Trouve l'index de c dans la chaine:
     >>> index('n', 'bonjour')
     2
    """
    for i in range(len(chaine)):
        if (c == chaine[i]):
            return i
    return -1


def index2(c, chaine):
    """
     Trouve l'index de c dans la chaine:
     >>> index('n', 'bonjour')
     2
    """
    for i in range(len(chaine)):
        if (c == chaine[i]):
            return i
    return -1


def chiffre_minuscules(chaine, x):
    """
     Chiffre une chaîne composée de minuscules
     >>> chiffre_minuscules('bonjour', 3)
     'erqmrxu'
    """
    r = translation(minuscules, x)
    resultat = ''
    for lettre in chaine:
        resultat = resultat + r[index(lettre, minuscules)]
    return resultat
