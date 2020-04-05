#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

# Copyright Jérémie Berger 2019.

# Fonctions pour le jeu du pendu du TP Openclassrooms, cours sur Python

# Règles du jeu :
# le programme choisit un mot au hasard dans une liste de mots
# le mot doit faire 8 lettres maximum
# A chaque tour, le joueur choisit une lettre
# Si elle de trouve dans le mot, on affiche le mot avec la lettre
# à sa place ou à plusieurs places si elle est plusieurs fois dans le mot
# Les lettres non trouvées sont affichées avec des *
# Le joueur a 8 tours pour trouver le mot
# Pour calculer le score :
# On prend le score courant, 0 si le joueur n'a pas encore joué
# on ajoute à ce score le nombre de coups restants pour trouver le mot
# exemple : si le joueur a trouvé le mot en 5 coups,
# le score sera de score + 3
# le fichier scores sert à enregistrer les scores
# ils seront sous forme de dictionnaire
# avec en clé le nom du joueur et en valeur son score

# améliorations possibles

# Optionnel, on pourrait avoir la possibilité d'ajouter des mots
# à la liste, en vérifiant qu'ils fassent bien 8 lettres ou moins
# Le problème est qu'on pourrait avoir des mots qui n'existent pas,
# donc il faudrait pouvoir vérifier qu'ils font bien partie de la
# langue française (fichier dictionnaire à trouver, puis à trier
# pour avoir uniquement les mots <= à 8 lettres)

# On  pourrait choisir un niveau de difficulté qui influe sur
# la taille du mot à deviner
# facile : 4 lettres max, normal : 6 lettres max, difficile : 8 lettres max


import random


def user_restart():
    """Fonction servant à demander à l'utilisateur si il veut recommencer.

    Il peut répondre par o ou n, majuscule ou minuscule
    la fonction se répétera si il répond autre chose.
    Elle renvoie un booléen."""

    restart = False
    start_again = ""
    ask_again = True

    while ask_again:
        start_again = input("Voulez-vous recommencer ? o/n : ")
        if start_again == "n" or start_again == "N":
            ask_again = False
            restart = False
        elif start_again == "o" or start_again == "O":
            ask_again = False
            restart = True
        else:
            print("Je n'ai pas compris votre choix.")

    return restart


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


def jouer_tours(chaine="", x=0, mot_secret=""):
    """Sert à faire x tours de jeux avec le mot secret choisi"""

    i = 0
    mot_trouve = ""
    nouveau_mot_trouve = ""
    liste_lettres_trouvees = ""
    nb_tours = 0
    victoire = False
    while i < x and victoire is False:
        mot_trouve = nouveau_mot_trouve
        lettre_choisie = demander_lettre()
        print("vous avez choisi la lettre {}".format(lettre_choisie))
        liste_lettres_trouvees += lettre_choisie
        nouveau_mot_trouve = comparer_chaines(chaine, lettre_choisie)
        if i > 0 and i < x:
            nouveau_mot_trouve = comparer_chaines(
                mot_trouve, nouveau_mot_trouve)
        print(nouveau_mot_trouve)
        nb_tours += 1
        i += 1
        if nouveau_mot_trouve == mot_secret:
            victoire = True
    return (liste_lettres_trouvees, nb_tours, victoire, mot_secret)


def comparer_chaines(chaine1="", chaine2=""):
    """Fonction servant à comparer deux chaines de caractères.

    Renvoie une chaine de caractères avec :
    des * là où les caractères sont différents,
    et la lettre là où elles sont identiques"""

    chaine_finale = ""
    i = 0
    while i < len(chaine1):
        j = 0
        while j < len(chaine2):
            if chaine1[i] == chaine2[j]:
                chaine_finale += chaine1[i]
            elif chaine1[i] == "*" and chaine2[j] != chaine1[i]:
                chaine_finale += chaine2[j]
            elif chaine2[j] == "*" and chaine1[i] != chaine2[j]:
                chaine_finale += chaine1[i]
            elif chaine1[i] == "*" and chaine2[j] == "*":
                chaine_finale += "*"
            elif chaine1[i] != chaine2[j]:
                chaine_finale += "*"
            j += 1
            i += 1
    return chaine_finale


liste_mots = ["pythonthonpy", "python", "thonpy",
              "voiture", "hopital", "service", "maison", "option"]
TOURS = 8
score = 0
mot_trouve = ""
nouveau_mot_trouve = ""
lettre_choisie = ""
gagne = False
liste_resultats = []


def choisir_mot_secret(liste_mots):
    mot_secret = choix_mot(liste_mots)
    print("Un mot secret a été choisi.")
    return mot_secret


def boucle_jeu_principale(mot_secret):
    (liste_finale, nb_tours, gagne) = jouer_tours(
        mot_secret, x=TOURS, mot_secret=mot_secret)
    liste_resultats = list((liste_finale, nb_tours, gagne))
    return liste_resultats


def calculer_score(max=0, tours=0):
    score = max - tours
    return score


def verifier_victoire(liste_resultats):
    if liste_resultats[2]:
        print("Vous avez gagné ! Bravo !")
        print("le mot à trouver était \"{}\"".format(liste_resultats[3]))
        print("Vous avez gagné en {} tours.".format(liste_resultats[1]))
        score = calculer_score(TOURS, liste_resultats[1])
        print(
            "Votre score est donc de {} - {} = {}"
            .format(liste_resultats[1], TOURS, score))
    else:
        print("Vous avez perdu !")
    return score


def jouer(liste_mots):
    mot = ""
    liste = []
    score = 0
    mot = choisir_mot_secret(liste_mots)
    liste = boucle_jeu_principale(mot)
    score = verifier_victoire(liste)
    return score


def main():
    continuer = True
    score = 0
    while continuer:
        nouveau_score = jouer(liste_mots)
        score += nouveau_score
        continuer = user_restart()
    return score


main()
