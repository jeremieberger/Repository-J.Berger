#!/usr/bin/python3.7
# -*-coding:utf-8 -*

# Copyright Nyrlathotep 2018. All Rights reserved.

from modulesPerso.userInterface import userInt, userRestart

restart = True

while restart is not False:
    i = 0
    height = 8
    espaces = 0
    chaine = ""
    chaine1 = ""
    height = userInt("Quelle doit-être la hauteur du sapin ? : ")
    size = height
    while height > 0:
        chaine += "/"
        while i > 0 and espaces < i:
            if height > 1:
                chaine += " "
                espaces += 1
            else:
                chaine += "_"
                espaces += 1
        chaine += "\\"
        print(chaine.center(2 * size))
        chaine = ""
        chaine1 = ""
        espaces = 0
        i += 2
        height -= 1
    print("||".center(size * 2))
    restart = userRestart()
