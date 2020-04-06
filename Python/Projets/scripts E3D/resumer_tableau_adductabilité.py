import xlrd
import xlwt

"""
objectifs :

récupérer des informations dans le excel tableau adductabilité pour les reporter de façon lisible dans un nouveau excel.

les infos qui nous intéressent :
- nom d'appui
- type d'appui
- immeuble à raccorder
- PB concerné
- adresse (optionnel)

déroulement :

on va dérouler ligne par ligne.
ligne1 : si il y a qqch dans la colonne "commentaires" : récupérer ce qqch puis
combien y at-il de lignes dans cette chaine ?  si plus de 1, les séparer.
récupérer l'immeuble correspondant, le pb, le type d'appui et toutes infos intéressantes.
les classer dans une base de données (dictionnaire ?) AVANT de les reporter dans un tableau. 
classer par ordre croissant des numéros d'appui avant report sur tableau xls

cas particulier : si il y a plus de 1 ligne dans commentaires (si on saute une ligne = si il y a un \n) il faut :
séparer les numéros d'appui (en comptant combien il y en a)
prendre le dernier appui de ces numéros
récupérer les autres infos.

"""