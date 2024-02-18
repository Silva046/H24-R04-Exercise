import os
os.chdir(os.path.dirname(__file__)) # place la console dans le même répertoire que ce script, on peut donc utiliser un chemin relatif pour ouvrir les fichiers dans le même répertoire.

#exercice de fonctions
#3 fichiers json sont disponnibles. Chaque fichier contient une liste dictionnaires.
# Chaque dictionnaire contient 3 clefs : Prenom, Nom, ID.
# On veut s'assurer qu'il n'y a pas duplication de ID dans chaque liste.

# Pour ce faire, on utilisera deux listes (vides initialement)
#       Une liste recevra tous les IDs depuis les fichiers json
#       L''autre liste recevra les IDs ayant des duplicata

#faites un fonction qui :   1- Prends un nom de fichier en paramètre,
#                           2- Ouvre le fichier json du même nom
#                           3- Convertie le contenue du fichier liste de dictionnaires
#                           3- Qui vérifie que l'ID n'existe pas déja dans la liste d'ID
#                               4a- si l'ID n'existe pas déja --> ajouté l'ID à la liste d'IDs.
#                               4b- si l'ID existe déjà --­> ajoute l'ID à la liste d'IDs ayant des duplicatas.
#
#Appeller cette fonction pour les 3 fichiers json.

import json


list_id = []
list_id_duplicata = []


# squelette du code pour vous aidez à commencer. Vous pouvez le modifier autant que vous voulez et n'etes pas obligner de l'utiliser :
nom_fichier = "gr2010.json"
def fonction(): # cette fonction doit prendre un nom de fichier en paramètres
    list_id = []
    list_id_duplicata = []
    with open("","r") as fichier : # open doit prendre un nom de fichier en paramètres
        
        # lire le contenue du fichier avec .read() et le mets dans une variable sous forme str
        # convertire la chaine de carachtères en liste de dictionnaires avec json.loads() et mettre dans une variable
        data = json.loads(fichier.read())
        
    #passer a travers chacun des dictionnaires
    # si l'ID n'extiste pas dans list_id --> l'ajouter à list_id
    # sinon l'ajouter à list_id_duplicata 

    # imprimer les IDs ayant des duplicata



