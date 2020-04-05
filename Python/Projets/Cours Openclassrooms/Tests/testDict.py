#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

# Copyright Jérémie Berger 2019.

# DICTIONNAIRES :

# Non ordonné,c'est un objet conteneur.
# Chaque élément est repéré par une clé.
# Structure : {clé : valeur, clé2, valeur2, etc...}
# Les clés et valeurs peuvent être n'importe quel objet
# de n'importe quel type

mon_dictionnaire = dict()
print(mon_dictionnaire)

# >>> {}

mon_dictionnaire = {}
print(mon_dictionnaire)

# >>> {}

mon_dictionnaire = {}
mon_dictionnaire["pseudo"] = "Prolixe"
mon_dictionnaire["mot de passe"] = "*"
mon_dictionnaire["pseudo"] = "6pri1"
print(mon_dictionnaire)

# >>> {'mot de passe': '*', 'pseudo': '6pri1'}

print(mon_dictionnaire["mot de passe"])

# >>> '*'

# Si la clé n'existe pas dans le dictionnaire,
# une erreur de type KeyError sera levée.

mondictionnaire = {}

# On peut utiliser des entires ou tout type comme clé :

mondictionnaire[0] = "a"
mondictionnaire[1] = "b"
mondictionnaire[3] = "c"
mondictionnaire[4] = "d"
mondictionnaire[5] = "e"
mondictionnaire[6] = "f"
mondictionnaire[7] = "g"
mondictionnaire[8] = "h"
mondictionnaire[9] = "i"
mondictionnaire[10] = "j"

print(mondictionnaire)

# >>> {0: 'a', 1: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j'}


# Exemple avec un échiquier :

echiquier = {}

# Ligne arrière des blancs
echiquier[('a', 1)] = "tour blanche"  # En bas à gauche de l'échiquier
echiquier[('b', 1)] = "cavalier blanc"  # À droite de la tour
echiquier[('c', 1)] = "fou blanc"  # À droite du cavalier
echiquier[('d', 1)] = "reine blanche"  # À droite du fou
# etc...

# Ligne avant des blancs
echiquier[('a', 2)] = "pion blanc"  # Devant la tour
echiquier[('b', 2)] = "pion blanc"  # Devant le cavalier, à droite du pion
# etc...

# Les tuples peuvent être sous-entendus, on pourrait'écrire :
# ['a', 1] etc...

# CREER UN DICTIONNAIRE REMPLI :

placard = {"chemise": 3, "pantalon": 6, "tee-shirt": 7}

# EXEPTION : CREER UN SET :

mon_set = {'pseudo', 'mot de passe'}

print(mon_set)

# Un set est un "dictionnaire sans valeurs", avec des clés uniquement.
# Ces clés doivent bien sur être uniques et on ne peut pas avoir deux
# fois la même clé dans un dictionnaire ou un set.

# SUPPRESSION DE CLES D'UN DICTIONNAIRE :

# Avec DEL :

placard = {"chemise": 3, "pantalon": 6, "tee shirt": 7}
del placard["chemise"]  # Supprime la clé et sa valeur

# Avec la méthode POP :

placard = {"chemise": 3, "pantalon": 6, "tee shirt": 7}
placard.pop("chemise") # Supprime la clé et la valeur et renvoie la valeur

# >>> 3

# STOCKER DES FONCTIONS DANS UN DICTIONNAIRE :

afficher = print  # L'objet print_2 pointera sur la fonction print
afficher("Affichons un message")  # On peut donc se servirde l'objet afficher
                                  # comme d'une fonction identique à print

# >>> Affichons un message

def fonction(message=""):
    print(message)

afficher2 = fonction

afficher2("chaine")

# On peut mettre ces fonctions dans un dictionnaire :

fonctions = {}

fonctions["afficher1"] = afficher
fonctions["afficher2"] = afficher2

print(fonctions)

# Pour appeler une fonction dans un dictionnaire, il faut bian penser
# à ajouter () après nom_dictionnaire[clé_fonction]

fonctions["afficher2"]("un message à afficher")

# dictionnaire[clé]()

# PARCOURIR UN DICTIONNAIRE :

fruits = {"pommes": 21, "melons": 3, "poires": 31}

for cle in fruits:  # On pourrait remplacer cle par nimporte quoi
    print(cle)

# >>> melons
# >>> poires
# >>> pommes

# Avec la méthode keys() :

fruits = {"pommes": 21, "melons": 3, "poires": 31}

for cle in fruits.keys():
    print(cle)

# >>> melons
# >>> poires
# >>> pommes

# La méthode keys(« clés » en anglais) renvoie la liste des clés
# contenues dans le dictionnaire.
# En vérité, ce n'est pas tout à fait une list
# (essayez de taperfruits.keys()dans votre interpréteur)
# mais c'est une séquence qui se parcourt comme une liste.


# PARCOURS DES VALEURS :

fruits = {"pommes": 21, "melons": 3, "poires": 31}

for valeur in fruits.values():  # Méthode de dictionnaire
    print(valeur)

# >>> 3
# >>> 31
# >>> 21

# Utilisation plus courante de la péthode .values :

if 21 in fruits.values():
    print("Un des fruits se trouve dans la quantité 21.")

# >>> Un des fruits se trouve dans la quantité 21.


# PARCOURS SIMULTANE CLE VALEURS :

# On utilise la méthode items qui envoie une liste
# contenant des tuples (clé, valeur)

fruits = {"pommes": 21, "melons": 3, "poires": 31}

for (cle, valeur) in fruits.items():
    print("La clé {} contient la valeur {}.".format(cle, valeur))

# >>> La clé melons contient la valeur 3.
# >>> La clé poires contient la valeur 31.
# >>> La clé pommes contient la valeur 21.


# UTILISER LES DICTIONNAIRES POUR RECUPERER
# DES PARAMETRES NOMMES D'UNE FONCTION :

def fonction_inconnue(**parametres_nommes):
    """Fonction permettant de voir comment récupérer les paramètres nommés
       dans un dictionnaire"""

    print("J'ai reçu en paramètres nommés : {}.".format(parametres_nommes))


fonction_inconnue()  # Aucun paramètre

# >>> J'ai reçu en paramètres nommés : {}

fonction_inconnue(p=4, j=8)  # 2 paramètres

# >>> J'ai reçu en paramètres nommés : {'p': 4, 'j': 8}

# POUR RECUPERER DES PARAMETRES NOMMES ET NON-NOMMES :


def fonction_inconnue(*en_liste, **en_dictionnaire):


# PASSER UN DICTIONNAIRE EN PARAMETRE D'UNE FOONCTION :

parametres = {"sep":" >> ", "end":" -\n"}

print("Voici", "un", "exemple", "d'appel", **parametres)

# >>> Voici >> un >> exemple >> d'appel -

# >>> On pourrait avoir le même résultat avec un print :

print("Voici", "un", "exemple", "d'appel", sep=" >> ", end=" -\n")

