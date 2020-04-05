#!/usr/bin/python3.7
# -*-coding:utf-8 -*

# Copyright Jérémie Berger 2018. All Rights reserved.

import random


def passwordGeneration(length=16, all_chars="azertyuiopqsdfghjklmwxcvbn" +
                       "AZERTYUIOPQSDFGHJKLMWXCVBN0123456789$*_-!?.#%"):
    """Générer le mot de passe avec les paramètres suivants :
    - length : nombre de caractères du mot de passe (16 par défaut).
    - all_chars : le mot de passe sera composé de caractères
    choisis aléatoirement parmi ceux de cette chaine :
    azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789$*_-!?.#%
    Renvoie une chaine de caractères."""

    i = 0
    char = ""  # Stocke un caractère
    pwd = ""  # Stocke le mot de passe

    while i < length:
        char = all_chars[random.randint(0, len(all_chars) - 1)]
        pwd += char
        i += 1

    return pwd


def startAgain():
    """Demander à l'utilisateur si il veut
    recommencer une opération.
    Il peut répondre par o ou n.
    La fonction se répétera si il répond autre chose.
    Renvoie un booléen."""

    restart = False  # Par défaut, on ne recommencera pas l'opération
    start_again = ""  # variable de stockage de l'entrée utilisateur au clavier
    ask_again = True  # détermine si on repose la question à l'utilisateur

    while ask_again:
        start_again = input("\nVoulez-vous recommencer ? o/n : ")
        if start_again == "n":
            ask_again = False
            restart = False
        elif start_again == "o":
            ask_again = False
            restart = True
        else:  # Si jamais l'utilisateur a entré autre chose que "o" ou "n"
            print("\nJe n'ai pas compris votre choix.")

    return restart


def askGeneration():
    """Demander si l'utilisateur souhaite
    générer le mot de passe avec les paramètres par défaut.
    Renvoie un booléen."""

    answer = ""  # stocke la réponse de l'utilisateur
    generate = False  # détermine si le mot de passe peut être généré
    ask_again = True  # détermine si on repose la question à l'utilisateur

    while ask_again:
        answer = input("\nUtiliser les paramètres par défaut ? o/n : ")
        if answer == "o":
            generate = True
            ask_again = False
        elif answer == "n":
            generate = False
            ask_again = False
        else:
            print("\nJe n'ai pas compris votre choix.")

    return generate


def askLength():
    """Demander à l'utilisateur
    la longeur de la chaine à générer.
    Renvoie un entier positif."""

    length = ""  # stocke la longueur choisie pour la chaine
    ask_again = True  # détermine si on repose la question à l'utilisateur

    while ask_again:
        length = input(
            "\nLongueur du mot de passe ? (Minimum : 4, Maximum : 32) : ")
        try:
            length = int(length)
        except ValueError:
            print("\nCeci n'est pas un nombre valide.")
        if length == 0:
            print("\nCette valeur ne peut pas être nulle.")
        elif (length <= -4) and (length >= -32):
            print("\nLa valeur sera positive.")
            try:
                length = abs(length)
                print("\nLe mot de passe fera ", length, " caractères.")
                ask_again = False
            except ValueError:
                print("\nNombre invalide.")
        elif (length >= -4) and (length <= -0):
            print("\nNombre invalide.")
        elif length < -32:
            print("\nNombre invalide.")
        elif length > 0 and length < 4:
            print("\nMinimum 4 caractères.")
        elif length > 32:
            print("\nMaximum 32 caractères.")
        else:
            ask_again = False

    return length


def askLowerCase():
    """Demander à l'utilisateur si il souhaite
    utiliser des minuscules dans le mot de passe.
    Renvoie un booléen."""

    use_lower = False  # détermine si on utilise des minuscules
    ask_lower = ""  # variable de stockage de l'entrée utilisateur
    ask_again = True  # détermine si on repose la question à l'utilisateur

    while ask_again:
        ask_lower = input("\nUiliser des minuscules ? o/n : ")
        if ask_lower == "o":
            use_lower = True
            ask_again = False
        elif ask_lower == "n":
            use_lower = False
            ask_again = False
        else:
            print("\nJe n'ai pas coompris votre choix.")

    return use_lower


