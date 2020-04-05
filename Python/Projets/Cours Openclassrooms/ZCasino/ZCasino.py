#!/usr/bin/python3.7
# -*-coding:utf-8 -*

# Copyright Nyrlathotep 2018. All Rights reserved.

# Importation des modules

import os
import random
import userInterface
import math

# Variables

pot_joueur = 1000  # La somme dont dispose le joueur
mise = 0  # mise choisie par le joueur pour un tour
numero_mise = 0  # numéro choisi par le joueur pour un tour
numero_choisi = 0  # numero choisi par la roulette pour un tour
gain = 0  # Ce que remporte le joueur lors d'un tour
recommencer = True  # Variable pour déterminer si on rejoue

# Programme

print("Vous disposez de", pot_joueur, "$.")
while pot_joueur > 0 and recommencer is True:
    while mise > pot_joueur or mise <= 0:
        mise = userInterface.userInt("Combien souhaitez-vous miser ? : ")
        if mise > pot_joueur:
            print("Vous ne disposez pas de suffisamment d'argent.")
        elif mise == 0:
            print("Vous devez miser au moins 1$.")
        else:
            print("Vous misez", mise, "$.")
    while numero_mise < 1 or numero_mise > 50:
        numero_mise = userInterface.userInt(
            "Sur quel numéro souhaitez vous miser ? (de 1 à 50) : ")
        try:
            numero_mise = int(numero_mise)
        except ValueError:
            print("Ce n'est pas un nombre.")
        if numero_mise < 1 or numero_mise > 50:
            print("Choisissez un numéro compris entre 1 et 50 inclus.")
    print("Vous misez sur le numéro", numero_mise, ".")
    numero_choisi = random.randrange(50)
    numero_choisi += 1
    print("La roulette a tiré le numéro", numero_choisi, ".")
    if numero_choisi == numero_mise:
        gain = mise * 3
        print("Vous gagnez", gain, "$.")
        pot_joueur += gain
    elif (numero_choisi % 2 == numero_mise % 2):
        gain = math.ceil(mise / 2)
        print("Vous gagnez", gain, "$.")
        pot_joueur += gain
    else:
        pot_joueur -= mise
        print("Vous perdez la mise de", mise, "$.")
    mise = 0
    numero_mise = 0
    numero_choisi = 0
    gain = 0
    if pot_joueur > 0:
        print("Vous disposez de", pot_joueur, "$.")
        recommencer = userInterface.userRestart()
    else:
        print("Vous n'avez plus d'argent !")
if pot_joueur <= 0:
    print("Vous avez perdu.")
elif pot_joueur > 0:
    print("Vous quittez la table avec", pot_joueur, "$ en poche.")
os.system("pause")
