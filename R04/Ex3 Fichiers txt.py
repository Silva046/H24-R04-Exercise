import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# import csv package #
import csv




# Le but de cet exercice est de lire le fichier des contributeurs
#    et de copier dans un autre fichier toutes les infos des contributeurs qui ont acceptés de rendre public leurs noms
#    Ce sont, en fait, tous les noms du début du fichier jusqu'à ce que vous avez la mention 'Pas de publication'
#    Donc on arrête de copier les noms aussitôt qu'on lit 'Pas de publication'

#    
# Dans ce script vous allez faire les étapes suivantes:
#   - ouvrir en lecture le fichier Ex3_contributeursNomPrenom.csv, avec l'encodage 'utf=8'
#   - ouvrir en écriture un nouveau fichier que vous appellerez contributeursPublics.csv
#   - Avec une boucle for, vous allez lire chaque ligne du premier fichier pour ensuite l'écrire dans le deuxième fichier
#     MAIS vous allez arrêter la copie quand au lieu du nom d'une personne, vous aurez 'Pas de publication'
with open("Ex3_contributeursNomPrenom.csv" , encoding='utf-8') as csv_file :
    csv_reader = csv.reader(csv_file , delimiter=',')
    next(csv_reader)
    with open("Contributeurs_Nom_Prénom" , "w" , encoding='utf-8') as csv_file_writer :
        csv_writer = csv.writer(csv_file_writer , delimiter=',' , lineterminator="\n")
        for line in csv_reader :
            if "Pas de publication" in line[0] :
                break 
            else :
                csv_writer.writerow(line)





            




