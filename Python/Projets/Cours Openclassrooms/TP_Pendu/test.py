#!/usr/bin/python3.7
# pendutests

import random

def choix_mot(liste):
    """Choisit un mot dans la liste envoyée en paramètre"""

    x = random.randint(0, len(liste) - 1)
    mot = liste[x]
    return mot


def entrer_lettre():
    """Demande à l'utilisateur d'entrer une lettre"""

    lettre = input("entrez une lettre :")
    return lettre


def verifier_lettre(lettre=""):
    """Vérifie que la lettre fait bien partie de l'alphabet.

    Elle peut être en minuscule ou en majuscule"""

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lettre = lettre.lower()
    continuer = True
    if lettre not in alphabet or lettre == "":
        print("Merci d'entrer une seule lettre de l'alphabet latin")
        continuer = False
    return continuer


def verifier_longueur(chaine=""):
    """Vérifie que la chaine en paramètre n'ait qu'un seul caractère"""

    continuer = True
    if len(chaine) > 1 or len(chaine) < -1:
        print("Merci d'entrer une seule lettre de l'alphabet latin")
        continuer = False
    return continuer


def demander_lettre():
    """Demande d'entrer une lettre puis l'affiche.

    Fait les vérifications necéssaires et la change en minuscule"""

    ok = False
    while not ok:
        lettre = entrer_lettre()
        ok = verifier_lettre(lettre) and verifier_longueur(lettre)
    #print(lettre.lower())
    return lettre.lower()


def entrer_nom():
    """demande à l'utilisateur d'enter son nom.

    Il sera automatiquement du type string"""

    nom = ""
    nom = input("Entrez votre nom :")
    return nom


def verifier_longueur_nom(nom):
    """Vérifie que le nom fasse 20 caractères maximum"""

    ok = True
    if len(nom) > 20:
        ok = False
    return ok


def demander_nom():
    """Demande d'entrer le nom du joueur puis l'affiche

    Vérifie que le nom soit de 20 lettres ou moins"""

    ok = False
    while not ok:
        nom = entrer_nom()
        if verifier_longueur_nom(nom):
            print(nom)
            ok = True
        else:
            print("nom trop long (20 caractères maximum)")
    return nom


def compter_mot(mot=""):
    i = 0
    for elt in mot:
        i += 1
    return i


def comparer_lettres(lettre1, lettre2):
    ok = False
    if lettre1 == lettre2:
        ok = True
    return ok


# La fonction comparer_chaines servira à la fois:
# à comparer le mot secret à une lettre choisie
# mais aussi à remplacer l'ancienne chaine trouvée par la nouvelle
def comparer_chaines(chaine1="", chaine2=""):
    """Fonction servant à comparer deux chaines de caractères.

    Renvoie une chaine de caractères avec :
    des * là où les caractères sont différents,
    et la lettre là où elles sont identiques"""

    print("log : on va comparer {} et {}".format(chaine1, chaine2))

    chaine_finale = ""
    i = 0
    while i < len(chaine1):
        j = 0
        while j < len(chaine2):
            if chaine1[i] == "*":
                chaine_finale += "*"
            elif chaine1[i] == chaine2[j] and chaine1[i] != "*":
                chaine_finale += chaine1[i]
            elif chaine1[i] != "*" and chaine2[j] == "*":
                chaine_finale += chaine1[i]
            else:
                chaine_finale += "*"
            j += 1
            i += 1
    return chaine_finale


chaine1 = "python"
chaine2 = "y"


nouvelle_chaine = comparer_chaines(chaine1, chaine2)
print(nouvelle_chaine)
