#!/usr/bin/python3.7
# -*-coding:utf-8 -*

# Copyright Jérémie Berger 2019

# LISTES ET TUPLES

# création :

liste = list()

# ou :

liste2 = []

liste3 = [1, 0.0, "chaine", (21, 87), []]

# accéder aux éléments d'une liste :

liste3[0]
liste3[1]
# etc...

# on peut rempacer les éléments d'une liste,
# une liste est MUTABLE, contrairement aux chaines.

liste3[2] = 23

# Ajouter un objet en fin de liste :

liste3.append("chaine2")  # ATTENTION : Cette méthode ne renvoie rien

# CHAINES : Comparaison :

chaine1 = "une petite phrase"
chaine2 = chaine1.upper()  # On met en majuscules chaine1
chaine1  # On affiche la chaîne d'origine
# >>> 'une petite phrase'
# Elle n'a pas été modifiée par la méthode upper
chaine2  # On affiche chaine2
# >>> 'UNE PETITE PHRASE'
# C'est chaine2 qui contient la chaîne en majuscules

# Voyons pour les listes à présent
liste4 = [1, 5.5, 18]
liste5 = []
liste5 = liste4.append(-15)  # On ajoute -15 à liste4
liste4  # On affiche liste1
# >>> [1, 5.5, 18, -15]
# Cette fois, l'appel de la méthode a modifié l'objet d'origine (liste1)
# Voyons ce que contient liste5
# >>> liste5
# Rien ? Vérifions avec print
print(liste5)
# >>> None

# LISTES : Suite :

# Insertion  dans une liste à la position 2 :

liste4.insert(2, 45)
liste4.insert(2, -15)
# etc...

# Concaténation de listes :

liste2.extend(liste3)

# ou

liste4 + liste3

# Suppprimer éléments d'une liste :

# DEL :

var = 34
del var

del liste4[0]

# REMOVE

liste1 = [1, 2, 3, 4, 5, 6]
liste1.remove(2)

# >>> liste1 = [1, 3, 4, 5, 6]

# ATTENTION : Supprime les valeurs données dans l'ordre où il les trouve

# PARCOURS DE LISTES :

ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 0  # Notre indice pour la boucle while
while i < len(ma_liste):
    print(ma_liste[i])
    i += 1

# >>> a
# >>> b
# >>> c
# >>> d
# >>> e
# >>> f
# >>> g
# >>> h

for elt in ma_liste:
    print(elt)

# >>> a
# >>> b
# >>> c
# >>> d
# >>> e
# >>> f
# >>> g
# >>> h

for i, elt in enumerate(ma_liste):

    print("À l'indice {} se trouve {}.".format(i, elt))

# >>> À l'indice 0 se trouve a
# >>> À l'indice 0 se trouve b
# >>> À l'indice 0 se trouve c
# >>> À l'indice 0 se trouve d
# >>> À l'indice 0 se trouve e
# >>> À l'indice 0 se trouve f
# >>> À l'indice 0 se trouve g
# >>> À l'indice 0 se trouve h

for elt in enumerate(ma_liste):

    print(elt)

# >>> (0, 'a')
# >>> (1, 'b')
# >>> (2, 'c')
# >>> (3, 'd')
# >>> (4, 'e')
# >>> (5, 'f')
# >>> (6, 'g')
# >>> (7, 'h')

# enumerate renvoie un tuple avec l'indice et
# l'element présent à cet indice e la séquence

# AUTRE EXEMPLE DE LA PUISSANCE DES LISTES :

autre_liste = [
    [1, 'a'],
    [4, 'd'],
    [7, 'g'],
    [26, 'z'],
]  # J'ai étalé la liste sur plusieurs lignes
for nb, lettre in autre_liste:
    print("La lettre {} est la {}e de l'alphabet.".format(lettre, nb))

# >>> La lettre a est la 1e de l'alphabet.
# >>> La lettre d est la 4e de l'alphabet.
# >>> La lettre g est la 7e de l'alphabet.
# >>> La lettre z est la 26e de l'alphabet.

# TUPLES :

tuple_vide = ()
tuple_non_vide = (1,)  # est équivalent à ci dessous
tuple_non_vide = 1,
tuple_avec_plusieurs_valeurs = (1, 2, 5)

# À la différence des listes, les tuples,
# une fois créés, ne peuvent être modifiés :
# on ne peut plus y ajouter d'objet ou en retirer.

a, b = 3, 4

# est équivalent à :

(a, b) = (3, 4)

# IMPORTANT :
# Quand une fonction renvoie plusieurs valeurs,
# elle les renvoie sous forme de tuple et il faut
# penser à les capturer sous cette forme;

# CHAINES A LISTES :

ma_chaine = "Bonjour à tous"
ma_chaine.split(" ")  # renvoie une liste

# >>> ['Bonjour', 'à', 'tous']

# LISTE A CHAINE :

ma_liste = ['Bonjour', 'à', 'tous']
" ".join(ma_liste)

# >>> 'Bonjour à tous'

# TRANSFORMER LISTE EN PARAMETRES DE FONCTION :

liste_des_parametres = [1, 4, 9, 16, 25, 36]
print(*liste_des_parametres)
# >>> 1 4 9 16 25 36

# COMPREHENSION DE LISTES :

liste_origine = [0, 1, 2, 3, 4, 5]
liste_origine = [nb * nb for nb in liste_origine]

print(*liste_origine)

# >>> [0, 1, 4, 9, 16, 25]

liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste_origine = [nb for nb in liste_origine if nb % 2 == 0]

print(*liste_origine)

# >>> [2, 4, 6, 8, 10]

nouvelle_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
nouvelle_liste = [(nb * nb) for nb in nouvelle_liste
                  if nb % 2 == 0 and nb >= 6]

print(*nouvelle_liste)

# TRI DE LISTE :

inventaire = [("pommes", 22),
              ("poires", 18),
              ("melons", 4),
              ("fraises", 76),
              ("prunes", 51)
              ]

# Fonction SORTED :

# Il faut mettre la quantité avant le nom du fruit :

inventaire_trie = [(x, fruit) for (fruit, x) in inventaire]

print(inventaire_trie)

# On rconstitue l'inventaire en le triant avec la fonction sorted :


inventaire = [(fruit, x) for (x, fruit) in sorted(inventaire_trie,
              reverse=True)]  # Reverse permet l'ordre décroissant

print(inventaire)

# Méthode SORT :

inventaire = [("pommes", 22),
              ("poires", 18),
              ("melons", 4),
              ("fraises", 76),
              ("prunes", 51)
              ]

print(inventaire)

# On change le sens de l'inventaire, la quantité avant le nom

inventaire_trie = [(x, fruit) for (fruit, x) in inventaire]

print(inventaire_trie)

# On trie l'inventaire inversé dans l'ordre décroissant

inventaire_trie.sort(reverse=True)

print(inventaire_trie)

# Et on reconstitue l'inventaire

inventaire = [(fruit, x) for (x, fruit) in inventaire_trie]

print(inventaire)

# ASTUCE : Pour les tuples, les () sont optionnelles,
# par exemple, ici, pour (x, fruit),
# on pourrait mettre x, fruit
# ATTENTION pourtant : ca ne marche pas partout :
# ici [(fruit, x) doit absolument avoir les () sinon erreur.
# Il est donc conseillé de toujours mettre les parenthèses
# pour les tuples.

liste22 = [21, 54, 32, 84, 12, 11, 79, 95, 46, 51, 3, 9, 94]

liste22.sort(reverse=False)

print(liste22)

liste22 = sorted(liste22, reverse=True)

print(liste22)