def askUpperCase():
    """Demander à l'utilisateur si il souhaite
    utiliser des majuscules dans le mot de passe.
    Renvoie un booléen."""

    use_upper = False  # détermine si on utilise des majuscules
    ask_upper = ""  # variable de stockage de l'entrée utilisateur
    ask_again = True  # détermine si on repose la question à l'utilisateur

    while ask_again:
        ask_upper = input("\nUiliser des majuscules ? o/n : ")
        if ask_upper == "o":
            use_upper = True
            ask_again = False
        elif ask_upper == "n":
            use_upper = False
            ask_again = False
        else:
            print("\nJe n'ai pas coompris votre choix.")

    return use_upper


def askNumbers():
    """Demander à l'utilisateur si il souhaite
    utiliser des chiffres dans le mot de passe.
    Renvoie un booléen."""

    use_number = False  # détermine si on utilise des chiffres ou pas
    ask_number = ""  # variable de stockage de l'entrée utilisateur
    ask_again = True  # détermine si on repose la question à l'utilisateur

    while ask_again:
        ask_number = input("\nUtiliser des chiffres ? o/n : ")
        if ask_number == "o":
            use_number = True
            ask_again = False
        elif ask_number == "n":
            use_number = False
            ask_again = False
        else:
            print("\nJe n'ai pas coompris votre choix.")

    return use_number


def askSpecials():
    """Demander à l'utilisateur si il souhaite
    utiliser des caractères spéciaux dans le mot de passe.
    Renvoie un booléen."""

    use_specials = False  # détermine si on utilise des caractères spéciaux
    ask_specials = ""  # variable de stockage de l'entrée utilisateur
    ask_again = True  # détermine si on repose la question à l'utilisateur

    while ask_again:
        ask_specials = input("\nUtiliser des caractères spéciaux ? o/n : ")
        if ask_specials == "o":
            use_specials = True
            ask_again = False
        elif ask_specials == "n":
            use_specials = False
            ask_again = False
        else:
            print("\nJe n'ai pas coompris votre choix.")

    return use_specials


def defineSpecials():
    """Demander à l'utilisateur de définir
    quels caractères spéciaux il veut utiliser.
    Renvoie une chaine de caractères."""

    chaine = ""
    chars = ""
    ask_again = True

    while ask_again:
        chars = input(
            "\nCaractères spéciaux à utiliser ? (Entrée pour continuer) : ")
        if chars == "":
            ask_again = False
        else:
            chaine += chars

    return chaine


recommencer = True
caracteres_possibles = ""
password = ""
majuscules = False
chiffres = False
speciaux = False
choixSpeciaux = ""
longueur = 0


print("""\n*** Password Generator ***\n
    \nCopyright Nyrlathotep 2018.
    \nTous droits réservés.\n""")

while recommencer:

    demander_generer = askGeneration()

    if demander_generer:

        password = passwordGeneration()
        print("\n")
        print(password, "\n")
        recommencer = startAgain()

    else:
        while caracteres_possibles == "":

            minuscules = askLowerCase()
            if minuscules:
                caracteres_possibles += "azertyuiopqsdfghjklmwxcvbn"
            else:
                print("\nLes minuscules ne seront pas utilisées.")

            majuscules = askUpperCase()
            if majuscules:
                caracteres_possibles += "AZERTYUIOPQSDFGHJKLMWXCVBN"
            else:
                print("\nLes majuscules ne seront pas utilisées.")

            chiffres = askNumbers()
            if chiffres:
                caracteres_possibles += "0123456789"
            else:
                print("\nLes chiffres ne seront pas utilisés.")

            speciaux = askSpecials()
            if speciaux:
                choixSpeciaux = defineSpecials()
                caracteres_possibles += choixSpeciaux
            else:
                print("\nAucun autre caractère ne sera utilisé.")

        longueur = askLength()
        password = passwordGeneration(longueur, caracteres_possibles)
        print("\n")
        print(password, "\n")
        caracteres_possibles = ""
        recommencer = startAgain()

print("""\nMerci d'avoir utilisé Password Generator 2.1.3\n
    Copyright Jérémie Berger 2018. Tous droits réservés.""")
