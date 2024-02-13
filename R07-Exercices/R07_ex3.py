import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

#exercice de fonctions
#3 fichiers csv sont disponnibles. On veut s'assurer qu'il n'y a pas duplication de ID
#initialiser une liste vide qui recevra les ID depuis les fichiers csv
#faites un fonction qui :   1-Prends un nom de fichier en paramètre,
#                           2-Ouvre et parcoure le fichier csv du même nom
#                           3-Qui vérifie que l'ID n'existe pas déja dans la liste d'ID
#                               3-si n'existe pas déja qui ajouté les IDs à la liste d'ID.
#Appeller cette fonction pour les 3 csv.
import csv

liste_id = []           #cette liste va contenir tous les IDs, une seule fois chaque ID
list_id_duplicata = []  #cette liste va contenir les IDs qui apparaissent plus d'une fois.

def verif_ID(nom_csv:str):
    pass



verif_ID("gr2010.csv")
verif_ID("gr2060.csv")
verif_ID("gr3460.csv")
print(liste_id)
print(list_id_duplicata)


