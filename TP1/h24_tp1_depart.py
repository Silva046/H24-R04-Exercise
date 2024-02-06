import os
import csv
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

NOM_ÉTUDIANT = "Baccichet, Vincent" # Écrivez votre nom et prénom ici
GROUPE_ÉTUDIANT = "1080"         # Écrivez votre groupe ici.



# Objectif :
# Vous avez un fichier csv : "resultats_evaluation.csv". Il s'agit de résultats d'évaluations d'étudiants.
# On veut que vous en extrayiez l'information.
# Que vous faisiez des calculs pour faire une analyse statistique.
# Puis que vous transformiez les résultats obtenus en un dictionnaire.


###################################################################
##                          Partie 1                            ###
###################################################################

# Vous devez lire et extraire les informations du csv "resultats_evaluation.csv"
# Le format de ce csv ne permet pas d'extraire les données très facilement. Regardez-le avant de commencer.

# Ce csv contient 20 étudiants, chaque ligne correspondant à l'ID unique de l'étudiant, son nom, son programme, et le résultat de 8 évaluations. 5 Tps et 3 examens.

# Le but de cette partie est d'obtenir une liste qui contient chacune des valeurs du csv.
# MAIS, nous n'avons pas besoin du nom de l'étudiant ou du programme.

liste_etudiants = []

with open("resultats_evaluation.csv" , encoding='utf-8') as csv_file :
    csv_reader = csv.reader(csv_file , delimiter=';')
    next(csv_reader)
    next(csv_reader)
    for line in csv_reader :
        note = line[3:]
        identifiant = [line[0]]
        identifiant.extend(note)
        liste_etudiants.append(identifiant)
print(liste_etudiants)







# À la fin de cette partie. "liste_etudiants" doit contenir toutes la valeurs des étudiants. Sauf le nom et le programme de l'étudiant



###################################################################
##                          Partie 2                            ###
###################################################################

# On veut savoir le nombre d'étudiants ayant passé le cours ainsi que la moyenne de ceux ayant passé le cours.
# À partir de la "liste_etudiants" produite dans la partie 1, passé au travers et prenez note du nombre d'étudiants ayant passé et de leur note finale.
# Le cours est à double seuil, un étudiant doit avoir une moyenne de 60% ou plus dans la partie TPs AINSI qu'une moyenne de 60% ou plus dans la partie examen.
#       SI UN ÉTUDIANT À MOINS DE 60% dans une des deux parties, ca note final ne peut pas être supérieur à la note dans cette partie.

# À la fin de cette partie, on veut imprimer : 
#           - Le nombre d'étudiants ayant passé.
#           - La moyenne de ces étudiants
#           - La moyenne de tous les étudiants
#           - Le taux de succès au cours (pourcentage d'étudiants ayant passé)
tp = liste_etudiants[1:6]
exam = liste_etudiants[6:]










###################################################################
##                          Partie 3                            ###
###################################################################

# On veut créer une liste de dictionnaires à partir de la liste obtenue dans la partie 1.
# Pour chaque étudiant on veut 3 paires clefs-valeurs dans le dictionnaire :
#               "ID" : Le id de l'étudiant
#               "note" : La note finale de l'étudiant.
#               "echec" : Une booléenne ayant la valeur True si l'étudiant échoue. Sinon la valeur False.
#
# Une fois cette liste de dictionnaire obtenue, imprimez-la dans le terminal. 


