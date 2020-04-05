#!/usr/bin/python3
# -*-coding:Utf-8 -*

# Copyright Nyrlathotep 2018

def cesarLettre(lettre_initiale="a", decalage=3,
                alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']):
    
    decalage == int((decalage % 26))
    nouvelle_lettre = alphabet[decalage]

    return str(nouvelle_lettre)

lettre_choisie = input("choisissez une lettre unique :")
decalage_choisi = input("Choisissez un décalage (nombre entier) :")

def cesar(chaine = "chaine par défaut"):

    chaine_finale = ""
    i = 0

    print(chaine_a_coder)

    while i < len(chaine_a_coder):
        chaine_finale += cesarLettre(lettre_initiale = lettre_choisie, decalage = decalage_choisi)
        i += 1

    print(chaine_finale)

    return chaine_finale

chaine_a_coder = input("Entrez un message à coder :")
print(cesar(chaine_a_coder))
