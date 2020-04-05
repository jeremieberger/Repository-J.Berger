#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

# Copyright Jérémie Berger 2019.

# Jeu du pendu pour le TP d'Openclassrooms pour le cours sur Python

# Règles du jeu :
# le programme choisit un mot au hasard dans une liste de mots OK
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


print("\n")
print("""    | | ___ _   _    __| |_   _  |  _ \\ ___ _ __   __| |_   _ 
 _  | |/ _ \\ | | |  / _` | | | | | |_) / _ \\ '_ \\ / _` | | | |
| |_| |  __/ |_| | | (_| | |_| | |  __/  __/ | | | (_| | |_| |
 \\___/ \\___|\\__,_|  \\__,_|\\__,_| |_|   \\___|_| |_|\\__,_|\\__,_|""")
print("version alpha 0.0.1".center(62, " "))
print("\n", "Copyright Jérémie Berger 2019. Tous droits réservés.".center(62, " "), "\n")
