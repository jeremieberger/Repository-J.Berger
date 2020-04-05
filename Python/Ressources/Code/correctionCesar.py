#############################################################################
"""
 Le Chiffre de César
 Programme pour chiffrer et déchiffrer par décalage
"""
#############################################################################
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


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


def chiffre_minuscules(chaine, x):
    """
     Chiffre une chaîne composée de alphabet
     >>> chiffre_minuscules('bonjour', 3)
     'erqmrxu'
    """
    r = translation(alphabet, x)
    resultat = ''
    for lettre in chaine:
        resultat = resultat + r[index(lettre, alphabet)]
    return resultat


def chiffre(chaine, x):
    """
     Chiffre une chaîne quelconque
     >>> chiffre('Bonjour les amis!', 3)
     'Erqmrxu ohv dplv!'
    """
    r_min = translation(alphabet, x)
    r_maj = translation(alphabet2, x)
    resultat = ''
    for lettre in chaine:
        if lettre in alphabet:
            resultat = resultat + r_min[index(lettre, alphabet)]
        elif lettre in alphabet2:
            resultat = resultat + r_maj[index(lettre, alphabet2)]
        else:
            resultat = resultat + lettre
    return resultat

#############################################################################
# Programme principal
#############################################################################


print(chiffre_minuscules('messagede test', 6))
print(chiffre('Autre message de tests', 6))
