#!/usr/bin/python3.7
# -*-coding:utf-8 -*

# Copyright Nyrlathotep 2018. All Rights reserved.

"""Module regroupant les fonctions d'interface utilisateur.
Les fonctions test* servent à tester si une variable peut être convertie
en un type donné.
Les fonctions user* sont des fonctions d'interactions basiques
avec l'utilisateur."""

# définition des fonctions test*


def testInt(var):
    """Fonction servant à tester si une variable peut être convertie
    en type Integer.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = int(var)
    except ValueError:
        possible = False

    return possible


def testFloat(var):
    """Fonction servant à tester si une variable peut être convertie
    en type Float.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = float(var)
    except ValueError:
        possible = False

    return possible


def testStr(var):
    """Fonction servant à tester si une variable peut être convertie
    en type String.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = str(var)
    except ValueError:
        possible = False

    return possible


def testLong(var):
    """Fonction servant à tester si une variable peut être convertie
    en type Long.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = long(var)
    except ValueError:
        possible = False

    return possible


def testComplex(var):
    """Fonction servant à tester si une variable peut être convertie
    en type Complex.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = complex(var)
    except ValueError:
        possible = False

    return possible


def testUnicode(var):
    """Fonction servant à tester si une variable peut être convertie
    en type Unicode.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = unicode(var)
    except ValueError:
        possible = False

    return possible


def testBasestring(var):
    """Fonction servant à tester si une variable peut être convertie
    en type Basestring.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = basestring(var)
    except ValueError:
        possible = False

    return possible


def testTuple(var):
    """Fonction servant à tester si une variable peut être convertie
    en type Tuple.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = tuple(var)
    except ValueError:
        possible = False

    return possible


def testList(var):
    """Fonction servant à tester si une variable peut être convertie
    en type List.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = list(var)
    except ValueError:
        possible = False

    return possible


def testXrange(var):
    """Fonction servant à tester si une variable peut être convertie
    en type Xrange.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = xrange(var)
    except ValueError:
        possible = False

    return possible


def testDict(var):
    """Fonction servant à tester si une variable peut être convertie
    en type Dict.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = dict(var)
    except ValueError:
        possible = False

    return possible


def testSet(var):
    """Fonction servant à tester si une variable peut être convertie
    en type Set.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = set(var)
    except ValueError:
        possible = False

    return possible


def testFrozenset(var):
    """Fonction servant à tester si une variable peut être convertie
    en type Frozenset.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = frozenset(var)
    except ValueError:
        possible = False

    return possible


def testObject(var):
    """Fonction servant à tester si une variable peut être convertie
    en type Object.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = object(var)
    except ValueError:
        possible = False

    return possible


def testSlice(var):
    """Fonction servant à tester si une variable peut être convertie
    en type Slice.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = slice(var)
    except ValueError:
        possible = False

    return possible


def testBool(var):
    """Fonction servant à tester si une variable peut être convertie
    en type Bool.
    Elle renvoie True si c'est le cas et False si ce n'est pas possible."""

    possible = True

    try:
        var = bool(var)
    except ValueError:
        possible = False

    return possible

# Définition des fonctions user*


def userRestart():
    """Fonction servant à demander à l'utilisateur si il veut
    recommencer une opération.
    Il peut répondre par o ou n et la fonction se répétera si il répond
    autre chose.
    Elle renvoie un booléen."""

    restart = False
    start_again = ""  # variable de stockage de l'entrée utilisateur au clavier
    ask_again = True  # variable pour savoir si on repose la question

    while ask_again:
        start_again = input("Voulez-vous recommencer ? o/n : ")
        if start_again == "n" or start_again == "N":
            ask_again = False
            restart = False
        elif start_again == "o" or start_again == "O":
            ask_again = False
            restart = True
        else:  # Si jamais l'utilisateur a entré autre chose que "o" ou "n"
            print("Je n'ai pas compris votre choix.")

    return restart


def userInt(string="Entrez un nombre entier : "):
    """Fonction servant à demander à l'utilisateur d'entrer un Integer.
    Si il entre autre chose, on lui redemande d'entrer un nombre."""

    ask_again = True
    user_input = ""
    var = 0

    while ask_again:
        user_input = input(string)
        try:
            user_input = int(user_input)
            ask_again = False
        except ValueError:
            print("Ce n'est pas un nombre valide.")
            ask_again = True
    var = int(user_input)

    return var


def userFloat(string="Entrez un nombre à virgule flottante : "):
    """Fonction servant à demander à l'utilisateur d'entrer un Integer.
    Si il entre autre chose, on lui redemande d'entrer un nombre."""

    ask_again = True
    user_input = ""
    var = 0

    while ask_again:
        user_input = input(string)
        try:
            user_input = float(user_input)
            ask_again = False
        except ValueError:
            print("Ce n'est pas un nombre valide.")
            ask_again = True
    var = float(user_input)

    return var
