#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

# Copyright Nyrlathotep 2018

liste = list()
print(liste)

liste2 = ["blablabla", 8978, []]
print(liste2)

liste4 = [1, 2, 3, "les listes c'est juste énorme !"]

liste3 = [1, 2 / 3, 5, 879, 0, 787, "dfgdf", liste4]
print(liste3)
print(liste3[0], liste3[1], liste3[2], liste3[7], liste4[3])

# On va se faire une fonction pour parcourir une liste
# et afficher tous ses éléments avec print
# à l'horizontale ou à la verticale


def parcourirListe(liste):
    """Cette fonction sert à parcourir une liste ou une chaine
    Elle est mieux que for,
    car elle détecte les erreurs de type éventuelles"""

    # Déjà on teste si c'est vraiment une liste

    possible = False
    i = 0

    try:
        liste = list(liste)
    except TypeError:
        possible = False
    else:
        possible = True

    # Ensuite seulement on parcourt la liste

    if not possible:
        print("Ce n'est pas une liste valide.")
    elif possible:
        while i < len(liste):
            print(liste[i])
            i += 1


liste5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste6 = 1235

parcourirListe(liste5)

# Ca devrait faire un peu comme un for

for element in liste5:
    print(element)

chaine = "une chaine de caractères"
liste7 = [1, 2, "une chaine", [1, 12, 14, 16, 18]]
liste_vide = []
chaine_vide = ""


def strToList(chaine=""):

    liste_vide = []
    for elt in chaine:
        liste_vide += elt

    return liste_vide


liste_vide = strToList(chaine)
print("la !", liste_vide)


def listToStr(liste=[]):

    chaine_vide = ""
    for elt in liste:
        chaine_vide += str(elt)

    return chaine_vide


chaine_vide = listToStr(liste7)
print("ici!", chaine_vide)

# là on voit que ça sert à rien de changer le type
# De liste à chaine ou inversemnent car ca ne marche juste pas
# mais sans renvoyer d'erreur contrairement aux autres types
# MYSTERE...
# Peut-être que en fait il crée bien une liste mais avec la chaine
# en position 0
# Du coup si on fait liste = list(chaine)
# liste[0] == chaine
# Donc il faudrait décomposer la chaine avec un for avant d'en faire une liste

liste8 = ["a", "b", "c", "d", "e", "f", "g"]
print(liste8)
str(liste8)
print(liste8)
liste8.append("h")
print(liste8)

chaine2 = "une autre chaine"

chaine3 = chaine2.upper()

print(chaine2)
print(chaine3)

liste8.insert(3, "un intrus !")
print(liste8)

liste2.extend(liste3)  # ATTENTION extend ne prend qu'un seul argument
print(liste2)

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste3 = [7, 8, 9]

print(liste1 + liste2 + liste3)

print(liste1)

liste1 += liste2
liste1 += liste3

print(liste1)

del liste1[3]

print(liste1)

liste1.remove(7)

print(liste1)

for i, elt in enumerate(liste1):
    print("à l'indice {} se trouve {}.".format(i, elt))

for elt in enumerate(liste1):
    print(elt)

for elt in enumerate(liste8):
    print(elt)


autre_liste = [
    [1, 'a'],
    [4, 'd'],
    [7, 'g'],
    [26, 'z'],
]  # J'ai étalé la liste sur plusieurs lignes

for nb, lettre in autre_liste:
    print("La {}e lettre de l'alphabet est la lettre {}.".format(nb, lettre))

# Définir des tupples

tupleVide = ()
tupple1 = (1,)
tupple2 = 2,
tupple3 = (1, 2, 3)

# Contrairement aux listes les tuples ne peuvent plus être modifiés
# une fois créés

# Affectation multiple avec des tuples :

(a, b, c, d) = (1, 2, 3, 4)
e, f, g, h = 5, 6, 7, 8  # Et sans tuples, comme on fait d'habitude

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)


def divisionEuclidienne(numerateur, denominateur):
    """Sert à diviser numerateur par denominateur
    Donne la partie entière et le reste de la division"""

    partieEntiere = numerateur // denominateur
    reste = numerateur % denominateur

    return partieEntiere, reste


resultat = divisionEuclidienne(12.564812368798, 3.25)
print(resultat)

resultat1, resultat2 = divisionEuclidienne(25, 6)

print(divisionEuclidienne(25, 6))
print(resultat1)
print(resultat2)


def fonction_inconnue(*parametres):
    """Test d'une fonction pouvant être appelée
    avec un nombre variable de paramètres"""

    print("J'ai reçu : {}.".format(parametres))


fonction_inconnue()
fonction_inconnue(35)
fonction_inconnue(35, "chaine", 54)


def fonctionSpace(obligatoire, *options, param1="chaine par défaut",
                  param2="chaine par défaut 2"):
    """Test de fonction avec des paramètres obligatoires
    et des paramètres optionnels"""

    print(options, param1, param2, obligatoire)


fonctionSpace("paramètre obligatoire", "chaine de test", param1="chaine perso")

tuple1 = ()  # création d'un tuple vide

print(type(tuple1))

# REGLE : il faut mettre les paramètres indéfinis obligatoires (parametre)
# puis les paramètres optionnels (*options)
# puis les paramètres définis par défaut (parametre_defini = valeur_par_defaut)

def Regle(parametre_obligatoire, *parametres_optionnels, parametres_definis="valeur"):
    """Voila la règle pour l'ordre des paramètres lors de la
 définition d'une fonction"""

# on révise la fonction enumerate

liste9 = [1, 2, 3, 4, 5, 6, 7 ,8 , 9]
liste11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

liste10 = enumerate(liste9)
print(list(liste10))

# Elle transforme une séquence ou tout autre itérable
# en tuples (position, element)
# MAIS : pour les afficher, il faut convertir ce que renvoie enumerate
# en liste ou en tuple
